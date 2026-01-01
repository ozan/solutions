#include <cuda_runtime.h>

#define BLOCK_SIZE 256
#define NUM_BLOCKS 512
#define GRID_SIZE NUM_BLOCKS *BLOCK_SIZE

__global__ void maxes_per_block(const float *input, float *block_maxes, int N) {
  // Reduce to find the global maximum
  __shared__ float maxes[BLOCK_SIZE];
  int gid = blockDim.x * blockIdx.x + threadIdx.x;
  maxes[threadIdx.x] = -INFINITY;
  __syncthreads();
  if (gid < N) {
    float local_max = input[gid];
    for (int i = gid + GRID_SIZE; i < N; i += GRID_SIZE)
      local_max = max(local_max, input[i]);
    maxes[threadIdx.x] = local_max;

    // block reduction
    for (int delta = BLOCK_SIZE / 2; delta > 0; delta /= 2) {
      __syncthreads();
      if (threadIdx.x < delta)
        maxes[threadIdx.x] =
            max(maxes[threadIdx.x], maxes[threadIdx.x + delta]);
    }
  }

  // set a block max for each block id
  if (threadIdx.x == 0)
    block_maxes[blockIdx.x] = maxes[0];
}

__global__ void overall_max(float *block_maxes, float *mx) {
  for (int delta = NUM_BLOCKS / 2; delta > 0; delta /= 2) {
    if (threadIdx.x < delta)
      block_maxes[threadIdx.x] =
          max(block_maxes[threadIdx.x], block_maxes[threadIdx.x + delta]);
    __syncthreads();
  }
  *mx = block_maxes[0];
}

__global__ void sum_exp(const float *input, float *mx, float *total, int N) {
  // Reduce to find the denominator: the sum of the exponents of vals minus
  // max
  __shared__ float sums[BLOCK_SIZE];
  int gid = blockDim.x * blockIdx.x + threadIdx.x;

  float sum = 0;
  for (int i = gid; i < N; i += GRID_SIZE)
    sum += expf(input[i] - *mx);
  sums[threadIdx.x] = sum;

  for (int delta = BLOCK_SIZE / 2; delta > 0; delta /= 2) {
    __syncthreads();
    if (threadIdx.x < delta)
      sums[threadIdx.x] += sums[threadIdx.x + delta];
  }

  if (threadIdx.x == 0) {
    atomicAdd(total, sums[0]);
  }
}

__global__ void softmax_kernel(const float *input, float *output, float *mx,
                               float *total, int N) {
  int gid = blockDim.x * blockIdx.x + threadIdx.x;
  for (int i = gid; i < N; i += GRID_SIZE)
    output[i] = expf(input[i] - *mx) / *total;
}

// input, output are device pointers (i.e. pointers to memory on the
// GPU)
extern "C" void solve(const float *input, float *output, int N) {
  float *block_maxes, *mx, *total;
  cudaMalloc(&block_maxes, sizeof(float) * NUM_BLOCKS);
  cudaMalloc(&mx, sizeof(float));
  cudaMalloc(&total, sizeof(float));
  cudaMemset(total, 0, sizeof(float));
  maxes_per_block<<<NUM_BLOCKS, BLOCK_SIZE>>>(input, block_maxes, N);
  overall_max<<<1, NUM_BLOCKS>>>(block_maxes, mx);
  sum_exp<<<NUM_BLOCKS, BLOCK_SIZE>>>(input, mx, total, N);
  softmax_kernel<<<NUM_BLOCKS, BLOCK_SIZE>>>(input, output, mx, total, N);
  cudaDeviceSynchronize();
  cudaFree(block_maxes);
  cudaFree(mx);
  cudaFree(total);
}

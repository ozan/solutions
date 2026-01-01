#include <cuda_fp16.h>
#include <cuda_runtime.h>

#define THREADS_PER_BLOCKS 256
#define NUM_BLOCKS 256
#define GRID_SIZE THREADS_PER_BLOCKS *NUM_BLOCKS

void __global__ dot_products(const half *__restrict__ A,
                             const half *__restrict__ B,
                             float *__restrict__ block_results, int N) {
  float __shared__ totals[THREADS_PER_BLOCKS];
  int gid = blockIdx.x * blockDim.x + threadIdx.x;

  float partial = 0;
  for (int i = gid; i < N; i += GRID_SIZE)
    partial += (float)A[i] * (float)B[i];
  totals[threadIdx.x] = partial;

// block reduction
#pragma unroll
  for (int delta = THREADS_PER_BLOCKS / 2; delta > 0; delta /= 2) {
    __syncthreads();
    if (threadIdx.x < delta)
      totals[threadIdx.x] += totals[threadIdx.x + delta];
  }

  // set value within block results
  if (threadIdx.x == 0)
    block_results[blockIdx.x] = totals[0];
}

void __global__ final_reduction(half *__restrict__ result,
                                float *__restrict__ block_results) {
#pragma unroll
  for (int delta = NUM_BLOCKS / 2; delta > 0; delta /= 2) {
    if (threadIdx.x < delta)
      block_results[threadIdx.x] += block_results[threadIdx.x + delta];
    __syncthreads();
  }

  if (threadIdx.x == 0)
    *result = (half)block_results[0];
}

// A, B, result are device pointers
extern "C" void solve(const half *A, const half *B, half *result, int N) {
  float *block_results;
  cudaMalloc(&block_results, NUM_BLOCKS * sizeof(float));
  dot_products<<<NUM_BLOCKS, THREADS_PER_BLOCKS>>>(A, B, block_results, N);
  final_reduction<<<1, NUM_BLOCKS>>>(result, block_results);
  cudaFree(block_results);
}

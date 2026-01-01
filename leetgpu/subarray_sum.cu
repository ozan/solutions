#include <cuda_runtime.h>

#define BLOCK_SIZE 128

void __global__ subarray_sum(const int *__restrict__ input,
                             int *__restrict__ output, int S, int E) {
  int __shared__ subtotals[BLOCK_SIZE];
  int gid = blockDim.x * blockIdx.x + threadIdx.x,
      stride = gridDim.x * blockDim.x, total = 0;
  for (int i = S + gid; i <= E; i += stride)
    total += input[i];
  subtotals[threadIdx.x] = total;

  // block-level reduction
#pragma unroll
  for (int delta = BLOCK_SIZE / 2; delta > 0; delta /= 2) {
    __syncthreads();
    if (threadIdx.x < delta)
      subtotals[threadIdx.x] += subtotals[threadIdx.x + delta];
  }

  // final atomic add per block
  if (threadIdx.x == 0)
    atomicAdd(output, subtotals[0]);
}

// input, output are device pointers (i.e. pointers to memory on the GPU)
extern "C" void solve(const int *input, int *output, int N, int S, int E) {
  // Strategy: grid-stride loop with block level reduction
  subarray_sum<<<256, BLOCK_SIZE>>>(input, output, S, E);
}

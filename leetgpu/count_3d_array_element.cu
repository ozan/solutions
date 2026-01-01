#include <cuda_runtime.h>

void __global__ count_elements(const int *__restrict__ input,
                               int *__restrict__ output, int len, int P) {
  __shared__ int count_in_block;

  int gid = blockDim.x * blockIdx.x + threadIdx.x,
      stride = blockDim.x * gridDim.x, count_local = 0;

  if (threadIdx.x == 0)
    count_in_block = 0;
  __syncthreads();

  for (int i = gid; i < len; i += stride)
    count_local += input[i] == P;

#pragma unroll
  for (int delta = 16; delta >= 1; delta >>= 1)
    count_local += __shfl_down_sync(0xffffffff, count_local, delta);

  if (threadIdx.x % 32 == 0)
    atomicAdd(&count_in_block, count_local);
  __syncthreads();

  if (threadIdx.x == 0)
    atomicAdd(output, count_in_block);
}

// input, output are device pointers (i.e. pointers to memory on the GPU)
extern "C" void solve(const int *input, int *output, int N, int M, int K,
                      int P) {

  // Strategy: treat as just one dimension, since all we need is a count
  // Use grid of 40 * 8 blocks, 256 threads per block, and grid stride loop
  count_elements<<<40 * 8, 256>>>(input, output, N * M * K, P);
}

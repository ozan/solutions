#include <cuda_runtime.h>

__global__ void prefix_sum(const float *__restrict__ input,
                           float *__restrict__ output, int N) {
  int gid = blockDim.x * blockIdx.x + threadIdx.x;

  if (gid >= N)
    return;

  output[gid] = input[gid];
  int mask = 1;

  // TODO can we used shared memory for at least part of this?

  while (mask < N) {
    __syncthreads();
    if (mask & gid) {
      int source = (gid & (~mask)) | (mask - 1);
      output[gid] += output[source];
    }
    mask <<= 1;
  }
}

// input, output are device pointers
extern "C" void solve(const float *input, float *output, int N) {
  int block_size = 256;
  int num_blocks = (N + block_size - 1) / block_size;
  prefix_sum<<<num_blocks, block_size>>>(input, output, N);
}

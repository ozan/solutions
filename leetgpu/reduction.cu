#include <cuda_runtime.h>

#define BLOCK_SIZE 128

void __global__ reduce(const float *__restrict__ input,
                       float *__restrict__ output, int N) {

  double __shared__ shared_sums[BLOCK_SIZE];

  int gid = blockDim.x * blockIdx.x + threadIdx.x,
      stride = gridDim.x * blockDim.x;

  // grid stride loop into thread-local sum
  double thread_sum = 0;
  for (int i = gid; i < N; i += stride)
    thread_sum += input[i];
  shared_sums[threadIdx.x] = thread_sum;

  // tree reduction all the way down... avoid warp reduction complexity with
  // doubles
  for (int delta = BLOCK_SIZE / 2; delta > 0; delta >>= 1) {
    __syncthreads();
    if (threadIdx.x < delta)
      shared_sums[threadIdx.x] += shared_sums[threadIdx.x + delta];
  }

  if (threadIdx.x == 0)
    atomicAdd(output, (float)shared_sums[0]);
}

// input, output are device pointers
extern "C" void solve(const float *input, float *output, int N) {
  reduce<<<40 * 16, 128>>>(input, output, N);
}

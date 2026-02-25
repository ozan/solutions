#include <cuda_runtime.h>

__global__ void clip_kernel(const float *__restrict__ input,
                            float *__restrict__ output, float lo, float hi,
                            int N) {
  int gid = blockIdx.x * blockDim.x + threadIdx.x;
  if (gid < N) {
    output[gid] = fmaxf(lo, fminf(input[gid], hi));
  }
}

// input, output are device pointers
extern "C" void solve(const float *input, float *output, float lo, float hi,
                      int N) {
  int threadsPerBlock = 256;
  int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;

  clip_kernel<<<blocksPerGrid, threadsPerBlock>>>(input, output, lo, hi, N);
  cudaDeviceSynchronize();
}

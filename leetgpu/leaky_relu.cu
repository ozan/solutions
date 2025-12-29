#include <cuda_runtime.h>

__global__ void leaky_relu_kernel(const float* __restrict__ input, float* __restrict__ output, int N) {
    int i = blockDim.x * blockIdx.x + threadIdx.x;
    if (i < N) {
        output[i] = input[i] <= 0 ? 0.01 * input[i] : input[i];
    }
}

// input, output are device pointers (i.e. pointers to memory on the GPU)
extern "C" void solve(const float* input, float* output, int N) {
    int threadsPerBlock = 256;
    int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;
    
    leaky_relu_kernel<<<blocksPerGrid, threadsPerBlock>>>(input, output, N);
    cudaDeviceSynchronize();
}

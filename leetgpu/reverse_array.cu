#include <cuda_runtime.h>

__global__ void reverse_array(float* input, int N) {
    int i = blockDim.x * blockIdx.x + threadIdx.x;
    if (i < N/2) {
        float x = input[N-i-1];
        input[N-i-1] = input[i];
        input[i] = x;
    }
}

// input is device pointer
extern "C" void solve(float* input, int N) {
    int threadsPerBlock = 256;
    int blocksPerGrid = (N/2 + threadsPerBlock - 1) / threadsPerBlock;

    reverse_array<<<blocksPerGrid, threadsPerBlock>>>(input, N);
    cudaDeviceSynchronize();
}
#include <cuda_runtime.h>

__global__ void swiglu_kernel(const float* input, float* output, int halfN) {
    int i = blockDim.x * blockIdx.x + threadIdx.x;
    if (i < halfN) {
        output[i] = input[i] * input[halfN+i] / (1.0f + expf(-input[i]));
    }

}

// input, output are device pointers
extern "C" void solve(const float* input, float* output, int N) {
    int halfN = N / 2;
    int threadsPerBlock = 256;
    int blocksPerGrid = (halfN + threadsPerBlock - 1) / threadsPerBlock;

    swiglu_kernel<<<blocksPerGrid, threadsPerBlock>>>(input, output, halfN);
    cudaDeviceSynchronize();
}

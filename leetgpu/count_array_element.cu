#include <cuda_runtime.h>

__global__ void count_equal_kernel(const int* input, int* output, int N, int K) {
    int i = blockDim.x * blockIdx.x + threadIdx.x,
        stride = blockDim.x * gridDim.x,
        count = 0;
    
    for (int j = i; j < N; j += stride) {
        count += input[j] == K;
    }

    atomicAdd(output, count);
}

// input, output are device pointers (i.e. pointers to memory on the GPU)
extern "C" void solve(const int* input, int* output, int N, int K) {
    int threadsPerBlock = 256;
    int blocksPerGrid = 65535;
    count_equal_kernel<<<blocksPerGrid, threadsPerBlock>>>(input, output, N, K);
    cudaDeviceSynchronize();
}
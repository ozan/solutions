#include <cuda_runtime.h>

__global__ void dot_product(const float* A, const float* B, float* result, int N) {
    int start = blockDim.x * blockIdx.x + threadIdx.x,
        stride = blockDim.x * gridDim.x;
    float total = 0.0f;
    
    for (int i = start; i < N; i += stride) total += A[i] * B[i];

    atomicAdd(result, total);
}

// A, B, result are device pointers
extern "C" void solve(const float* A, const float* B, float* result, int N) {
    int threadsPerBlock = 256;
    int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;
    if (blocksPerGrid > 128) blocksPerGrid = 128;

    dot_product<<<blocksPerGrid, threadsPerBlock>>>(A, B, result, N);

}

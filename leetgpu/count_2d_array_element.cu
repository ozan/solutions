#include <cuda_runtime.h>

__global__ void count_2d_equal_kernel(const int* input, int* output, int N, int M, int K) {
    int xi = blockDim.x * blockIdx.x + threadIdx.x,
        yi = blockDim.y * blockIdx.y + threadIdx.y,
        xstride = blockDim.x * gridDim.x,
        ystride = blockDim.y * gridDim.y,
        total = 0;

    for (int i = yi; i < M; i += ystride) {
        for (int j = xi; j < N; j += xstride) {
            total += input[i * N + j] == K;
        }
    }

    atomicAdd(output, total);
}

// input, output are device pointers (i.e. pointers to memory on the GPU)
extern "C" void solve(const int* input, int* output, int N, int M, int K) {
    dim3 threadsPerBlock(16, 16);
    dim3 blocksPerGrid((M + threadsPerBlock.x - 1) / threadsPerBlock.x,
                              (N + threadsPerBlock.y - 1) / threadsPerBlock.y);
    
    // Cap blocks per grid, to take advantage of stride
    if (blocksPerGrid.x > 128) blocksPerGrid.x = 128;
    if (blocksPerGrid.y > 128) blocksPerGrid.y = 128;

    count_2d_equal_kernel<<<blocksPerGrid, threadsPerBlock>>>(input, output, N, M, K);
    cudaDeviceSynchronize();
}
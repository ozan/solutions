#include <cuda_runtime.h>
#define TILE_DIM 8

__global__ void matrix_transpose_kernel(const float* input, float* output, int rows, int cols) {
    __shared__ float tile[TILE_DIM][TILE_DIM + 1];  // +1 avoids bank conflicts

    int x = TILE_DIM * blockIdx.x + threadIdx.x;
    int y = TILE_DIM * blockIdx.y + threadIdx.y;

    // Load tile (coalesced reads)
    int i = y * cols + x;
    if (i < rows * cols) tile[threadIdx.y][threadIdx.x] = input[i];

    __syncthreads();

    // Write tile (coalesced writes)
    x = TILE_DIM * blockIdx.y + threadIdx.x;
    y = TILE_DIM * blockIdx.x + threadIdx.y;

    i = y * rows + x;
    if (x < rows && y < cols) output[i] = tile[threadIdx.x][threadIdx.y];
}


// input, output are device pointers (i.e. pointers to memory on the GPU)
extern "C" void solve(const float* input, float* output, int rows, int cols) {
    dim3 threadsPerBlock(TILE_DIM, TILE_DIM);
    dim3 blocksPerGrid((cols + threadsPerBlock.x - 1) / threadsPerBlock.x,
                       (rows + threadsPerBlock.y - 1) / threadsPerBlock.y);

    matrix_transpose_kernel<<<blocksPerGrid, threadsPerBlock>>>(input, output, rows, cols);
    cudaDeviceSynchronize();
}

#include <cuda_runtime.h>

__global__ void invert_kernel(unsigned char* image, int width, int height) {
    int i = blockDim.x * blockIdx.x + threadIdx.x;
    if (i < width * height) {
        int pix = i << 2;
        image[pix+0] = ~image[pix+0];
        image[pix+1] = ~image[pix+1];
        image[pix+2] = ~image[pix+2];
    }
}
// image_input, image_output are device pointers (i.e. pointers to memory on the GPU)
extern "C" void solve(unsigned char* image, int width, int height) {
    int threadsPerBlock = 256;
    int blocksPerGrid = (width * height + threadsPerBlock - 1) / threadsPerBlock;

    invert_kernel<<<blocksPerGrid, threadsPerBlock>>>(image, width, height);
    cudaDeviceSynchronize();
}
#include <cuda_runtime.h>

__constant__ float kernel_const[2048];

__global__ void convolution_1d_kernel(const float* __restrict__ input, const float* __restrict__ kernel,
				      float* __restrict__ output, int input_size, int kernel_size) {
    int gid = blockDim.x * blockIdx.x + threadIdx.x;
    int num_shared = blockDim.x + kernel_size - 1;  // block + halo
    extern __shared__ float shared_input[];

    // cooperative loading
    for (int i = threadIdx.x; i < num_shared; i += blockDim.x) {
	int from = blockIdx.x * blockDim.x + i;
	if (from < input_size) shared_input[i] = input[from];
    }

    __syncthreads();

    // convolution, now from shared memory
    if (gid < input_size - kernel_size + 1) {
        float out = 0.0f;
        for (int i = 0; i < kernel_size; i++) out += shared_input[threadIdx.x+i] * kernel[i];
        output[gid] = out;
    }

}

// input, kernel, output are device pointers (i.e. pointers to memory on the GPU)
extern "C" void solve(const float* input, const float* kernel, float* output, int input_size, int kernel_size) {
    int output_size = input_size - kernel_size + 1;
    int threadsPerBlock = 256;
    int blocksPerGrid = (output_size + threadsPerBlock - 1) / threadsPerBlock;
    int shared_mem_size = (threadsPerBlock + kernel_size - 1) * sizeof(float);

    cudaMemcpyToSymbol(kernel_const, kernel, kernel_size * sizeof(float));

    convolution_1d_kernel<<<blocksPerGrid, threadsPerBlock, shared_mem_size>>>(input, kernel, output, input_size, kernel_size);
    cudaDeviceSynchronize();
}

#include <cuda_runtime.h>

__constant__ float c_kernel[1024];

void __global__ convolution_kernel(const float *__restrict__ input,
                                   float *__restrict__ output, int input_rows,
                                   int input_cols, int kernel_rows,
                                   int kernel_cols) {
  int gx = blockDim.x * blockIdx.x + threadIdx.x,
      gy = blockDim.y * blockIdx.y + threadIdx.y,
      output_rows = input_rows - kernel_rows + 1,
      output_cols = input_cols - kernel_cols + 1;

  if (gx >= output_cols || gy >= output_rows)
    return;

  // first pass: naively reaccess gx and gy. TODO cooperative access
  float total = 0.0f;

  for (int i = 0; i < kernel_rows; i++) {
    for (int j = 0; j < kernel_cols; j++) {
      float k = c_kernel[i * kernel_cols + j];
      total += input[(gy + i) * input_cols + (gx + j)] * k;
    }
  }
  output[gy * output_cols + gx] = total;
}

// input, kernel, output are device pointers
extern "C" void solve(const float *input, const float *kernel, float *output,
                      int input_rows, int input_cols, int kernel_rows,
                      int kernel_cols) {

  dim3 block(32, 32);
  dim3 grid((input_cols - kernel_cols + 32) / 32,
            (input_rows - kernel_rows + 32) / 32);

  cudaMemcpyToSymbol(c_kernel, kernel,
                     kernel_rows * kernel_cols * sizeof(float));

  convolution_kernel<<<grid, block>>>(input, output, input_rows, input_cols,
                                      kernel_rows, kernel_cols);
  cudaDeviceSynchronize();
}

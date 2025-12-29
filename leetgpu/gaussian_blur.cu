#include <cuda_runtime.h>

__constant__ float c_kernel[512];

void __global__ blur(const float *__restrict__ input,
                     float *__restrict__ output, int input_rows, int input_cols,
                     int kernel_rows, int kernel_cols) {
  // TODO cooperative access
  int gx = blockDim.x * blockIdx.x + threadIdx.x,
      gy = blockDim.y * blockIdx.y + threadIdx.y, half_kx = kernel_cols / 2,
      half_ky = kernel_rows / 2;

  if (gy >= input_rows || gx >= input_cols)
    return;

  float total = 0.0f;
  for (int iy = 0; iy < kernel_rows; iy++) {
    for (int ix = 0; ix < kernel_cols; ix++) {
      int sx = gx + ix - half_kx, sy = gy + iy - half_ky;

      total +=
          (sx < 0 || sy < 0 || sx >= input_cols || sy >= input_rows)
              ? 0.0f
              : input[sy * input_cols + sx] * c_kernel[iy * kernel_cols + ix];
    }
  }
  output[gy * input_cols + gx] = total;
}

// input, kernel, output are device pointers
extern "C" void solve(const float *input, const float *kernel, float *output,
                      int input_rows, int input_cols, int kernel_rows,
                      int kernel_cols) {
  cudaMemcpyToSymbol(c_kernel, kernel,
                     kernel_rows * kernel_cols * sizeof(float));

  dim3 block(32, 32);
  dim3 grid((input_cols + 32 - 1) / 32, (input_rows + 32 - 1) / 32);

  blur<<<grid, block>>>(input, output, input_rows, input_cols, kernel_rows,
                        kernel_cols);
}

#include <cuda_runtime.h>

__global__ void max_pooling(const float *input, float *output, int N, int C,
                            int H, int W, int H_out, int W_out, int kernel_size,
                            int stride, int padding) {
  int x_out = blockDim.x * blockIdx.x + threadIdx.x,
      y_out = blockDim.y * blockIdx.y + threadIdx.y,
      input_offset = blockIdx.z * H * W,
      output_offset = blockIdx.z * H_out * W_out;

  if (x_out < W_out && y_out < H_out) {
    float val = -INFINITY;
    for (int dy = 0; dy < kernel_size; dy += 1) {
      int y_in = y_out * stride + dy - padding;
      for (int dx = 0; dx < kernel_size; dx += 1) {
        int x_in = x_out * stride + dx - padding;
        if (y_in >= 0 && x_in >= 0 && y_in < H && x_in < W)
          val = max(val, input[input_offset + y_in * W + x_in]);
      }
    }
    output[output_offset + y_out * W_out + x_out] = val;
  }
}

// input, output are device pointers (i.e. pointers to memory on the GPU)
extern "C" void solve(const float *input, float *output, int N, int C, int H,
                      int W, int kernel_size, int stride, int padding) {
  int H_out = (H - kernel_size + 2 * padding) / stride + 1,
      W_out = (W - kernel_size + 2 * padding) / stride + 1;

  dim3 threadsPerBlock(16, 16);
  dim3 blocks((W_out + 16 - 1) / 16, (H_out + 16 - 1) / 16, N * C);

  max_pooling<<<blocks, threadsPerBlock>>>(input, output, N, C, H, W, H_out,
                                           W_out, kernel_size, stride, padding);
}

#include <iostream>
#include <vector>
#include <cmath>
#include <cuda_runtime.h>

extern "C" void solve(const float* input, const float* kernel, float* output,
                      int input_rows, int input_cols, int kernel_rows, int kernel_cols);

bool run_test(const std::vector<float>& input, int input_rows, int input_cols,
              const std::vector<float>& kernel, int kernel_rows, int kernel_cols,
              const std::vector<float>& expected, const char* name) {
    int output_rows = input_rows - kernel_rows + 1;
    int output_cols = input_cols - kernel_cols + 1;
    int output_size = output_rows * output_cols;
    std::vector<float> h_output(output_size);

    float *d_input, *d_kernel, *d_output;
    cudaMalloc(&d_input, input.size() * sizeof(float));
    cudaMalloc(&d_kernel, kernel.size() * sizeof(float));
    cudaMalloc(&d_output, output_size * sizeof(float));

    cudaMemcpy(d_input, input.data(), input.size() * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(d_kernel, kernel.data(), kernel.size() * sizeof(float), cudaMemcpyHostToDevice);

    solve(d_input, d_kernel, d_output, input_rows, input_cols, kernel_rows, kernel_cols);

    cudaMemcpy(h_output.data(), d_output, output_size * sizeof(float), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        std::cout << name << ": CUDA error: " << cudaGetErrorString(error) << std::endl;
        cudaFree(d_input);
        cudaFree(d_kernel);
        cudaFree(d_output);
        return false;
    }

    bool success = true;
    for (int i = 0; i < output_size; i++) {
        if (std::abs(h_output[i] - expected[i]) > 1e-5) {
            std::cout << name << ": Error at index " << i << ": got " << h_output[i]
                      << ", expected " << expected[i] << std::endl;
            success = false;
        }
    }

    cudaFree(d_input);
    cudaFree(d_kernel);
    cudaFree(d_output);

    if (success) std::cout << name << ": PASSED" << std::endl;
    return success;
}

int main() {
    bool all_passed = true;

    // Example 1: 3x3 input, 2x2 kernel
    // Input:     Kernel:
    // 1 2 3      0 1
    // 4 5 6      1 0
    // 7 8 9
    all_passed &= run_test(
        {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f, 9.0f}, 3, 3,
        {0.0f, 1.0f, 1.0f, 0.0f}, 2, 2,
        {6.0f, 8.0f, 12.0f, 14.0f},
        "Example 1"
    );

    // Example 2: 5x5 input, 3x3 kernel
    // Input:              Kernel:
    // 1  2  3  4  5       1 0 1
    // 6  7  8  9  10      0 1 0
    // 11 12 13 14 15      1 0 1
    // 16 17 18 19 20
    // 21 22 23 24 25
    all_passed &= run_test(
        {1.0f, 2.0f, 3.0f, 4.0f, 5.0f,
         6.0f, 7.0f, 8.0f, 9.0f, 10.0f,
         11.0f, 12.0f, 13.0f, 14.0f, 15.0f,
         16.0f, 17.0f, 18.0f, 19.0f, 20.0f,
         21.0f, 22.0f, 23.0f, 24.0f, 25.0f}, 5, 5,
        {1.0f, 0.0f, 1.0f,
         0.0f, 1.0f, 0.0f,
         1.0f, 0.0f, 1.0f}, 3, 3,
        {35.0f, 40.0f, 45.0f,
         60.0f, 65.0f, 70.0f,
         85.0f, 90.0f, 95.0f},
        "Example 2"
    );

    if (all_passed) {
        std::cout << "Success! All 2D convolution tests passed." << std::endl;
    }

    return all_passed ? 0 : 1;
}

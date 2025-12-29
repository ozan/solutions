#include <iostream>
#include <vector>
#include <cmath>
#include <cuda_runtime.h>

extern "C" void solve(const float* input, const float* kernel, float* output,
                      int input_rows, int input_cols, int kernel_rows, int kernel_cols);

bool run_test(const std::vector<float>& input, int input_rows, int input_cols,
              const std::vector<float>& kernel, int kernel_rows, int kernel_cols,
              const std::vector<float>& expected, const char* name) {
    int output_size = input_rows * input_cols;
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
        if (std::abs(h_output[i] - expected[i]) > 1e-4) {
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

    // Example 1: 5x5 input with 3x3 Gaussian kernel
    all_passed &= run_test(
        {1.0f, 2.0f, 3.0f, 4.0f, 5.0f,
         6.0f, 7.0f, 8.0f, 9.0f, 10.0f,
         11.0f, 12.0f, 13.0f, 14.0f, 15.0f,
         16.0f, 17.0f, 18.0f, 19.0f, 20.0f,
         21.0f, 22.0f, 23.0f, 24.0f, 25.0f}, 5, 5,
        {0.0625f, 0.125f, 0.0625f,
         0.125f, 0.25f, 0.125f,
         0.0625f, 0.125f, 0.0625f}, 3, 3,
        {1.6875f, 2.75f, 3.5f, 4.25f, 3.5625f,
         4.75f, 7.0f, 8.0f, 9.0f, 7.25f,
         8.5f, 12.0f, 13.0f, 14.0f, 11.0f,
         12.25f, 17.0f, 18.0f, 19.0f, 14.75f,
         11.0625f, 15.25f, 16.0f, 16.75f, 12.9375f},
        "Example 1"
    );

    // Example 2: 3x3 input with 3x3 kernel
    all_passed &= run_test(
        {10.0f, 20.0f, 30.0f,
         40.0f, 50.0f, 60.0f,
         70.0f, 80.0f, 90.0f}, 3, 3,
        {0.1f, 0.1f, 0.1f,
         0.1f, 0.2f, 0.1f,
         0.1f, 0.1f, 0.1f}, 3, 3,
        {13.0f, 23.0f, 19.0f,
         31.0f, 50.0f, 39.0f,
         31.0f, 47.0f, 37.0f},
        "Example 2"
    );

    if (all_passed) {
        std::cout << "Success! All Gaussian blur tests passed." << std::endl;
    }

    return all_passed ? 0 : 1;
}

#include <iostream>
#include <vector>
#include <cmath>
#include <cuda_runtime.h>

extern "C" void solve(const float* input, const float* kernel, float* output, int input_size, int kernel_size);

bool run_test(const std::vector<float>& input, const std::vector<float>& kernel,
              const std::vector<float>& expected, const char* name) {
    int input_size = input.size();
    int kernel_size = kernel.size();
    int output_size = input_size - kernel_size + 1;
    std::vector<float> h_output(output_size);

    float *d_input, *d_kernel, *d_output;
    cudaMalloc(&d_input, input_size * sizeof(float));
    cudaMalloc(&d_kernel, kernel_size * sizeof(float));
    cudaMalloc(&d_output, output_size * sizeof(float));

    cudaMemcpy(d_input, input.data(), input_size * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(d_kernel, kernel.data(), kernel_size * sizeof(float), cudaMemcpyHostToDevice);

    solve(d_input, d_kernel, d_output, input_size, kernel_size);

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

    // Example 1
    all_passed &= run_test(
        {1.0f, 2.0f, 3.0f, 4.0f, 5.0f},
        {1.0f, 0.0f, -1.0f},
        {-2.0f, -2.0f, -2.0f},
        "Example 1"
    );

    // Example 2
    all_passed &= run_test(
        {2.0f, 4.0f, 6.0f, 8.0f},
        {0.5f, 0.2f},
        {1.8f, 3.2f, 4.6f},
        "Example 2"
    );

    if (all_passed) {
        std::cout << "Success! All 1D convolution tests passed." << std::endl;
    }

    return all_passed ? 0 : 1;
}

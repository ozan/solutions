#include <iostream>
#include <vector>
#include <cmath>
#include <cuda_runtime.h>

extern "C" void solve(const float* input, float* output, int N);

bool run_test(const std::vector<float>& input, const std::vector<float>& expected, const char* name) {
    int N = input.size();
    std::vector<float> h_output(N);

    float *d_input, *d_output;
    cudaMalloc(&d_input, N * sizeof(float));
    cudaMalloc(&d_output, N * sizeof(float));

    cudaMemcpy(d_input, input.data(), N * sizeof(float), cudaMemcpyHostToDevice);

    solve(d_input, d_output, N);

    cudaMemcpy(h_output.data(), d_output, N * sizeof(float), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        std::cout << name << ": CUDA error: " << cudaGetErrorString(error) << std::endl;
        cudaFree(d_input);
        cudaFree(d_output);
        return false;
    }

    bool success = true;
    for (int i = 0; i < N; i++) {
        if (std::abs(h_output[i] - expected[i]) > 1e-5) {
            std::cout << name << ": Error at index " << i << ": got " << h_output[i]
                      << ", expected " << expected[i] << std::endl;
            success = false;
        }
    }

    cudaFree(d_input);
    cudaFree(d_output);

    if (success) std::cout << name << ": PASSED" << std::endl;
    return success;
}

int main() {
    bool all_passed = true;

    // Example 1
    all_passed &= run_test(
        {1.0f, -2.0f, 3.0f, -4.0f},
        {1.0f, -0.02f, 3.0f, -0.04f},
        "Example 1"
    );

    // Example 2
    all_passed &= run_test(
        {-1.5f, 0.0f, 2.5f, -3.0f},
        {-0.015f, 0.0f, 2.5f, -0.03f},
        "Example 2"
    );

    if (all_passed) {
        std::cout << "Success! All Leaky ReLU tests passed." << std::endl;
    }

    return all_passed ? 0 : 1;
}

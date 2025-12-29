#include <iostream>
#include <vector>
#include <cmath>
#include <cuda_runtime.h>

extern "C" void solve(float* input, int N);

bool run_test(std::vector<float> input, const std::vector<float>& expected, const char* name) {
    int N = input.size();

    float *d_input;
    cudaMalloc(&d_input, N * sizeof(float));

    cudaMemcpy(d_input, input.data(), N * sizeof(float), cudaMemcpyHostToDevice);

    solve(d_input, N);

    cudaMemcpy(input.data(), d_input, N * sizeof(float), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        std::cout << name << ": CUDA error: " << cudaGetErrorString(error) << std::endl;
        cudaFree(d_input);
        return false;
    }

    bool success = true;
    for (int i = 0; i < N; i++) {
        if (std::abs(input[i] - expected[i]) > 1e-5) {
            std::cout << name << ": Error at index " << i << ": got " << input[i]
                      << ", expected " << expected[i] << std::endl;
            success = false;
        }
    }

    cudaFree(d_input);

    if (success) std::cout << name << ": PASSED" << std::endl;
    return success;
}

int main() {
    bool all_passed = true;

    // Example 1
    all_passed &= run_test(
        {1.0f, 2.0f, 3.0f, 4.0f},
        {4.0f, 3.0f, 2.0f, 1.0f},
        "Example 1"
    );

    // Example 2
    all_passed &= run_test(
        {1.5f, 2.5f, 3.5f},
        {3.5f, 2.5f, 1.5f},
        "Example 2"
    );

    if (all_passed) {
        std::cout << "Success! All reverse_array tests passed." << std::endl;
    }

    return all_passed ? 0 : 1;
}

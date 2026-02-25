#include <iostream>
#include <vector>
#include <cmath>
#include <cuda_runtime.h>

extern "C" void solve(const float* input, float* output, float lo, float hi, int N);

bool run_test(const std::vector<float>& input, float lo, float hi,
              const std::vector<float>& expected, const char* name) {
    int N = input.size();
    std::vector<float> h_output(N);

    float *d_input, *d_output;
    cudaMalloc(&d_input, N * sizeof(float));
    cudaMalloc(&d_output, N * sizeof(float));

    cudaMemcpy(d_input, input.data(), N * sizeof(float), cudaMemcpyHostToDevice);

    solve(d_input, d_output, lo, hi, N);

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

    // Example 1: [1.5, -2.0, 3.0, 4.5], lo = 0.0, hi = 3.5 -> [1.5, 0.0, 3.0, 3.5]
    all_passed &= run_test(
        {1.5f, -2.0f, 3.0f, 4.5f},
        0.0f, 3.5f,
        {1.5f, 0.0f, 3.0f, 3.5f},
        "Example 1"
    );

    // Example 2: [-1.0, 2.0, 5.0], lo = -0.5, hi = 2.5 -> [-0.5, 2.0, 2.5]
    all_passed &= run_test(
        {-1.0f, 2.0f, 5.0f},
        -0.5f, 2.5f,
        {-0.5f, 2.0f, 2.5f},
        "Example 2"
    );

    // Edge case: all values within range
    all_passed &= run_test(
        {1.0f, 2.0f, 3.0f},
        0.0f, 5.0f,
        {1.0f, 2.0f, 3.0f},
        "All within range"
    );

    // Edge case: all values below lo
    all_passed &= run_test(
        {-5.0f, -3.0f, -1.0f},
        0.0f, 10.0f,
        {0.0f, 0.0f, 0.0f},
        "All below lo"
    );

    // Edge case: all values above hi
    all_passed &= run_test(
        {15.0f, 20.0f, 25.0f},
        0.0f, 10.0f,
        {10.0f, 10.0f, 10.0f},
        "All above hi"
    );

    // Edge case: values exactly at boundaries
    all_passed &= run_test(
        {0.0f, 5.0f, 2.5f},
        0.0f, 5.0f,
        {0.0f, 5.0f, 2.5f},
        "Values at boundaries"
    );

    // Edge case: negative range
    all_passed &= run_test(
        {-10.0f, -5.0f, 0.0f, 5.0f},
        -7.0f, -2.0f,
        {-7.0f, -5.0f, -2.0f, -2.0f},
        "Negative range"
    );

    if (all_passed) {
        std::cout << "Success! All clip_kernel tests passed." << std::endl;
    }

    return all_passed ? 0 : 1;
}

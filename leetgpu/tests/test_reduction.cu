#include <iostream>
#include <vector>
#include <cmath>
#include <cuda_runtime.h>

// Declaration of the solve function from reduction.cu
extern "C" void solve(const float* input, float* output, int N);

bool test_reduction(const std::vector<float>& h_input, float expected, const char* test_name) {
    int N = h_input.size();
    std::cout << "Running " << test_name << " with N=" << N << "..." << std::endl;

    float h_result = 0.0f;

    // Allocate device memory
    float *d_input, *d_output;
    cudaMalloc(&d_input, N * sizeof(float));
    cudaMalloc(&d_output, sizeof(float));

    // Copy data: host -> device
    cudaMemcpy(d_input, h_input.data(), N * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemset(d_output, 0, sizeof(float));

    // Run solution
    solve(d_input, d_output, N);

    // Copy result: device -> host
    cudaMemcpy(&h_result, d_output, sizeof(float), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        printf("CUDA error: %s\n", cudaGetErrorString(error));
        cudaFree(d_input);
        cudaFree(d_output);
        return false;
    }

    // Verify result with tolerance for floating point accumulation errors
    float tolerance = std::max(1e-4f, N * 1e-6f);
    bool success = std::abs(h_result - expected) < tolerance;

    if (success) {
        std::cout << "  Success! Result=" << h_result << ", Expected=" << expected << std::endl;
    } else {
        std::cout << "  Error: Result=" << h_result << ", Expected=" << expected << std::endl;
    }

    // Cleanup
    cudaFree(d_input);
    cudaFree(d_output);

    return success;
}

bool test_reduction_large(int N, const char* test_name) {
    std::cout << "Running " << test_name << " with N=" << N << "..." << std::endl;

    // Allocate host memory
    std::vector<float> h_input(N);
    float h_result = 0.0f;

    // Initialize data and compute expected result
    double expected = 0.0;
    for (int i = 0; i < N; i++) {
        h_input[i] = ((float)(i % 1000) - 500.0f) * 0.01f;  // Values in [-5.0, 4.99]
        expected += (double)h_input[i];
    }

    // Allocate device memory
    float *d_input, *d_output;
    cudaMalloc(&d_input, N * sizeof(float));
    cudaMalloc(&d_output, sizeof(float));

    // Copy data: host -> device
    cudaMemcpy(d_input, h_input.data(), N * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemset(d_output, 0, sizeof(float));

    // Run solution
    solve(d_input, d_output, N);

    // Copy result: device -> host
    cudaMemcpy(&h_result, d_output, sizeof(float), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        printf("CUDA error: %s\n", cudaGetErrorString(error));
        cudaFree(d_input);
        cudaFree(d_output);
        return false;
    }

    // Verify result with tolerance for floating point accumulation errors
    float tolerance = N * 1e-5f;
    bool success = std::abs(h_result - (float)expected) < tolerance;

    if (success) {
        std::cout << "  Success! Result=" << h_result << ", Expected=" << expected << std::endl;
    } else {
        std::cout << "  Error: Result=" << h_result << ", Expected=" << expected << std::endl;
    }

    // Cleanup
    cudaFree(d_input);
    cudaFree(d_output);

    return success;
}

int main() {
    bool all_passed = true;

    // Example 1: [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0] -> 36.0
    all_passed &= test_reduction(
        {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f},
        36.0f,
        "example_1"
    );

    // Example 2: [-2.5, 1.5, -1.0, 2.0] -> 0.0
    all_passed &= test_reduction(
        {-2.5f, 1.5f, -1.0f, 2.0f},
        0.0f,
        "example_2"
    );

    // Test 3: Large input (multiple blocks)
    all_passed &= test_reduction_large(1000000, "large_array_1M");

    // Test 4: Very large input (stress test with many blocks)
    all_passed &= test_reduction_large(10000000, "large_array_10M");

    if (all_passed) {
        std::cout << "\nAll tests passed!" << std::endl;
        return 0;
    } else {
        std::cout << "\nSome tests failed!" << std::endl;
        return 1;
    }
}

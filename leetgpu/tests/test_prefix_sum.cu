#include <iostream>
#include <vector>
#include <cmath>
#include <cuda_runtime.h>

// Declaration of the solve function from prefix_sum.cu
extern "C" void solve(const float* input, float* output, int N);

bool test_prefix_sum(const std::vector<float>& h_input, const std::vector<float>& expected, const char* test_name) {
    int N = h_input.size();
    std::cout << "Running " << test_name << " with N=" << N << "..." << std::endl;

    std::vector<float> h_output(N);

    // Allocate device memory
    float *d_input, *d_output;
    cudaMalloc(&d_input, N * sizeof(float));
    cudaMalloc(&d_output, N * sizeof(float));

    // Copy data: host -> device
    cudaMemcpy(d_input, h_input.data(), N * sizeof(float), cudaMemcpyHostToDevice);

    // Run solution
    solve(d_input, d_output, N);

    // Copy result: device -> host
    cudaMemcpy(h_output.data(), d_output, N * sizeof(float), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        printf("CUDA error: %s\n", cudaGetErrorString(error));
        cudaFree(d_input);
        cudaFree(d_output);
        return false;
    }

    // Verify results with tolerance for floating point errors
    bool success = true;
    for (int i = 0; i < N; i++) {
        float tolerance = std::max(1e-4f, std::abs(expected[i]) * 1e-5f);
        if (std::abs(h_output[i] - expected[i]) > tolerance) {
            std::cout << "  Error at index " << i << ": got " << h_output[i]
                      << ", expected " << expected[i] << std::endl;
            success = false;
            break;
        }
    }

    if (success) {
        std::cout << "  Success!" << std::endl;
    }

    // Cleanup
    cudaFree(d_input);
    cudaFree(d_output);

    return success;
}

bool test_prefix_sum_large(int N, const char* test_name) {
    std::cout << "Running " << test_name << " with N=" << N << "..." << std::endl;

    // Allocate host memory
    std::vector<float> h_input(N);
    std::vector<float> h_output(N);
    std::vector<double> expected(N);

    // Initialize data and compute expected result
    for (int i = 0; i < N; i++) {
        h_input[i] = ((float)(i % 2000) - 1000.0f) * 0.001f;  // Values in [-1.0, 0.999]
    }

    // Compute expected prefix sum using double precision
    expected[0] = (double)h_input[0];
    for (int i = 1; i < N; i++) {
        expected[i] = expected[i-1] + (double)h_input[i];
    }

    // Allocate device memory
    float *d_input, *d_output;
    cudaMalloc(&d_input, N * sizeof(float));
    cudaMalloc(&d_output, N * sizeof(float));

    // Copy data: host -> device
    cudaMemcpy(d_input, h_input.data(), N * sizeof(float), cudaMemcpyHostToDevice);

    // Run solution
    solve(d_input, d_output, N);

    // Copy result: device -> host
    cudaMemcpy(h_output.data(), d_output, N * sizeof(float), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        printf("CUDA error: %s\n", cudaGetErrorString(error));
        cudaFree(d_input);
        cudaFree(d_output);
        return false;
    }

    // Verify results with tolerance for floating point accumulation errors
    bool success = true;
    for (int i = 0; i < N; i++) {
        float tolerance = std::max(1e-2f, std::abs((float)expected[i]) * 1e-4f);
        if (std::abs(h_output[i] - (float)expected[i]) > tolerance) {
            std::cout << "  Error at index " << i << ": got " << h_output[i]
                      << ", expected " << expected[i] << std::endl;
            success = false;
            break;
        }
    }

    if (success) {
        std::cout << "  Success!" << std::endl;
    }

    // Cleanup
    cudaFree(d_input);
    cudaFree(d_output);

    return success;
}

int main() {
    bool all_passed = true;

    // Example 1: [1.0, 2.0, 3.0, 4.0] -> [1.0, 3.0, 6.0, 10.0]
    all_passed &= test_prefix_sum(
        {1.0f, 2.0f, 3.0f, 4.0f},
        {1.0f, 3.0f, 6.0f, 10.0f},
        "example_1"
    );

    // Example 2: [5.0, -2.0, 3.0, 1.0, -4.0] -> [5.0, 3.0, 6.0, 7.0, 3.0]
    all_passed &= test_prefix_sum(
        {5.0f, -2.0f, 3.0f, 1.0f, -4.0f},
        {5.0f, 3.0f, 6.0f, 7.0f, 3.0f},
        "example_2"
    );

    // Test 3: Single element
    all_passed &= test_prefix_sum(
        {42.0f},
        {42.0f},
        "single_element"
    );

    // Test 4: All zeros
    all_passed &= test_prefix_sum(
        {0.0f, 0.0f, 0.0f, 0.0f, 0.0f},
        {0.0f, 0.0f, 0.0f, 0.0f, 0.0f},
        "all_zeros"
    );

    // Test 5: All same values
    all_passed &= test_prefix_sum(
        {3.0f, 3.0f, 3.0f, 3.0f},
        {3.0f, 6.0f, 9.0f, 12.0f},
        "all_same"
    );

    // Test 6: Negative values
    all_passed &= test_prefix_sum(
        {-1.0f, -2.0f, -3.0f, -4.0f},
        {-1.0f, -3.0f, -6.0f, -10.0f},
        "all_negative"
    );

    // Test 7: Alternating positive/negative
    all_passed &= test_prefix_sum(
        {1.0f, -1.0f, 1.0f, -1.0f, 1.0f, -1.0f},
        {1.0f, 0.0f, 1.0f, 0.0f, 1.0f, 0.0f},
        "alternating"
    );

    // Test 8: Power of 2 size (common for GPU algorithms)
    all_passed &= test_prefix_sum(
        {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f, 8.0f},
        {1.0f, 3.0f, 6.0f, 10.0f, 15.0f, 21.0f, 28.0f, 36.0f},
        "power_of_2_size"
    );

    // Test 9: Non-power of 2 size
    all_passed &= test_prefix_sum(
        {1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f, 1.0f},
        {1.0f, 2.0f, 3.0f, 4.0f, 5.0f, 6.0f, 7.0f},
        "non_power_of_2"
    );

    // Test 10: Medium size array
    all_passed &= test_prefix_sum_large(1024, "medium_1K");

    // Test 11: Large array (multiple thread blocks)
    all_passed &= test_prefix_sum_large(100000, "large_100K");

    // Test 12: Very large array (stress test)
    all_passed &= test_prefix_sum_large(10000000, "large_10M");

    // Test 13: Maximum size constraint test
    all_passed &= test_prefix_sum_large(100000000, "max_size_100M");

    if (all_passed) {
        std::cout << "\nAll tests passed!" << std::endl;
        return 0;
    } else {
        std::cout << "\nSome tests failed!" << std::endl;
        return 1;
    }
}

#include <iostream>
#include <vector>
#include <cuda_runtime.h>

// Declaration of the solve function from subarray_sum.cu
extern "C" void solve(const int* input, int* output, int N, int S, int E);

bool test_subarray_sum(const std::vector<int>& h_input, int S, int E, int expected, const char* test_name) {
    int N = h_input.size();
    std::cout << "Running " << test_name << " with N=" << N << ", S=" << S << ", E=" << E << "..." << std::endl;

    int h_result = 0;

    // Allocate device memory
    int *d_input, *d_output;
    cudaMalloc(&d_input, N * sizeof(int));
    cudaMalloc(&d_output, sizeof(int));

    // Copy data: host -> device
    cudaMemcpy(d_input, h_input.data(), N * sizeof(int), cudaMemcpyHostToDevice);
    cudaMemset(d_output, 0, sizeof(int));

    // Run solution
    solve(d_input, d_output, N, S, E);

    // Copy result: device -> host
    cudaMemcpy(&h_result, d_output, sizeof(int), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        printf("CUDA error: %s\n", cudaGetErrorString(error));
        cudaFree(d_input);
        cudaFree(d_output);
        return false;
    }

    // Verify result
    bool success = (h_result == expected);

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

bool test_subarray_sum_large(int N, int S, int E, const char* test_name) {
    std::cout << "Running " << test_name << " with N=" << N << ", S=" << S << ", E=" << E << "..." << std::endl;

    // Allocate host memory
    std::vector<int> h_input(N);
    int h_result = 0;

    // Initialize data (values between 1 and 10 per constraints)
    long long expected = 0;
    for (int i = 0; i < N; i++) {
        h_input[i] = (i % 10) + 1;  // Values in [1, 10]
        if (i >= S && i <= E) {
            expected += h_input[i];
        }
    }

    // Allocate device memory
    int *d_input, *d_output;
    cudaMalloc(&d_input, N * sizeof(int));
    cudaMalloc(&d_output, sizeof(int));

    // Copy data: host -> device
    cudaMemcpy(d_input, h_input.data(), N * sizeof(int), cudaMemcpyHostToDevice);
    cudaMemset(d_output, 0, sizeof(int));

    // Run solution
    solve(d_input, d_output, N, S, E);

    // Copy result: device -> host
    cudaMemcpy(&h_result, d_output, sizeof(int), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        printf("CUDA error: %s\n", cudaGetErrorString(error));
        cudaFree(d_input);
        cudaFree(d_output);
        return false;
    }

    // Verify result
    bool success = (h_result == (int)expected);

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

    // Example 1: input = [1, 2, 1, 3, 4], S = 1, E = 3 -> 6
    all_passed &= test_subarray_sum(
        {1, 2, 1, 3, 4},
        1, 3,
        6,
        "example_1"
    );

    // Example 2: input = [1, 2, 3, 4], S = 0, E = 3 -> 10
    all_passed &= test_subarray_sum(
        {1, 2, 3, 4},
        0, 3,
        10,
        "example_2"
    );

    // Test 3: Single element subarray
    all_passed &= test_subarray_sum(
        {5, 10, 3, 7, 2},
        2, 2,
        3,
        "single_element"
    );

    // Test 4: Full array sum
    all_passed &= test_subarray_sum(
        {1, 2, 3, 4, 5, 6, 7, 8, 9, 10},
        0, 9,
        55,
        "full_array"
    );

    // Test 5: Large input (multiple blocks)
    all_passed &= test_subarray_sum_large(1000000, 100, 999000, "large_array_1M");

    // Test 6: Very large input (stress test)
    all_passed &= test_subarray_sum_large(10000000, 0, 9999999, "large_array_10M");

    // Test 7: Large array with small subarray
    all_passed &= test_subarray_sum_large(10000000, 5000000, 5000100, "large_array_small_range");

    if (all_passed) {
        std::cout << "\nAll tests passed!" << std::endl;
        return 0;
    } else {
        std::cout << "\nSome tests failed!" << std::endl;
        return 1;
    }
}

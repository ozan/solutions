#include <iostream>
#include <vector>
#include <cuda_runtime.h>

extern "C" void solve(const int *input, int *histogram, int N, int num_bins);

bool run_test(const std::vector<int>& input, int num_bins, const std::vector<int>& expected, const char* name) {
    int N = input.size();

    int *d_input, *d_histogram;
    cudaMalloc(&d_input, N * sizeof(int));
    cudaMalloc(&d_histogram, num_bins * sizeof(int));

    cudaMemcpy(d_input, input.data(), N * sizeof(int), cudaMemcpyHostToDevice);
    cudaMemset(d_histogram, 0, num_bins * sizeof(int));

    solve(d_input, d_histogram, N, num_bins);

    std::vector<int> h_histogram(num_bins);
    cudaMemcpy(h_histogram.data(), d_histogram, num_bins * sizeof(int), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        std::cout << name << ": CUDA error: " << cudaGetErrorString(error) << std::endl;
        cudaFree(d_input);
        cudaFree(d_histogram);
        return false;
    }

    bool success = (h_histogram == expected);
    if (!success) {
        std::cout << name << ": Error" << std::endl;
        std::cout << "  Got:      [";
        for (int i = 0; i < num_bins; i++) {
            std::cout << h_histogram[i] << (i < num_bins - 1 ? ", " : "");
        }
        std::cout << "]" << std::endl;
        std::cout << "  Expected: [";
        for (int i = 0; i < num_bins; i++) {
            std::cout << expected[i] << (i < num_bins - 1 ? ", " : "");
        }
        std::cout << "]" << std::endl;
    } else {
        std::cout << name << ": PASSED" << std::endl;
    }

    cudaFree(d_input);
    cudaFree(d_histogram);
    return success;
}

bool run_test_large(int N, int num_bins, const char* name) {
    std::cout << "Running " << name << " with N=" << N << ", num_bins=" << num_bins << "..." << std::endl;

    std::vector<int> h_input(N);
    std::vector<int> expected(num_bins, 0);

    // Generate input and compute expected histogram
    for (int i = 0; i < N; i++) {
        h_input[i] = i % num_bins;
        expected[h_input[i]]++;
    }

    int *d_input, *d_histogram;
    cudaMalloc(&d_input, N * sizeof(int));
    cudaMalloc(&d_histogram, num_bins * sizeof(int));

    cudaMemcpy(d_input, h_input.data(), N * sizeof(int), cudaMemcpyHostToDevice);
    cudaMemset(d_histogram, 0, num_bins * sizeof(int));

    solve(d_input, d_histogram, N, num_bins);

    std::vector<int> h_histogram(num_bins);
    cudaMemcpy(h_histogram.data(), d_histogram, num_bins * sizeof(int), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        std::cout << name << ": CUDA error: " << cudaGetErrorString(error) << std::endl;
        cudaFree(d_input);
        cudaFree(d_histogram);
        return false;
    }

    bool success = (h_histogram == expected);
    if (!success) {
        std::cout << name << ": Error - histogram mismatch" << std::endl;
        // Print first few mismatches
        int mismatches = 0;
        for (int i = 0; i < num_bins && mismatches < 5; i++) {
            if (h_histogram[i] != expected[i]) {
                std::cout << "  Bin " << i << ": got " << h_histogram[i] << ", expected " << expected[i] << std::endl;
                mismatches++;
            }
        }
    } else {
        std::cout << name << ": PASSED" << std::endl;
    }

    cudaFree(d_input);
    cudaFree(d_histogram);
    return success;
}

int main() {
    bool all_passed = true;

    // Example 1: [0, 1, 2, 1, 0], num_bins=3 -> [2, 2, 1]
    all_passed &= run_test(
        {0, 1, 2, 1, 0},
        3,
        {2, 2, 1},
        "Example 1"
    );

    // Example 2: [3, 3, 3, 3], num_bins=5 -> [0, 0, 0, 4, 0]
    all_passed &= run_test(
        {3, 3, 3, 3},
        5,
        {0, 0, 0, 4, 0},
        "Example 2"
    );

    // Test 3: Single element
    all_passed &= run_test(
        {0},
        1,
        {1},
        "Single element"
    );

    // Test 4: All same bin
    all_passed &= run_test(
        {5, 5, 5, 5, 5, 5, 5, 5, 5, 5},
        10,
        {0, 0, 0, 0, 0, 10, 0, 0, 0, 0},
        "All same bin"
    );

    // Test 5: Uniform distribution
    all_passed &= run_test(
        {0, 1, 2, 3, 4, 5, 6, 7},
        8,
        {1, 1, 1, 1, 1, 1, 1, 1},
        "Uniform distribution"
    );

    // Test 6: Large array with few bins
    all_passed &= run_test_large(1000000, 10, "Large array 1M, 10 bins");

    // Test 7: Large array with many bins
    all_passed &= run_test_large(1000000, 256, "Large array 1M, 256 bins");

    // Test 8: Large array with max bins
    all_passed &= run_test_large(1000000, 1024, "Large array 1M, 1024 bins");

    // Test 9: Very large array
    all_passed &= run_test_large(10000000, 100, "Large array 10M, 100 bins");

    if (all_passed) {
        std::cout << "\nSuccess! All histogramming tests passed." << std::endl;
    } else {
        std::cout << "\nSome tests failed!" << std::endl;
    }

    return all_passed ? 0 : 1;
}

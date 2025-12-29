#include <iostream>
#include <vector>
#include <cmath>
#include <cuda_runtime.h>

// Declaration of the solve function from dot_product.cu
extern "C" void solve(const float* A, const float* B, float* result, int N);

bool test_dot_product(int N, const char* test_name) {
    std::cout << "Running " << test_name << " with N=" << N << "..." << std::endl;

    // Allocate host memory
    std::vector<float> h_A(N);
    std::vector<float> h_B(N);
    float h_result = 0.0f;

    // Initialize data and compute expected result
    double expected = 0.0;
    for (int i = 0; i < N; i++) {
        h_A[i] = 1.0f + (float)(i % 10);
        h_B[i] = 2.0f + (float)(i % 7);
        expected += (double)h_A[i] * (double)h_B[i];
    }

    // Allocate device memory
    float *d_A, *d_B, *d_result;
    cudaMalloc(&d_A, N * sizeof(float));
    cudaMalloc(&d_B, N * sizeof(float));
    cudaMalloc(&d_result, sizeof(float));

    // Copy data: host -> device
    cudaMemcpy(d_A, h_A.data(), N * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, h_B.data(), N * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemset(d_result, 0, sizeof(float)); // Initialize result to 0

    // Run solution
    solve(d_A, d_B, d_result, N);

    // Copy result: device -> host
    cudaMemcpy(&h_result, d_result, sizeof(float), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        printf("CUDA error: %s\n", cudaGetErrorString(error));
        cudaFree(d_A);
        cudaFree(d_B);
        cudaFree(d_result);
        return false;
    }

    // Verify result with tolerance for floating point accumulation errors
    float tolerance = N * 1e-4f;
    bool success = std::abs(h_result - (float)expected) < tolerance;

    if (success) {
        std::cout << "  Success! Result=" << h_result << ", Expected=" << expected << std::endl;
    } else {
        std::cout << "  Error: Result=" << h_result << ", Expected=" << expected << std::endl;
    }

    // Cleanup
    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_result);

    return success;
}

int main() {
    bool all_passed = true;

    // Test 1: Small N (single block, 256 threads)
    all_passed &= test_dot_product(100, "test_single_block");

    // Test 2: N=1000 (multiple blocks: ceil(1000/256) = 4 blocks)
    all_passed &= test_dot_product(1000, "test_multiple_blocks");

    // Test 3: Larger N (many blocks, tests grid-stride loop)
    all_passed &= test_dot_product(100000, "test_large_array");

    if (all_passed) {
        std::cout << "\nAll tests passed!" << std::endl;
        return 0;
    } else {
        std::cout << "\nSome tests failed!" << std::endl;
        return 1;
    }
}

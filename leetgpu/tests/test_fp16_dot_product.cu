#include <iostream>
#include <vector>
#include <cmath>
#include <cuda_fp16.h>
#include <cuda_runtime.h>

// Declaration of the solve function from fp16_dot_product.cu
extern "C" void solve(const half* A, const half* B, half* result, int N);

bool test_fp16_dot_product(const std::vector<float>& h_A_float, const std::vector<float>& h_B_float,
                           float expected, const char* test_name) {
    int N = h_A_float.size();
    std::cout << "Running " << test_name << " with N=" << N << "..." << std::endl;

    // Convert float to half
    std::vector<half> h_A(N);
    std::vector<half> h_B(N);
    for (int i = 0; i < N; i++) {
        h_A[i] = __float2half(h_A_float[i]);
        h_B[i] = __float2half(h_B_float[i]);
    }

    // Allocate device memory
    half *d_A, *d_B, *d_result;
    cudaMalloc(&d_A, N * sizeof(half));
    cudaMalloc(&d_B, N * sizeof(half));
    cudaMalloc(&d_result, sizeof(half));

    // Copy data: host -> device
    cudaMemcpy(d_A, h_A.data(), N * sizeof(half), cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, h_B.data(), N * sizeof(half), cudaMemcpyHostToDevice);
    cudaMemset(d_result, 0, sizeof(half));

    // Run solution
    solve(d_A, d_B, d_result, N);

    // Copy result: device -> host
    half h_result_half;
    cudaMemcpy(&h_result_half, d_result, sizeof(half), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        printf("CUDA error: %s\n", cudaGetErrorString(error));
        cudaFree(d_A);
        cudaFree(d_B);
        cudaFree(d_result);
        return false;
    }

    float h_result = __half2float(h_result_half);

    // Verify result with tolerance (FP16 has lower precision)
    float tolerance = std::max(0.1f, std::abs(expected) * 0.01f);
    bool success = std::abs(h_result - expected) < tolerance;

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

bool test_fp16_dot_product_large(int N, const char* test_name) {
    std::cout << "Running " << test_name << " with N=" << N << "..." << std::endl;

    // Allocate host memory
    std::vector<half> h_A(N);
    std::vector<half> h_B(N);

    // Initialize data and compute expected result
    // Use small values to avoid FP16 overflow (max ~65504)
    // Scale factor ensures result stays in FP16 range
    float scale = (N > 100000) ? 0.01f : 0.1f;
    double expected = 0.0;
    for (int i = 0; i < N; i++) {
        float a = ((float)(i % 10) + 1.0f) * scale;
        float b = ((float)(i % 7) + 1.0f) * scale;
        h_A[i] = __float2half(a);
        h_B[i] = __float2half(b);
        expected += (double)a * (double)b;
    }

    // Allocate device memory
    half *d_A, *d_B, *d_result;
    cudaMalloc(&d_A, N * sizeof(half));
    cudaMalloc(&d_B, N * sizeof(half));
    cudaMalloc(&d_result, sizeof(half));

    // Copy data: host -> device
    cudaMemcpy(d_A, h_A.data(), N * sizeof(half), cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, h_B.data(), N * sizeof(half), cudaMemcpyHostToDevice);
    cudaMemset(d_result, 0, sizeof(half));

    // Run solution
    solve(d_A, d_B, d_result, N);

    // Copy result: device -> host
    half h_result_half;
    cudaMemcpy(&h_result_half, d_result, sizeof(half), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        printf("CUDA error: %s\n", cudaGetErrorString(error));
        cudaFree(d_A);
        cudaFree(d_B);
        cudaFree(d_result);
        return false;
    }

    float h_result = __half2float(h_result_half);

    // FP16 has limited precision (~3 decimal digits), use relative tolerance
    float tolerance = std::max(1.0f, std::abs((float)expected) * 0.05f);
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

    // Example 1: [1.0, 2.0, 3.0, 4.0] dot [5.0, 6.0, 7.0, 8.0] = 70.0
    all_passed &= test_fp16_dot_product(
        {1.0f, 2.0f, 3.0f, 4.0f},
        {5.0f, 6.0f, 7.0f, 8.0f},
        70.0f,
        "example_1"
    );

    // Example 2: [0.5, 1.5, 2.5] dot [2.0, 3.0, 4.0] = 15.5
    all_passed &= test_fp16_dot_product(
        {0.5f, 1.5f, 2.5f},
        {2.0f, 3.0f, 4.0f},
        15.5f,
        "example_2"
    );

    // Test 3: Single element
    all_passed &= test_fp16_dot_product(
        {3.0f},
        {4.0f},
        12.0f,
        "single_element"
    );

    // Test 4: Medium size (multiple blocks)
    all_passed &= test_fp16_dot_product_large(1000, "medium_array_1K");

    // Test 5: Large size
    all_passed &= test_fp16_dot_product_large(100000, "large_array_100K");

    // Test 6: Very large size
    all_passed &= test_fp16_dot_product_large(1000000, "large_array_1M");

    if (all_passed) {
        std::cout << "\nAll tests passed!" << std::endl;
        return 0;
    } else {
        std::cout << "\nSome tests failed!" << std::endl;
        return 1;
    }
}

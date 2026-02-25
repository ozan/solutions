#include <iostream>
#include <vector>
#include <cmath>
#include <cuda_runtime.h>

extern "C" void solve(const float* A, const float* B, float* output, int N);

bool run_test(const std::vector<float>& A, const std::vector<float>& B,
              const std::vector<float>& expected, const char* name) {
    int N = A.size();

    float *d_A, *d_B, *d_output;
    cudaMalloc(&d_A, N * sizeof(float));
    cudaMalloc(&d_B, N * sizeof(float));
    cudaMalloc(&d_output, 2 * N * sizeof(float));

    cudaMemcpy(d_A, A.data(), N * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, B.data(), N * sizeof(float), cudaMemcpyHostToDevice);

    solve(d_A, d_B, d_output, N);

    std::vector<float> result(2 * N);
    cudaMemcpy(result.data(), d_output, 2 * N * sizeof(float), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        std::cout << name << ": CUDA error: " << cudaGetErrorString(error) << std::endl;
        cudaFree(d_A);
        cudaFree(d_B);
        cudaFree(d_output);
        return false;
    }

    bool success = true;
    for (int i = 0; i < 2 * N; i++) {
        if (std::abs(result[i] - expected[i]) > 1e-5) {
            std::cout << name << ": Error at index " << i << ": got " << result[i]
                      << ", expected " << expected[i] << std::endl;
            success = false;
        }
    }

    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_output);

    if (success) std::cout << name << ": PASSED" << std::endl;
    return success;
}

int main() {
    bool all_passed = true;

    // Example 1: A = [1.0, 2.0, 3.0], B = [4.0, 5.0, 6.0] -> [1.0, 4.0, 2.0, 5.0, 3.0, 6.0]
    all_passed &= run_test(
        {1.0f, 2.0f, 3.0f},
        {4.0f, 5.0f, 6.0f},
        {1.0f, 4.0f, 2.0f, 5.0f, 3.0f, 6.0f},
        "Example 1"
    );

    // Example 2: A = [10.0, 20.0], B = [30.0, 40.0] -> [10.0, 30.0, 20.0, 40.0]
    all_passed &= run_test(
        {10.0f, 20.0f},
        {30.0f, 40.0f},
        {10.0f, 30.0f, 20.0f, 40.0f},
        "Example 2"
    );

    // Edge case: single element
    all_passed &= run_test(
        {5.0f},
        {9.0f},
        {5.0f, 9.0f},
        "Single element"
    );

    // Larger test
    {
        int N = 10000;
        std::vector<float> A(N), B(N), expected(2 * N);
        for (int i = 0; i < N; i++) {
            A[i] = static_cast<float>(i);
            B[i] = static_cast<float>(i + N);
            expected[2 * i] = A[i];
            expected[2 * i + 1] = B[i];
        }
        all_passed &= run_test(A, B, expected, "Large array (N=10000)");
    }

    // Stress test near max constraint
    {
        int N = 1000000;
        std::vector<float> A(N), B(N), expected(2 * N);
        for (int i = 0; i < N; i++) {
            A[i] = static_cast<float>(i % 1000);
            B[i] = static_cast<float>((i + 500) % 1000);
            expected[2 * i] = A[i];
            expected[2 * i + 1] = B[i];
        }
        all_passed &= run_test(A, B, expected, "Stress test (N=1000000)");
    }

    if (all_passed) {
        std::cout << "Success! All interleave_arrays tests passed." << std::endl;
    }

    return all_passed ? 0 : 1;
}

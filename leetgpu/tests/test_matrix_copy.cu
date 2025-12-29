#include <iostream>
#include <vector>
#include <cmath>
#include <cuda_runtime.h>

extern "C" void solve(const float* A, float* B, int N);

bool run_test(const std::vector<float>& A, int N, const char* name) {
    std::vector<float> h_B(N * N);

    float *d_A, *d_B;
    cudaMalloc(&d_A, N * N * sizeof(float));
    cudaMalloc(&d_B, N * N * sizeof(float));

    cudaMemcpy(d_A, A.data(), N * N * sizeof(float), cudaMemcpyHostToDevice);

    solve(d_A, d_B, N);

    cudaMemcpy(h_B.data(), d_B, N * N * sizeof(float), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        std::cout << name << ": CUDA error: " << cudaGetErrorString(error) << std::endl;
        cudaFree(d_A);
        cudaFree(d_B);
        return false;
    }

    bool success = true;
    for (int i = 0; i < N * N; i++) {
        if (std::abs(h_B[i] - A[i]) > 1e-5) {
            std::cout << name << ": Error at index " << i << ": got " << h_B[i]
                      << ", expected " << A[i] << std::endl;
            success = false;
        }
    }

    cudaFree(d_A);
    cudaFree(d_B);

    if (success) std::cout << name << ": PASSED" << std::endl;
    return success;
}

int main() {
    bool all_passed = true;

    // Example 1: 2x2 matrix
    all_passed &= run_test(
        {1.0f, 2.0f,
         3.0f, 4.0f},
        2,
        "Example 1"
    );

    // Example 2: 3x3 matrix
    all_passed &= run_test(
        {5.5f, 6.6f, 7.7f,
         8.8f, 9.9f, 10.1f,
         11.2f, 12.3f, 13.4f},
        3,
        "Example 2"
    );

    if (all_passed) {
        std::cout << "Success! All matrix_copy tests passed." << std::endl;
    }

    return all_passed ? 0 : 1;
}

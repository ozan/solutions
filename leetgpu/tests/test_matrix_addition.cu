#include <iostream>
#include <vector>
#include <cmath>
#include <cuda_runtime.h>

extern "C" void solve(const float* A, const float* B, float* C, int N);

bool run_test(const std::vector<float>& A, const std::vector<float>& B,
              const std::vector<float>& expected, int N, const char* name) {
    std::vector<float> h_C(N * N);

    float *d_A, *d_B, *d_C;
    cudaMalloc(&d_A, N * N * sizeof(float));
    cudaMalloc(&d_B, N * N * sizeof(float));
    cudaMalloc(&d_C, N * N * sizeof(float));

    cudaMemcpy(d_A, A.data(), N * N * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, B.data(), N * N * sizeof(float), cudaMemcpyHostToDevice);

    solve(d_A, d_B, d_C, N);

    cudaMemcpy(h_C.data(), d_C, N * N * sizeof(float), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        std::cout << name << ": CUDA error: " << cudaGetErrorString(error) << std::endl;
        cudaFree(d_A);
        cudaFree(d_B);
        cudaFree(d_C);
        return false;
    }

    bool success = true;
    for (int i = 0; i < N * N; i++) {
        if (std::abs(h_C[i] - expected[i]) > 1e-5) {
            std::cout << name << ": Error at index " << i << ": got " << h_C[i]
                      << ", expected " << expected[i] << std::endl;
            success = false;
        }
    }

    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);

    if (success) std::cout << name << ": PASSED" << std::endl;
    return success;
}

int main() {
    bool all_passed = true;

    // Example 1: 2x2 matrices
    all_passed &= run_test(
        {1.0f, 2.0f,
         3.0f, 4.0f},
        {5.0f, 6.0f,
         7.0f, 8.0f},
        {6.0f, 8.0f,
         10.0f, 12.0f},
        2,
        "Example 1"
    );

    // Example 2: 3x3 matrices
    all_passed &= run_test(
        {1.5f, 2.5f, 3.5f,
         4.5f, 5.5f, 6.5f,
         7.5f, 8.5f, 9.5f},
        {0.5f, 0.5f, 0.5f,
         0.5f, 0.5f, 0.5f,
         0.5f, 0.5f, 0.5f},
        {2.0f, 3.0f, 4.0f,
         5.0f, 6.0f, 7.0f,
         8.0f, 9.0f, 10.0f},
        3,
        "Example 2"
    );

    if (all_passed) {
        std::cout << "Success! All matrix_addition tests passed." << std::endl;
    }

    return all_passed ? 0 : 1;
}

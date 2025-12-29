#include <iostream>
#include <vector>
#include <cmath>
#include <cuda_runtime.h>

// Declaration of the solve function from matrix_multiplication.cu
// A is M x N, B is N x K, C is M x K
extern "C" void solve(const float* A, const float* B, float* C, int M, int N, int K);

bool test_small_matrix() {
    std::cout << "=== Test 1: Small matrix (2x3 * 3x4) ===" << std::endl;

    int M = 2;
    int N = 3;
    int K = 4;

    // A is 2x3
    std::vector<float> h_A = {1.0f, 2.0f, 3.0f,
                              4.0f, 5.0f, 6.0f};

    // B is 3x4
    std::vector<float> h_B = {1.0f, 2.0f, 3.0f, 4.0f,
                              5.0f, 6.0f, 7.0f, 8.0f,
                              9.0f, 10.0f, 11.0f, 12.0f};

    // C = A * B is 2x4
    // C[0][0] = 1*1 + 2*5 + 3*9 = 1 + 10 + 27 = 38
    // C[0][1] = 1*2 + 2*6 + 3*10 = 2 + 12 + 30 = 44
    // C[0][2] = 1*3 + 2*7 + 3*11 = 3 + 14 + 33 = 50
    // C[0][3] = 1*4 + 2*8 + 3*12 = 4 + 16 + 36 = 56
    // C[1][0] = 4*1 + 5*5 + 6*9 = 4 + 25 + 54 = 83
    // C[1][1] = 4*2 + 5*6 + 6*10 = 8 + 30 + 60 = 98
    // C[1][2] = 4*3 + 5*7 + 6*11 = 12 + 35 + 66 = 113
    // C[1][3] = 4*4 + 5*8 + 6*12 = 16 + 40 + 72 = 128
    std::vector<float> expected = {38.0f, 44.0f, 50.0f, 56.0f,
                                   83.0f, 98.0f, 113.0f, 128.0f};

    std::vector<float> h_C(M * K);

    float *d_A, *d_B, *d_C;
    cudaMalloc(&d_A, M * N * sizeof(float));
    cudaMalloc(&d_B, N * K * sizeof(float));
    cudaMalloc(&d_C, M * K * sizeof(float));

    cudaMemcpy(d_A, h_A.data(), M * N * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, h_B.data(), N * K * sizeof(float), cudaMemcpyHostToDevice);

    solve(d_A, d_B, d_C, M, N, K);

    cudaMemcpy(h_C.data(), d_C, M * K * sizeof(float), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        std::cout << "CUDA error: " << cudaGetErrorString(error) << std::endl;
        cudaFree(d_A);
        cudaFree(d_B);
        cudaFree(d_C);
        return false;
    }

    bool success = true;
    for (int i = 0; i < M * K; i++) {
        if (std::abs(h_C[i] - expected[i]) > 1e-5) {
            std::cout << "Error at index " << i << ": got " << h_C[i]
                      << ", expected " << expected[i] << std::endl;
            success = false;
        }
    }

    if (success) {
        std::cout << "Success!" << std::endl;
    }

    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);
    return success;
}

bool test_square_matrix() {
    std::cout << "\n=== Test 2: Square identity matrix (3x3) ===" << std::endl;

    int M = 3, N = 3, K = 3;

    // A is 3x3
    std::vector<float> h_A = {1.0f, 2.0f, 3.0f,
                              4.0f, 5.0f, 6.0f,
                              7.0f, 8.0f, 9.0f};

    // B is identity 3x3
    std::vector<float> h_B = {1.0f, 0.0f, 0.0f,
                              0.0f, 1.0f, 0.0f,
                              0.0f, 0.0f, 1.0f};

    // C = A * I = A
    std::vector<float> expected = h_A;

    std::vector<float> h_C(M * K);

    float *d_A, *d_B, *d_C;
    cudaMalloc(&d_A, M * N * sizeof(float));
    cudaMalloc(&d_B, N * K * sizeof(float));
    cudaMalloc(&d_C, M * K * sizeof(float));

    cudaMemcpy(d_A, h_A.data(), M * N * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, h_B.data(), N * K * sizeof(float), cudaMemcpyHostToDevice);

    solve(d_A, d_B, d_C, M, N, K);

    cudaMemcpy(h_C.data(), d_C, M * K * sizeof(float), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        std::cout << "CUDA error: " << cudaGetErrorString(error) << std::endl;
        cudaFree(d_A);
        cudaFree(d_B);
        cudaFree(d_C);
        return false;
    }

    bool success = true;
    for (int i = 0; i < M * K; i++) {
        if (std::abs(h_C[i] - expected[i]) > 1e-5) {
            std::cout << "Error at index " << i << ": got " << h_C[i]
                      << ", expected " << expected[i] << std::endl;
            success = false;
        }
    }

    if (success) {
        std::cout << "Success!" << std::endl;
    }

    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);
    return success;
}

bool test_large_matrix() {
    std::cout << "\n=== Test 3: Large matrix (1024x1024 * 1024x1024) ===" << std::endl;

    int M = 1024, N = 1024, K = 1024;
    size_t size_A = (size_t)M * N;
    size_t size_B = (size_t)N * K;
    size_t size_C = (size_t)M * K;

    std::vector<float> h_A(size_A);
    std::vector<float> h_B(size_B);
    std::vector<float> h_C(size_C);

    // Initialize with simple pattern
    for (size_t i = 0; i < size_A; i++) {
        h_A[i] = (float)(i % 10) * 0.1f;
    }
    for (size_t i = 0; i < size_B; i++) {
        h_B[i] = (float)(i % 10) * 0.1f;
    }

    float *d_A, *d_B, *d_C;
    cudaMalloc(&d_A, size_A * sizeof(float));
    cudaMalloc(&d_B, size_B * sizeof(float));
    cudaMalloc(&d_C, size_C * sizeof(float));

    cudaMemcpy(d_A, h_A.data(), size_A * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, h_B.data(), size_B * sizeof(float), cudaMemcpyHostToDevice);

    // Warm-up run
    solve(d_A, d_B, d_C, M, N, K);
    cudaDeviceSynchronize();

    // Timed runs using CUDA events
    cudaEvent_t start, stop;
    cudaEventCreate(&start);
    cudaEventCreate(&stop);

    const int NUM_RUNS = 10;

    cudaEventRecord(start);
    for (int i = 0; i < NUM_RUNS; i++) {
        solve(d_A, d_B, d_C, M, N, K);
    }
    cudaEventRecord(stop);
    cudaEventSynchronize(stop);

    float milliseconds = 0;
    cudaEventElapsedTime(&milliseconds, start, stop);
    float avg_ms = milliseconds / NUM_RUNS;

    // Calculate GFLOPS
    // Matrix multiplication: 2*M*N*K floating point operations (multiply and add)
    double flops = 2.0 * M * N * K;
    double gflops = (flops / 1e9) / (avg_ms / 1000.0);

    std::cout << "Average time: " << avg_ms << " ms" << std::endl;
    std::cout << "Performance: " << gflops << " GFLOPS" << std::endl;

    cudaEventDestroy(start);
    cudaEventDestroy(stop);

    cudaMemcpy(h_C.data(), d_C, size_C * sizeof(float), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        std::cout << "CUDA error: " << cudaGetErrorString(error) << std::endl;
        cudaFree(d_A);
        cudaFree(d_B);
        cudaFree(d_C);
        return false;
    }

    // Verify a few random elements against CPU computation
    bool success = true;
    int errors_shown = 0;
    for (int row = 0; row < M && errors_shown < 5; row += 256) {
        for (int col = 0; col < K && errors_shown < 5; col += 256) {
            float expected = 0.0f;
            for (int i = 0; i < N; i++) {
                expected += h_A[row * N + i] * h_B[i * K + col];
            }
            float actual = h_C[row * K + col];
            if (std::abs(actual - expected) > 1e-2) {  // Looser tolerance for large matrices
                std::cout << "Error at (" << row << "," << col << "): got " << actual
                          << ", expected " << expected << std::endl;
                success = false;
                errors_shown++;
            }
        }
    }

    if (success) {
        std::cout << "Success!" << std::endl;
    }

    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);
    return success;
}

int main() {
    bool all_passed = true;

    all_passed &= test_small_matrix();
    all_passed &= test_square_matrix();
    all_passed &= test_large_matrix();

    std::cout << "\n=== Summary ===" << std::endl;
    if (all_passed) {
        std::cout << "All tests passed!" << std::endl;
    } else {
        std::cout << "Some tests failed." << std::endl;
    }

    return all_passed ? 0 : 1;
}

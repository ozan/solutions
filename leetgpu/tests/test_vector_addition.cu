#include <iostream>
#include <vector>
#include <cmath>
#include <cuda_runtime.h>

// Declaration of the solve function from vector_addition.cu
extern "C" void solve(const float* A, const float* B, float* C, int N);

int main() {
    int N = 1 << 20; // 1 million elements
    size_t bytes = N * sizeof(float);
    std::cout << "Running vector_addition with N=" << N << " elements..." << std::endl;

    // Allocate host memory
    std::vector<float> h_A(N);
    std::vector<float> h_B(N);
    std::vector<float> h_C(N);

    // Initialize data
    for (int i = 0; i < N; i++) {
        h_A[i] = 1.0f * (float)i;
        h_B[i] = 2.0f * (float)i;
    }

    // Allocate device memory
    float *d_A, *d_B, *d_C;
    cudaMalloc(&d_A, bytes);
    cudaMalloc(&d_B, bytes);
    cudaMalloc(&d_C, bytes);

    // Copy data: host -> device
    cudaMemcpy(d_A, h_A.data(), bytes, cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, h_B.data(), bytes, cudaMemcpyHostToDevice);

    // Run solution
    solve(d_A, d_B, d_C, N);

    // Copy result: device -> host
    cudaMemcpy(h_C.data(), d_C, bytes, cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
	    printf("CUDA error: %s\n", cudaGetErrorString(error));
	    exit(-1);
    }

    // Verify results (expect 1.0 * i + 2.0 * i = 3.0 * i)
    bool success = true;
    for (int i = 0; i < N; i++) {
	float expected = 3.0f * (float)i;
        if (std::abs(h_C[i] - expected) > 1e-5) {
            std::cout << "Error at index " << i << ": " << h_C[i] << " != " << expected << std::endl;
            success = false;
            break;
        }
    }

    if (success) std::cout << "Success! All values computed correctly." << std::endl;

    // Cleanup
    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);

    return success ? 0 : 1;
}

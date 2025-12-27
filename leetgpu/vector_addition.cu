#include <iostream>
#include <vector>
#include <cuda_runtime.h>

// --- YOUR LEETGPU CODE STARTS HERE ---
__global__ void vector_add(const float* A, const float* B, float* C, int N) {
    int i = blockDim.x * blockIdx.x + threadIdx.x;
    if (i < N) C[i] = A[i] + B[i];
}

// A, B, C are device pointers (i.e. pointers to memory on the GPU)
extern "C" void solve(const float* A, const float* B, float* C, int N) {
    int threadsPerBlock = 256;
    int blocksPerGrid = (N + threadsPerBlock - 1) / threadsPerBlock;

    vector_add<<<blocksPerGrid, threadsPerBlock>>>(A, B, C, N);
    cudaDeviceSynchronize();
}
// --- YOUR LEETGPU CODE ENDS HERE ---

// --- HARNESS TO RUN LOCALLY ---
int main() {
    // 1. Setup Data Size
    int N = 1 << 20; // 1 million elements
    size_t bytes = N * sizeof(float);
    std::cout << "Running vector_add with N=" << N << " elements..." << std::endl;

    // 2. Allocate Host (CPU) Memory
    std::vector<float> h_A(N);
    std::vector<float> h_B(N);
    std::vector<float> h_C(N);

    // Initialize data
    for (int i = 0; i < N; i++) {
        h_A[i] = 1.0f;
        h_B[i] = 2.0f;
    }

    // 3. Allocate Device (GPU) Memory
    float *d_A, *d_B, *d_C;
    cudaMalloc(&d_A, bytes);
    cudaMalloc(&d_B, bytes);
    cudaMalloc(&d_C, bytes);

    // 4. Copy Data: Host -> Device
    cudaMemcpy(d_A, h_A.data(), bytes, cudaMemcpyHostToDevice);
    cudaMemcpy(d_B, h_B.data(), bytes, cudaMemcpyHostToDevice);

    // 5. Run Your Solution
    solve(d_A, d_B, d_C, N);

    // 6. Copy Result: Device -> Host
    cudaMemcpy(h_C.data(), d_C, bytes, cudaMemcpyDeviceToHost);

    // 7. Verify Results
    // We expect 1.0 + 2.0 = 3.0 for all elements
    bool success = true;
    for (int i = 0; i < N; i++) {
        if (abs(h_C[i] - 3.0f) > 1e-5) {
            std::cout << "Error at index " << i << ": " << h_C[i] << " != 3.0" << std::endl;
            success = false;
            break;
        }
    }

    if (success) std::cout << "Success! All values computed correctly." << std::endl;

    // 8. Cleanup
    cudaFree(d_A);
    cudaFree(d_B);
    cudaFree(d_C);

    return 0;
}
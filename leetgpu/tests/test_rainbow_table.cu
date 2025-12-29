#include <iostream>
#include <vector>
#include <cuda_runtime.h>

extern "C" void solve(const int* input, unsigned int* output, int N, int R);

bool run_test(const std::vector<int>& input, int R,
              const std::vector<unsigned int>& expected, const char* name) {
    int N = input.size();
    std::vector<unsigned int> h_output(N);

    int *d_input;
    unsigned int *d_output;
    cudaMalloc(&d_input, N * sizeof(int));
    cudaMalloc(&d_output, N * sizeof(unsigned int));

    cudaMemcpy(d_input, input.data(), N * sizeof(int), cudaMemcpyHostToDevice);

    solve(d_input, d_output, N, R);

    cudaMemcpy(h_output.data(), d_output, N * sizeof(unsigned int), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        std::cout << name << ": CUDA error: " << cudaGetErrorString(error) << std::endl;
        cudaFree(d_input);
        cudaFree(d_output);
        return false;
    }

    bool success = true;
    for (int i = 0; i < N; i++) {
        if (h_output[i] != expected[i]) {
            std::cout << name << ": Error at index " << i << ": got " << h_output[i]
                      << ", expected " << expected[i] << std::endl;
            success = false;
        }
    }

    cudaFree(d_input);
    cudaFree(d_output);

    if (success) std::cout << name << ": PASSED" << std::endl;
    return success;
}

int main() {
    bool all_passed = true;

    // Example 1: R=2
    all_passed &= run_test(
        {123, 456, 789},
        2,
        {1636807824, 1273011621, 2193987222},
        "Example 1"
    );

    // Example 2: R=3
    all_passed &= run_test(
        {0, 1, 2147483647},
        3,
        {96754810, 3571711400, 2006156166},
        "Example 2"
    );

    if (all_passed) {
        std::cout << "Success! All rainbow_table tests passed." << std::endl;
    }

    return all_passed ? 0 : 1;
}

#include <iostream>
#include <vector>
#include <cuda_runtime.h>

extern "C" void solve(const int* input, int* output, int N, int K);

bool run_test(const std::vector<int>& input, int K, int expected, const char* name) {
    int N = input.size();

    int *d_input, *d_output;
    cudaMalloc(&d_input, N * sizeof(int));
    cudaMalloc(&d_output, sizeof(int));

    cudaMemcpy(d_input, input.data(), N * sizeof(int), cudaMemcpyHostToDevice);
    cudaMemset(d_output, 0, sizeof(int));

    solve(d_input, d_output, N, K);

    int h_output = 0;
    cudaMemcpy(&h_output, d_output, sizeof(int), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        std::cout << name << ": CUDA error: " << cudaGetErrorString(error) << std::endl;
        cudaFree(d_input);
        cudaFree(d_output);
        return false;
    }

    bool success = (h_output == expected);
    if (!success) {
        std::cout << name << ": Error: got " << h_output << ", expected " << expected << std::endl;
    } else {
        std::cout << name << ": PASSED" << std::endl;
    }

    cudaFree(d_input);
    cudaFree(d_output);
    return success;
}

int main() {
    bool all_passed = true;

    // Example 1: [1, 2, 3, 4, 5, 1], k=1 -> count=2
    all_passed &= run_test(
        {1, 2, 3, 4, 5, 1},
        1,
        2,
        "Example 1"
    );

    // Example 2: [5, 10, 5, 2], k=1 -> count=0
    all_passed &= run_test(
        {5, 10, 5, 2},
        1,
        0,
        "Example 2"
    );

    if (all_passed) {
        std::cout << "Success! All count_array_element tests passed." << std::endl;
    }

    return all_passed ? 0 : 1;
}

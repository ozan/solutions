#include <iostream>
#include <vector>
#include <cuda_runtime.h>

extern "C" void solve(const int* input, int* output, int N, int M, int K);

bool run_test(const std::vector<int>& input, int N, int M, int K, int expected, const char* name) {
    int *d_input, *d_output;
    cudaMalloc(&d_input, N * M * sizeof(int));
    cudaMalloc(&d_output, sizeof(int));

    cudaMemcpy(d_input, input.data(), N * M * sizeof(int), cudaMemcpyHostToDevice);
    cudaMemset(d_output, 0, sizeof(int));

    solve(d_input, d_output, N, M, K);

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

    // Example 1: [1, 2, 3, 4, 1], k=1 -> count=2 (as 1x5 matrix, N=5 cols, M=1 row)
    all_passed &= run_test(
        {1, 2, 3, 4, 1},
        5, 1,
        1,
        2,
        "Example 1"
    );

    // Example 2: [5, 10, 5, 2], k=11 -> count=0 (as 2x2 matrix, N=2 cols, M=2 rows)
    all_passed &= run_test(
        {5, 10, 5, 2},
        2, 2,
        11,
        0,
        "Example 2"
    );

    if (all_passed) {
        std::cout << "Success! All count_2d_array_element tests passed." << std::endl;
    }

    return all_passed ? 0 : 1;
}

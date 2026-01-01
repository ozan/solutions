#include <iostream>
#include <vector>
#include <cuda_runtime.h>

extern "C" void solve(const int* input, int* output, int N, int M, int K, int P);

bool run_test(const std::vector<int>& input, int N, int M, int K, int P, int expected, const char* name) {
    int *d_input, *d_output;
    cudaMalloc(&d_input, N * M * K * sizeof(int));
    cudaMalloc(&d_output, sizeof(int));

    cudaMemcpy(d_input, input.data(), N * M * K * sizeof(int), cudaMemcpyHostToDevice);
    cudaMemset(d_output, 0, sizeof(int));

    solve(d_input, d_output, N, M, K, P);

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

    // Example 1: [[[1, 2, 3], [4, 5, 1]], [[1, 1, 1], [2, 2, 2]]]
    // N=2, M=2, K=3, P=1 -> count=5
    all_passed &= run_test(
        {1, 2, 3, 4, 5, 1, 1, 1, 1, 2, 2, 2},
        2, 2, 3,
        1,
        5,
        "Example 1"
    );

    // Example 2: [[[5, 10], [5, 2], [2, 2]]]
    // N=1, M=3, K=2, P=1 -> count=0
    all_passed &= run_test(
        {5, 10, 5, 2, 2, 2},
        1, 3, 2,
        1,
        0,
        "Example 2"
    );

    // Additional test: all same values
    // [[[3, 3], [3, 3]]], N=1, M=2, K=2, P=3 -> count=4
    all_passed &= run_test(
        {3, 3, 3, 3},
        1, 2, 2,
        3,
        4,
        "All same values"
    );

    // Additional test: value not present
    // [[[1, 2], [3, 4]]], N=1, M=2, K=2, P=99 -> count=0
    all_passed &= run_test(
        {1, 2, 3, 4},
        1, 2, 2,
        99,
        0,
        "Value not present"
    );

    // Large test: 128x128x128 = 2,097,152 elements (multiple blocks in each dimension)
    // Fill with pattern: every 7th element is the target value (42)
    {
        const int N = 128, M = 128, K = 128;
        const int total = N * M * K;
        const int P = 42;
        std::vector<int> large_input(total);
        int expected_count = 0;
        for (int i = 0; i < total; i++) {
            if (i % 7 == 0) {
                large_input[i] = P;
                expected_count++;
            } else {
                int val = (i % 41) + 1;  // Values 1-41, avoiding P=42
                large_input[i] = val;
            }
        }
        all_passed &= run_test(large_input, N, M, K, P, expected_count, "Large 128x128x128");
    }

    // Very large test: 256x256x256 = 16,777,216 elements
    // Every element at position where (i+j+k) % 11 == 0 is target
    {
        const int N = 256, M = 256, K = 256;
        const int total = N * M * K;
        const int P = 77;
        std::vector<int> large_input(total);
        int expected_count = 0;
        for (int n = 0; n < N; n++) {
            for (int m = 0; m < M; m++) {
                for (int k = 0; k < K; k++) {
                    int idx = n * M * K + m * K + k;
                    if ((n + m + k) % 11 == 0) {
                        large_input[idx] = P;
                        expected_count++;
                    } else {
                        large_input[idx] = (idx % 76) + 1;  // Values 1-76, avoiding P
                    }
                }
            }
        }
        all_passed &= run_test(large_input, N, M, K, P, expected_count, "Large 256x256x256");
    }

    if (all_passed) {
        std::cout << "Success! All count_3d_array_element tests passed." << std::endl;
    }

    return all_passed ? 0 : 1;
}

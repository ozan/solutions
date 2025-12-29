#include <iostream>
#include <vector>
#include <cmath>
#include <cuda_runtime.h>

// Declaration of the solve function from matrix_transpose.cu
extern "C" void solve(const float* input, float* output, int rows, int cols);

bool test_small_matrix() {
    std::cout << "=== Test 1: Small matrix (2x3) ===" << std::endl;

    int rows = 2;
    int cols = 3;

    std::vector<float> h_input = {1.0f, 2.0f, 3.0f,
                                  4.0f, 5.0f, 6.0f};

    std::vector<float> expected = {1.0f, 4.0f,
                                   2.0f, 5.0f,
                                   3.0f, 6.0f};

    std::vector<float> h_output(rows * cols);

    float *d_input, *d_output;
    cudaMalloc(&d_input, rows * cols * sizeof(float));
    cudaMalloc(&d_output, rows * cols * sizeof(float));

    cudaMemcpy(d_input, h_input.data(), rows * cols * sizeof(float), cudaMemcpyHostToDevice);

    solve(d_input, d_output, rows, cols);

    cudaMemcpy(h_output.data(), d_output, rows * cols * sizeof(float), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        std::cout << "CUDA error: " << cudaGetErrorString(error) << std::endl;
        cudaFree(d_input);
        cudaFree(d_output);
        return false;
    }

    bool success = true;
    for (int i = 0; i < rows * cols; i++) {
        if (std::abs(h_output[i] - expected[i]) > 1e-5) {
            std::cout << "Error at index " << i << ": got " << h_output[i]
                      << ", expected " << expected[i] << std::endl;
            success = false;
        }
    }

    if (success) {
        std::cout << "Success!" << std::endl;
    }

    cudaFree(d_input);
    cudaFree(d_output);
    return success;
}

bool test_large_matrix() {
    std::cout << "\n=== Test 2: Large matrix (2048x4096) ===" << std::endl;

    int rows = 2048;
    int cols = 4096;
    size_t size = (size_t)rows * cols;

    std::vector<float> h_input(size);
    std::vector<float> h_output(size);

    // Initialize with recognizable pattern: value = row * 10000 + col
    for (int r = 0; r < rows; r++) {
        for (int c = 0; c < cols; c++) {
            h_input[r * cols + c] = (float)(r * 10000 + c);
        }
    }

    float *d_input, *d_output;
    cudaMalloc(&d_input, size * sizeof(float));
    cudaMalloc(&d_output, size * sizeof(float));

    cudaMemcpy(d_input, h_input.data(), size * sizeof(float), cudaMemcpyHostToDevice);

    // Warm-up run
    solve(d_input, d_output, rows, cols);
    cudaDeviceSynchronize();

    // Timed runs using CUDA events
    cudaEvent_t start, stop;
    cudaEventCreate(&start);
    cudaEventCreate(&stop);

    const int NUM_RUNS = 10;

    cudaEventRecord(start);
    for (int i = 0; i < NUM_RUNS; i++) {
        solve(d_input, d_output, rows, cols);
    }
    cudaEventRecord(stop);
    cudaEventSynchronize(stop);

    float milliseconds = 0;
    cudaEventElapsedTime(&milliseconds, start, stop);
    float avg_ms = milliseconds / NUM_RUNS;

    // Calculate effective bandwidth
    // Transpose reads and writes each element once
    size_t bytes = 2 * size * sizeof(float);
    float bandwidth_gb_s = (bytes / 1e9) / (avg_ms / 1000.0f);

    std::cout << "Average time: " << avg_ms << " ms" << std::endl;
    std::cout << "Effective bandwidth: " << bandwidth_gb_s << " GB/s" << std::endl;

    cudaEventDestroy(start);
    cudaEventDestroy(stop);

    cudaMemcpy(h_output.data(), d_output, size * sizeof(float), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        std::cout << "CUDA error: " << cudaGetErrorString(error) << std::endl;
        cudaFree(d_input);
        cudaFree(d_output);
        return false;
    }

    // Verify: output[c][r] should equal input[r][c]
    // output is cols x rows, so output[c * rows + r] = input[r * cols + c]
    bool success = true;
    int errors_shown = 0;
    for (int r = 0; r < rows && errors_shown < 5; r++) {
        for (int c = 0; c < cols && errors_shown < 5; c++) {
            float expected = h_input[r * cols + c];
            float actual = h_output[c * rows + r];
            if (std::abs(actual - expected) > 1e-5) {
                std::cout << "Error at (" << r << "," << c << "): got " << actual
                          << ", expected " << expected << std::endl;
                success = false;
                errors_shown++;
            }
        }
    }

    if (success) {
        std::cout << "Success!" << std::endl;
    }

    cudaFree(d_input);
    cudaFree(d_output);
    return success;
}

int main() {
    bool all_passed = true;

    all_passed &= test_small_matrix();
    all_passed &= test_large_matrix();

    std::cout << "\n=== Summary ===" << std::endl;
    if (all_passed) {
        std::cout << "All tests passed!" << std::endl;
    } else {
        std::cout << "Some tests failed." << std::endl;
    }

    return all_passed ? 0 : 1;
}

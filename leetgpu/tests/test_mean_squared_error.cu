#include <iostream>
#include <vector>
#include <cmath>
#include <cuda_runtime.h>

// Declaration of the solve function from mean_squared_error.cu
extern "C" void solve(const float* predictions, const float* targets, float* mse, int N);

bool test_mse_fixed(const std::vector<float>& predictions, const std::vector<float>& targets,
                    float expected_mse, const char* test_name) {
    int N = predictions.size();
    std::cout << "Running " << test_name << " with N=" << N << "..." << std::endl;

    float h_mse = 0.0f;

    // Allocate device memory
    float *d_predictions, *d_targets, *d_mse;
    cudaMalloc(&d_predictions, N * sizeof(float));
    cudaMalloc(&d_targets, N * sizeof(float));
    cudaMalloc(&d_mse, sizeof(float));

    // Copy data: host -> device
    cudaMemcpy(d_predictions, predictions.data(), N * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(d_targets, targets.data(), N * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemset(d_mse, 0, sizeof(float));

    // Run solution
    solve(d_predictions, d_targets, d_mse, N);

    // Copy result: device -> host
    cudaMemcpy(&h_mse, d_mse, sizeof(float), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        printf("CUDA error: %s\n", cudaGetErrorString(error));
        cudaFree(d_predictions);
        cudaFree(d_targets);
        cudaFree(d_mse);
        return false;
    }

    // Verify result with tolerance
    float tolerance = 0.01f;
    bool success = std::abs(h_mse - expected_mse) < tolerance;

    if (success) {
        std::cout << "  Success! MSE=" << h_mse << ", Expected=" << expected_mse << std::endl;
    } else {
        std::cout << "  Error: MSE=" << h_mse << ", Expected=" << expected_mse << std::endl;
    }

    // Cleanup
    cudaFree(d_predictions);
    cudaFree(d_targets);
    cudaFree(d_mse);

    return success;
}

bool test_mse_generated(int N, const char* test_name) {
    std::cout << "Running " << test_name << " with N=" << N << "..." << std::endl;

    // Allocate host memory
    std::vector<float> h_predictions(N);
    std::vector<float> h_targets(N);
    float h_mse = 0.0f;

    // Initialize data and compute expected result
    double sum_squared_error = 0.0;
    for (int i = 0; i < N; i++) {
        h_predictions[i] = (float)((i % 1000) - 500) + 0.5f;
        h_targets[i] = (float)((i % 1000) - 500);
        double diff = (double)h_predictions[i] - (double)h_targets[i];
        sum_squared_error += diff * diff;
    }
    double expected_mse = sum_squared_error / N;

    // Allocate device memory
    float *d_predictions, *d_targets, *d_mse;
    cudaMalloc(&d_predictions, N * sizeof(float));
    cudaMalloc(&d_targets, N * sizeof(float));
    cudaMalloc(&d_mse, sizeof(float));

    // Copy data: host -> device
    cudaMemcpy(d_predictions, h_predictions.data(), N * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(d_targets, h_targets.data(), N * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemset(d_mse, 0, sizeof(float));

    // Run solution
    solve(d_predictions, d_targets, d_mse, N);

    // Copy result: device -> host
    cudaMemcpy(&h_mse, d_mse, sizeof(float), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        printf("CUDA error: %s\n", cudaGetErrorString(error));
        cudaFree(d_predictions);
        cudaFree(d_targets);
        cudaFree(d_mse);
        return false;
    }

    // Verify result with tolerance for floating point accumulation errors
    float tolerance = std::max(0.01f, (float)(expected_mse * 1e-4));
    bool success = std::abs(h_mse - (float)expected_mse) < tolerance;

    if (success) {
        std::cout << "  Success! MSE=" << h_mse << ", Expected=" << expected_mse << std::endl;
    } else {
        std::cout << "  Error: MSE=" << h_mse << ", Expected=" << expected_mse << std::endl;
    }

    // Cleanup
    cudaFree(d_predictions);
    cudaFree(d_targets);
    cudaFree(d_mse);

    return success;
}

int main() {
    bool all_passed = true;

    // Test 1: Example 1 from problem statement
    // predictions = [1.0, 2.0, 3.0, 4.0], targets = [1.5, 2.5, 3.5, 4.5]
    // MSE = ((0.5)^2 + (0.5)^2 + (0.5)^2 + (0.5)^2) / 4 = 1.0 / 4 = 0.25
    all_passed &= test_mse_fixed(
        {1.0f, 2.0f, 3.0f, 4.0f},
        {1.5f, 2.5f, 3.5f, 4.5f},
        0.25f,
        "test_example_1"
    );

    // Test 2: Example 2 from problem statement
    // predictions = [10.0, 20.0, 30.0], targets = [12.0, 18.0, 33.0]
    // MSE = ((−2)^2 + (2)^2 + (−3)^2) / 3 = (4 + 4 + 9) / 3 = 17 / 3 ≈ 5.67
    all_passed &= test_mse_fixed(
        {10.0f, 20.0f, 30.0f},
        {12.0f, 18.0f, 33.0f},
        5.67f,
        "test_example_2"
    );

    // Test 3: Small N (single block)
    all_passed &= test_mse_generated(100, "test_single_block");

    // Test 4: Medium N (multiple blocks)
    all_passed &= test_mse_generated(10000, "test_multiple_blocks");

    // Test 5: Large N (many blocks, tests grid-stride loop)
    all_passed &= test_mse_generated(1000000, "test_large_array");

    // Test 6: Very large N (stress test near upper constraint)
    all_passed &= test_mse_generated(100000000, "test_very_large_array");

    if (all_passed) {
        std::cout << "\nAll tests passed!" << std::endl;
        return 0;
    } else {
        std::cout << "\nSome tests failed!" << std::endl;
        return 1;
    }
}

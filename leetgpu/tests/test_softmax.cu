#include <iostream>
#include <vector>
#include <cmath>
#include <cuda_runtime.h>

// Declaration of the solve function from softmax.cu
extern "C" void solve(const float* input, float* output, int N);

// Compute softmax on CPU for reference
std::vector<double> cpu_softmax(const std::vector<float>& input) {
    int N = input.size();
    std::vector<double> result(N);

    // Find max for numerical stability
    double max_val = input[0];
    for (int i = 1; i < N; i++) {
        if (input[i] > max_val) max_val = input[i];
    }

    // Compute exp(x - max) and sum
    double sum = 0.0;
    for (int i = 0; i < N; i++) {
        result[i] = std::exp((double)input[i] - max_val);
        sum += result[i];
    }

    // Normalize
    for (int i = 0; i < N; i++) {
        result[i] /= sum;
    }

    return result;
}

bool test_softmax(const std::vector<float>& h_input, const std::vector<float>& expected, const char* test_name, float tolerance = 1e-3f) {
    int N = h_input.size();
    std::cout << "Running " << test_name << " with N=" << N << "..." << std::endl;

    std::vector<float> h_output(N);

    // Allocate device memory
    float *d_input, *d_output;
    cudaMalloc(&d_input, N * sizeof(float));
    cudaMalloc(&d_output, N * sizeof(float));

    // Copy data: host -> device
    cudaMemcpy(d_input, h_input.data(), N * sizeof(float), cudaMemcpyHostToDevice);

    // Run solution
    solve(d_input, d_output, N);

    // Copy result: device -> host
    cudaMemcpy(h_output.data(), d_output, N * sizeof(float), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        printf("CUDA error: %s\n", cudaGetErrorString(error));
        cudaFree(d_input);
        cudaFree(d_output);
        return false;
    }

    // Verify results
    bool success = true;
    for (int i = 0; i < N; i++) {
        float rel_tol = std::max(tolerance, std::abs(expected[i]) * tolerance);
        if (std::abs(h_output[i] - expected[i]) > rel_tol) {
            std::cout << "  Mismatch at index " << i << ": got " << h_output[i]
                      << ", expected " << expected[i] << std::endl;
            success = false;
        }
    }

    // Check that output sums to ~1.0
    float sum = 0.0f;
    for (int i = 0; i < N; i++) {
        sum += h_output[i];
    }
    if (std::abs(sum - 1.0f) > 1e-3f) {
        std::cout << "  Error: Output sum=" << sum << ", expected ~1.0" << std::endl;
        success = false;
    }

    if (success) {
        std::cout << "  Success! Output sums to " << sum << std::endl;
    }

    // Cleanup
    cudaFree(d_input);
    cudaFree(d_output);

    return success;
}

bool test_softmax_large(int N, const char* test_name) {
    std::cout << "Running " << test_name << " with N=" << N << "..." << std::endl;

    // Allocate host memory
    std::vector<float> h_input(N);
    std::vector<float> h_output(N);

    // Initialize data with random-ish values
    for (int i = 0; i < N; i++) {
        h_input[i] = ((float)(i % 100) - 50.0f) * 0.1f;  // Values in [-5.0, 4.9]
    }

    // Compute expected result on CPU
    std::vector<double> expected = cpu_softmax(h_input);

    // Allocate device memory
    float *d_input, *d_output;
    cudaMalloc(&d_input, N * sizeof(float));
    cudaMalloc(&d_output, N * sizeof(float));

    // Copy data: host -> device
    cudaMemcpy(d_input, h_input.data(), N * sizeof(float), cudaMemcpyHostToDevice);

    // Run solution
    solve(d_input, d_output, N);

    // Copy result: device -> host
    cudaMemcpy(h_output.data(), d_output, N * sizeof(float), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        printf("CUDA error: %s\n", cudaGetErrorString(error));
        cudaFree(d_input);
        cudaFree(d_output);
        return false;
    }

    // Verify results with tolerance
    bool success = true;
    float tolerance = 1e-5f;
    int mismatches = 0;
    for (int i = 0; i < N; i++) {
        float rel_tol = std::max(tolerance, (float)expected[i] * 0.01f);
        if (std::abs(h_output[i] - (float)expected[i]) > rel_tol) {
            if (mismatches < 5) {
                std::cout << "  Mismatch at index " << i << ": got " << h_output[i]
                          << ", expected " << expected[i] << std::endl;
            }
            mismatches++;
            success = false;
        }
    }
    if (mismatches > 5) {
        std::cout << "  ... and " << (mismatches - 5) << " more mismatches" << std::endl;
    }

    // Check that output sums to ~1.0
    double sum = 0.0;
    for (int i = 0; i < N; i++) {
        sum += h_output[i];
    }
    if (std::abs(sum - 1.0) > 1e-3) {
        std::cout << "  Error: Output sum=" << sum << ", expected ~1.0" << std::endl;
        success = false;
    }

    if (success) {
        std::cout << "  Success! Output sums to " << sum << std::endl;
    }

    // Cleanup
    cudaFree(d_input);
    cudaFree(d_output);

    return success;
}

int main() {
    bool all_passed = true;

    // Example 1: [1.0, 2.0, 3.0] -> [0.0900, 0.2447, 0.6652]
    all_passed &= test_softmax(
        {1.0f, 2.0f, 3.0f},
        {0.0900306f, 0.244728f, 0.665241f},
        "example_1"
    );

    // Example 2: [-10.0, -5.0, 0.0, 5.0, 10.0]
    // Correct softmax values (sum to 1.0):
    // exp(-10)/sum, exp(-5)/sum, exp(0)/sum, exp(5)/sum, exp(10)/sum
    // where sum = exp(-10) + exp(-5) + exp(0) + exp(5) + exp(10)
    all_passed &= test_softmax(
        {-10.0f, -5.0f, 0.0f, 5.0f, 10.0f},
        {2.0473e-9f, 3.0386e-7f, 4.5094e-5f, 6.6925e-3f, 0.99326f},
        "example_2"
    );

    // Test 3: Single element
    all_passed &= test_softmax(
        {5.0f},
        {1.0f},
        "single_element"
    );

    // Test 4: Two elements
    all_passed &= test_softmax(
        {0.0f, 0.0f},
        {0.5f, 0.5f},
        "equal_elements"
    );

    // Test 5: Large values (numerical stability test)
    all_passed &= test_softmax(
        {1000.0f, 1001.0f, 1002.0f},
        {0.0900306f, 0.244728f, 0.665241f},
        "large_values"
    );

    // Test 6: Negative values
    all_passed &= test_softmax(
        {-1.0f, -2.0f, -3.0f},
        {0.665241f, 0.244728f, 0.0900306f},
        "negative_values"
    );

    // Test 7: Medium-sized array
    all_passed &= test_softmax_large(1000, "medium_array_1K");

    // Test 8: Large array
    all_passed &= test_softmax_large(100000, "large_array_100K");

    // Test 9: Very large array (near constraint limit)
    all_passed &= test_softmax_large(500000, "large_array_500K");

    if (all_passed) {
        std::cout << "\nAll tests passed!" << std::endl;
        return 0;
    } else {
        std::cout << "\nSome tests failed!" << std::endl;
        return 1;
    }
}

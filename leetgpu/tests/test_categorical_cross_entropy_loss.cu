#include <iostream>
#include <vector>
#include <cmath>
#include <cuda_runtime.h>

// Declaration of the solve function from categorical_cross_entropy_loss.cu
extern "C" void solve(const float* logits, const int* true_labels, float* loss, int N, int C);

bool test_cce_fixed(const std::vector<float>& logits, const std::vector<int>& true_labels,
                    int N, int C, float expected_loss, const char* test_name) {
    std::cout << "Running " << test_name << " with N=" << N << ", C=" << C << "..." << std::endl;

    float h_loss = 0.0f;

    // Allocate device memory
    float *d_logits, *d_loss;
    int *d_true_labels;
    cudaMalloc(&d_logits, N * C * sizeof(float));
    cudaMalloc(&d_true_labels, N * sizeof(int));
    cudaMalloc(&d_loss, sizeof(float));

    // Copy data: host -> device
    cudaMemcpy(d_logits, logits.data(), N * C * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(d_true_labels, true_labels.data(), N * sizeof(int), cudaMemcpyHostToDevice);
    cudaMemset(d_loss, 0, sizeof(float));

    // Run solution
    solve(d_logits, d_true_labels, d_loss, N, C);

    // Copy result: device -> host
    cudaMemcpy(&h_loss, d_loss, sizeof(float), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        printf("CUDA error: %s\n", cudaGetErrorString(error));
        cudaFree(d_logits);
        cudaFree(d_true_labels);
        cudaFree(d_loss);
        return false;
    }

    // Verify result with tolerance
    float tolerance = 0.0001f;
    bool success = std::abs(h_loss - expected_loss) < tolerance;

    if (success) {
        std::cout << "  Success! Loss=" << h_loss << ", Expected=" << expected_loss << std::endl;
    } else {
        std::cout << "  Error: Loss=" << h_loss << ", Expected=" << expected_loss << std::endl;
    }

    // Cleanup
    cudaFree(d_logits);
    cudaFree(d_true_labels);
    cudaFree(d_loss);

    return success;
}

// Compute softmax cross entropy loss on CPU for verification
double compute_expected_cce(const std::vector<float>& logits, const std::vector<int>& true_labels, int N, int C) {
    double total_loss = 0.0;
    for (int i = 0; i < N; i++) {
        // Find max logit for numerical stability
        double max_logit = logits[i * C];
        for (int j = 1; j < C; j++) {
            max_logit = std::max(max_logit, (double)logits[i * C + j]);
        }

        // Compute log-sum-exp
        double sum_exp = 0.0;
        for (int j = 0; j < C; j++) {
            sum_exp += std::exp(logits[i * C + j] - max_logit);
        }
        double log_sum_exp = max_logit + std::log(sum_exp);

        // Cross entropy for this sample: -log(softmax[true_label])
        double loss_i = log_sum_exp - logits[i * C + true_labels[i]];
        total_loss += loss_i;
    }
    return total_loss / N;
}

bool test_cce_generated(int N, int C, const char* test_name) {
    std::cout << "Running " << test_name << " with N=" << N << ", C=" << C << "..." << std::endl;

    // Allocate host memory
    std::vector<float> h_logits(N * C);
    std::vector<int> h_true_labels(N);
    float h_loss = 0.0f;

    // Initialize data
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < C; j++) {
            // Generate logits in range [-10, 10]
            h_logits[i * C + j] = ((float)((i * C + j) % 2001) - 1000) / 100.0f;
        }
        h_true_labels[i] = i % C;
    }

    // Compute expected result on CPU
    double expected_loss = compute_expected_cce(h_logits, h_true_labels, N, C);

    // Allocate device memory
    float *d_logits, *d_loss;
    int *d_true_labels;
    cudaMalloc(&d_logits, N * C * sizeof(float));
    cudaMalloc(&d_true_labels, N * sizeof(int));
    cudaMalloc(&d_loss, sizeof(float));

    // Copy data: host -> device
    cudaMemcpy(d_logits, h_logits.data(), N * C * sizeof(float), cudaMemcpyHostToDevice);
    cudaMemcpy(d_true_labels, h_true_labels.data(), N * sizeof(int), cudaMemcpyHostToDevice);
    cudaMemset(d_loss, 0, sizeof(float));

    // Run solution
    solve(d_logits, d_true_labels, d_loss, N, C);

    // Copy result: device -> host
    cudaMemcpy(&h_loss, d_loss, sizeof(float), cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        printf("CUDA error: %s\n", cudaGetErrorString(error));
        cudaFree(d_logits);
        cudaFree(d_true_labels);
        cudaFree(d_loss);
        return false;
    }

    // Verify result with tolerance for floating point accumulation errors
    float tolerance = std::max(0.001f, (float)(expected_loss * 1e-3));
    bool success = std::abs(h_loss - (float)expected_loss) < tolerance;

    if (success) {
        std::cout << "  Success! Loss=" << h_loss << ", Expected=" << expected_loss << std::endl;
    } else {
        std::cout << "  Error: Loss=" << h_loss << ", Expected=" << expected_loss << std::endl;
    }

    // Cleanup
    cudaFree(d_logits);
    cudaFree(d_true_labels);
    cudaFree(d_loss);

    return success;
}

int main() {
    bool all_passed = true;

    // Test 1: Example 1 from problem statement
    // N = 2, C = 3
    // logits = [[1.0, 2.0, 0.5], [0.1, 3.0, 1.5]]
    // true_labels = [1, 1]
    // loss = 0.3548926
    all_passed &= test_cce_fixed(
        {1.0f, 2.0f, 0.5f, 0.1f, 3.0f, 1.5f},
        {1, 1},
        2, 3,
        0.3548926f,
        "test_example_1"
    );

    // Test 2: Example 2 from problem statement
    // N = 3, C = 4
    // logits = [[-0.5, 1.5, 0.0, 1.0], [2.0, -1.0, 0.5, 0.5], [0.0, 0.0, 0.0, 0.0]]
    // true_labels = [3, 0, 1]
    // loss = 0.98820376
    all_passed &= test_cce_fixed(
        {-0.5f, 1.5f, 0.0f, 1.0f, 2.0f, -1.0f, 0.5f, 0.5f, 0.0f, 0.0f, 0.0f, 0.0f},
        {3, 0, 1},
        3, 4,
        0.98820376f,
        "test_example_2"
    );

    // Test 3: Small N, small C
    all_passed &= test_cce_generated(100, 10, "test_small");

    // Test 4: Medium N, medium C
    all_passed &= test_cce_generated(1000, 100, "test_medium");

    // Test 5: Large N, small C
    all_passed &= test_cce_generated(10000, 10, "test_large_n_small_c");

    // Test 6: Medium N, large C
    all_passed &= test_cce_generated(1000, 1000, "test_medium_n_large_c");

    // Test 7: Stress test near upper constraints
    all_passed &= test_cce_generated(10000, 1000, "test_stress");

    if (all_passed) {
        std::cout << "\nAll tests passed!" << std::endl;
        return 0;
    } else {
        std::cout << "\nSome tests failed!" << std::endl;
        return 1;
    }
}

#include <iostream>
#include <vector>
#include <cmath>
#include <cuda_runtime.h>

// Declaration of the solve function from twod_max_pooling.cu
extern "C" void solve(const float* input, float* output, int N, int C, int H, int W, int kernel_size, int stride, int padding);

bool test_max_pooling(const std::vector<float>& h_input,
                      const std::vector<float>& expected,
                      int N, int C, int H, int W, int kernel_size, int stride, int padding,
                      const char* test_name) {
    // Output dimensions with stride and padding
    int out_H = (H + 2 * padding - kernel_size) / stride + 1;
    int out_W = (W + 2 * padding - kernel_size) / stride + 1;
    int in_size = N * C * H * W;
    int out_size = N * C * out_H * out_W;

    std::cout << "Running " << test_name << " (N=" << N << ", C=" << C
              << ", " << H << "x" << W << ", kernel=" << kernel_size
              << ", stride=" << stride << ", pad=" << padding
              << " -> " << out_H << "x" << out_W << ")..." << std::endl;

    std::vector<float> h_output(out_size);

    // Allocate device memory
    float *d_input, *d_output;
    cudaMalloc(&d_input, in_size * sizeof(float));
    cudaMalloc(&d_output, out_size * sizeof(float));

    // Copy input: host -> device
    cudaMemcpy(d_input, h_input.data(), in_size * sizeof(float), cudaMemcpyHostToDevice);

    // Run solution
    solve(d_input, d_output, N, C, H, W, kernel_size, stride, padding);

    // Copy result: device -> host
    cudaMemcpy(h_output.data(), d_output, out_size * sizeof(float), cudaMemcpyDeviceToHost);

    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        std::cout << "  CUDA error: " << cudaGetErrorString(error) << std::endl;
        cudaFree(d_input);
        cudaFree(d_output);
        return false;
    }

    // Verify results
    bool success = true;
    float tolerance = 1e-5f;

    for (int i = 0; i < out_size; i++) {
        if (std::abs(h_output[i] - expected[i]) > tolerance) {
            success = false;
            // Decode position in NCHW format
            int tmp = i;
            int w = tmp % out_W; tmp /= out_W;
            int h = tmp % out_H; tmp /= out_H;
            int c = tmp % C; tmp /= C;
            int n = tmp;
            std::cout << "  Mismatch at (n=" << n << ",c=" << c << ",h=" << h << ",w=" << w << "): "
                      << "got " << h_output[i] << ", expected " << expected[i] << std::endl;
        }
    }

    if (success) {
        std::cout << "  Success!" << std::endl;
    }

    // Cleanup
    cudaFree(d_input);
    cudaFree(d_output);

    return success;
}

int main() {
    bool all_passed = true;

    // ========== Existing tests with padding=0 ==========

    // Basic test case (N=1, C=1, stride=1, padding=0):
    all_passed &= test_max_pooling(
        {1.0f, 2.0f, 3.0f,
         4.0f, 5.0f, 6.0f,
         7.0f, 8.0f, 9.0f},
        {5.0f, 6.0f,
         8.0f, 9.0f},
        1, 1, 3, 3, 2, 1, 0,
        "basic_3x3_kernel2_stride1_pad0"
    );

    // Non-square test case (N=1, C=1, stride=1, padding=0):
    all_passed &= test_max_pooling(
        {1.0f, 2.0f, 3.0f, 4.0f,
         5.0f, 6.0f, 7.0f, 8.0f},
        {6.0f, 7.0f, 8.0f},
        1, 1, 2, 4, 2, 1, 0,
        "non_square_2x4_kernel2_stride1_pad0"
    );

    // Stride=2 test (padding=0):
    all_passed &= test_max_pooling(
        {1.0f,  2.0f,  3.0f,  4.0f,
         5.0f,  6.0f,  7.0f,  8.0f,
         9.0f,  10.0f, 11.0f, 12.0f,
         13.0f, 14.0f, 15.0f, 16.0f},
        {6.0f, 8.0f,
         14.0f, 16.0f},
        1, 1, 4, 4, 2, 2, 0,
        "stride2_4x4_kernel2_pad0"
    );

    // ========== Padding tests ==========

    // Padding=1 with 2x2 input, kernel=2, stride=1 -> 3x3 output
    // Padded input (4x4 with -inf):
    // [[-inf, -inf, -inf, -inf],
    //  [-inf,   1,    2,  -inf],
    //  [-inf,   3,    4,  -inf],
    //  [-inf, -inf, -inf, -inf]]
    // Output 3x3:
    // (0,0): max(-inf,-inf,-inf,1) = 1   (0,1): max(-inf,-inf,1,2) = 2   (0,2): max(-inf,-inf,2,-inf) = 2
    // (1,0): max(-inf,1,-inf,3) = 3      (1,1): max(1,2,3,4) = 4         (1,2): max(2,-inf,4,-inf) = 4
    // (2,0): max(-inf,3,-inf,-inf) = 3   (2,1): max(3,4,-inf,-inf) = 4   (2,2): max(4,-inf,-inf,-inf) = 4
    all_passed &= test_max_pooling(
        {1.0f, 2.0f,
         3.0f, 4.0f},
        {1.0f, 2.0f, 2.0f,
         3.0f, 4.0f, 4.0f,
         3.0f, 4.0f, 4.0f},
        1, 1, 2, 2, 2, 1, 1,
        "pad1_2x2_kernel2_stride1"
    );

    // "Same" padding: kernel=3, padding=1, stride=1 preserves dimensions
    // Input 3x3 -> Output 3x3
    // Each output is max of 3x3 window centered on that position
    // Corners and edges will have some -inf in their windows
    //
    // Input:       Padded (conceptually):
    // [[1, 2, 3],  [[-inf,-inf,-inf,-inf,-inf],
    //  [4, 5, 6],   [-inf,  1,   2,   3, -inf],
    //  [7, 8, 9]]   [-inf,  4,   5,   6, -inf],
    //               [-inf,  7,   8,   9, -inf],
    //               [-inf,-inf,-inf,-inf,-inf]]
    //
    // Output[0,0]: max of top-left 3x3 = max(1,2,4,5) = 5
    // Output[0,1]: max of top-center 3x3 = max(1,2,3,4,5,6) = 6
    // Output[0,2]: max of top-right 3x3 = max(2,3,5,6) = 6
    // Output[1,0]: max of mid-left 3x3 = max(1,2,4,5,7,8) = 8
    // Output[1,1]: max of center 3x3 = max(1,2,3,4,5,6,7,8,9) = 9
    // Output[1,2]: max of mid-right 3x3 = max(2,3,5,6,8,9) = 9
    // Output[2,0]: max of bot-left 3x3 = max(4,5,7,8) = 8
    // Output[2,1]: max of bot-center 3x3 = max(4,5,6,7,8,9) = 9
    // Output[2,2]: max of bot-right 3x3 = max(5,6,8,9) = 9
    all_passed &= test_max_pooling(
        {1.0f, 2.0f, 3.0f,
         4.0f, 5.0f, 6.0f,
         7.0f, 8.0f, 9.0f},
        {5.0f, 6.0f, 6.0f,
         8.0f, 9.0f, 9.0f,
         8.0f, 9.0f, 9.0f},
        1, 1, 3, 3, 3, 1, 1,
        "same_padding_3x3_kernel3"
    );

    // Padding with stride=2
    // Input 3x3, kernel=2, stride=2, padding=1
    // Padded input 5x5: output = (3 + 2*1 - 2) / 2 + 1 = 2x2
    // Padded:
    // [[-inf, -inf, -inf, -inf, -inf],
    //  [-inf,   1,    2,    3,  -inf],
    //  [-inf,   4,    5,    6,  -inf],
    //  [-inf,   7,    8,    9,  -inf],
    //  [-inf, -inf, -inf, -inf, -inf]]
    // Window (0,0) at padded (0,0): max(-inf,-inf,-inf,1) = 1
    // Window (0,1) at padded (0,2): max(-inf,-inf,2,3) = 3
    // Window (1,0) at padded (2,0): max(-inf,4,-inf,7) = 7
    // Window (1,1) at padded (2,2): max(5,6,8,9) = 9
    all_passed &= test_max_pooling(
        {1.0f, 2.0f, 3.0f,
         4.0f, 5.0f, 6.0f,
         7.0f, 8.0f, 9.0f},
        {1.0f, 3.0f,
         7.0f, 9.0f},
        1, 1, 3, 3, 2, 2, 1,
        "pad1_3x3_kernel2_stride2"
    );

    // 5x5 input with kernel=3, stride=1, padding=1 -> 5x5 output (same padding)
    all_passed &= test_max_pooling(
        {1.0f,  2.0f,  3.0f,  4.0f,  5.0f,
         6.0f,  7.0f,  8.0f,  9.0f,  10.0f,
         11.0f, 12.0f, 13.0f, 14.0f, 15.0f,
         16.0f, 17.0f, 18.0f, 19.0f, 20.0f,
         21.0f, 22.0f, 23.0f, 24.0f, 25.0f},
        {7.0f,  8.0f,  9.0f,  10.0f, 10.0f,
         12.0f, 13.0f, 14.0f, 15.0f, 15.0f,
         17.0f, 18.0f, 19.0f, 20.0f, 20.0f,
         22.0f, 23.0f, 24.0f, 25.0f, 25.0f,
         22.0f, 23.0f, 24.0f, 25.0f, 25.0f},
        1, 1, 5, 5, 3, 1, 1,
        "same_padding_5x5_kernel3"
    );

    // Padding with batch and channels (N=2, C=2)
    // 2x2 input, kernel=2, stride=1, padding=1 -> 3x3 output
    all_passed &= test_max_pooling(
        // Sample 0, Channel 0
        {1.0f, 2.0f,
         3.0f, 4.0f,
         // Sample 0, Channel 1
         5.0f, 6.0f,
         7.0f, 8.0f,
         // Sample 1, Channel 0
         -1.0f, -2.0f,
         -3.0f, -4.0f,
         // Sample 1, Channel 1
         0.0f, 0.0f,
         0.0f, 1.0f},
        // Sample 0, Channel 0: corners get single values, edges get max of 2, center gets max of 4
        {1.0f, 2.0f, 2.0f,
         3.0f, 4.0f, 4.0f,
         3.0f, 4.0f, 4.0f,
         // Sample 0, Channel 1
         5.0f, 6.0f, 6.0f,
         7.0f, 8.0f, 8.0f,
         7.0f, 8.0f, 8.0f,
         // Sample 1, Channel 0: all negative, corners still get their values
         -1.0f, -1.0f, -2.0f,
         -1.0f, -1.0f, -2.0f,
         -3.0f, -3.0f, -4.0f,
         // Sample 1, Channel 1
         0.0f, 0.0f, 0.0f,
         0.0f, 1.0f, 1.0f,
         0.0f, 1.0f, 1.0f},
        2, 2, 2, 2, 2, 1, 1,
        "pad1_batch_channels"
    );

    if (all_passed) {
        std::cout << "\nAll tests passed!" << std::endl;
        return 0;
    } else {
        std::cout << "\nSome tests failed!" << std::endl;
        return 1;
    }
}

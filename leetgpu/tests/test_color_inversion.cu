#include <iostream>
#include <vector>
#include <cuda_runtime.h>

extern "C" void solve(unsigned char* image, int width, int height);

bool run_test(std::vector<unsigned char> image, int width, int height,
              const std::vector<unsigned char>& expected, const char* name) {
    unsigned char* d_image;
    cudaMalloc(&d_image, width * height * 4 * sizeof(unsigned char));

    cudaMemcpy(d_image, image.data(), width * height * 4, cudaMemcpyHostToDevice);

    solve(d_image, width, height);

    cudaMemcpy(image.data(), d_image, width * height * 4, cudaMemcpyDeviceToHost);
    cudaError_t error = cudaGetLastError();
    if (error != cudaSuccess) {
        std::cout << name << ": CUDA error: " << cudaGetErrorString(error) << std::endl;
        cudaFree(d_image);
        return false;
    }

    bool success = true;
    for (int i = 0; i < width * height * 4; i++) {
        if (image[i] != expected[i]) {
            std::cout << name << ": Error at byte " << i << ": got " << (int)image[i]
                      << ", expected " << (int)expected[i] << std::endl;
            success = false;
        }
    }

    cudaFree(d_image);

    if (success) std::cout << name << ": PASSED" << std::endl;
    return success;
}

int main() {
    bool all_passed = true;

    // Example 1: width=1, height=2 (2 pixels)
    all_passed &= run_test(
        {255, 0, 128, 255, 0, 255, 0, 255},
        1, 2,
        {0, 255, 127, 255, 255, 0, 255, 255},
        "Example 1"
    );

    // Example 2: width=2, height=1 (2 pixels)
    all_passed &= run_test(
        {10, 20, 30, 255, 100, 150, 200, 255},
        2, 1,
        {245, 235, 225, 255, 155, 105, 55, 255},
        "Example 2"
    );

    if (all_passed) {
        std::cout << "Success! All color_inversion tests passed." << std::endl;
    }

    return all_passed ? 0 : 1;
}

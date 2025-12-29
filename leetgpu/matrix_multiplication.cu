#include <cuda_runtime.h>

__global__ void matrix_multiplication_kernel(const float* A, const float* B, float* C, int M, int N,
                                             int K) {
	// A is MxN, B is NxK, so output is MxK (M rows, K columns, indexed by y and x respectively)
	
	// naive approach, TODO come back to tiling
	int x = blockDim.x * blockIdx.x + threadIdx.x,
	    y = blockDim.y * blockIdx.y + threadIdx.y;

	if (y < M && x < K) {
		float total = 0.0f;
		for (int i = 0; i < N; i++) total += A[y * N + i] * B[i * K + x];
		C[y * K + x] = total;
	}
}

// A, B, C are device pointers (i.e. pointers to memory on the GPU)
extern "C" void solve(const float* A, const float* B, float* C, int M, int N, int K) {
    dim3 threadsPerBlock(16, 16);
    dim3 blocksPerGrid((K + threadsPerBlock.x - 1) / threadsPerBlock.x,
                       (M + threadsPerBlock.y - 1) / threadsPerBlock.y);

    matrix_multiplication_kernel<<<blocksPerGrid, threadsPerBlock>>>(A, B, C, M, N, K);
    cudaDeviceSynchronize();
}


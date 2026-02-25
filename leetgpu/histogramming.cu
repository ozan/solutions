#include <cuda_runtime.h>

#define BLOCK_SIZE 1024
#define NUM_BLOCKS 160
#define GRID_SIZE (BLOCK_SIZE * NUM_BLOCKS)

__global__ void histogram_kernel(const int *__restrict__ input,
                                 int *__restrict__ histogram, int N,
                                 int num_bins) {
  __shared__ int s_histo[1024];
  int gid = blockDim.x * blockIdx.x + threadIdx.x;

  // initialize shared memory
  s_histo[threadIdx.x] = 0;

  __syncthreads();

  // grid-stride loop with int4 vectorized loads
  const int4 *input4 = reinterpret_cast<const int4 *>(input);
  int N4 = N / 4;
  for (int i = gid; i < N4; i += GRID_SIZE) {
    int4 vals = input4[i];
    atomicAdd(&s_histo[vals.x], 1);
    atomicAdd(&s_histo[vals.y], 1);
    atomicAdd(&s_histo[vals.z], 1);
    atomicAdd(&s_histo[vals.w], 1);
  }

  // handle remainder elements (N % 4)
  int remainder_start = N4 * 4;
  for (int i = remainder_start + gid; i < N; i += GRID_SIZE) {
    atomicAdd(&s_histo[input[i]], 1);
  }

  __syncthreads();

  // each thread is responsible for its own accumulation into global histogram
  // this works since block size is 1024, and there is no more than 1024 bins
  if (threadIdx.x < num_bins) {
    atomicAdd(&histogram[threadIdx.x], s_histo[threadIdx.x]);
  }
}

// input, histogram are device pointers
extern "C" void solve(const int *input, int *histogram, int N, int num_bins) {
  histogram_kernel<<<NUM_BLOCKS, BLOCK_SIZE>>>(input, histogram, N, num_bins);
}

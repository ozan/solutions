#include <cuda_runtime.h>

__device__ double atomicAddDouble(double *address, double val) {
  unsigned long long *addr_as_ull = (unsigned long long *)address;
  unsigned long long old = *addr_as_ull, assumed;
  do {
    assumed = old;
    old = atomicCAS(addr_as_ull, assumed,
                    __double_as_longlong(__longlong_as_double(assumed) + val));
  } while (assumed != old);
  return __longlong_as_double(old);
}

void __global__ squared_errors(const float *__restrict__ predictions,
                               const float *__restrict__ targets,
                               double *total_se, int N) {
  int start = blockDim.x * blockIdx.x + threadIdx.x,
      stride = gridDim.x * blockDim.x;
  double local_total = 0, dif;

  for (int i = start; i < N; i += stride) {
    dif = predictions[i] - targets[i];
    local_total += dif * dif;
  }

  atomicAddDouble(
      total_se,
      local_total); // TODO on leetgpu, just atomicAdd(total_se, dif * dif);
}

void __global__ final_division(double *total_se, float *mse, int N) {
  *mse = *total_se / N;
}

// predictions, targets, mse are device pointers
extern "C" void solve(const float *predictions, const float *targets,
                      float *mse, int N) {
  // - Add shared memory at block level
  // - Shuffle warp
  //
  // Ideal grid stride:
  // On a Tesla T4 we have 40 SMs, with 1024 max threads per SM
  // With 256 thread blocks, we should theoretically saturate the SMs with a
  // grid size of 40 * 4 blocks, But let's use the rule of thumb 40 * 8 to have
  // enough scheduled
  int threadsPerBlock = 128;
  int numBlocks = 40 * 8; // 8 per SM to leave some in queue

  double *total_se;
  cudaMalloc(&total_se, sizeof(double));
  cudaMemset(total_se, 0, sizeof(double));

  squared_errors<<<numBlocks, threadsPerBlock>>>(predictions, targets, total_se,
                                                 N);

  final_division<<<1, 1>>>(total_se, mse, N);
}

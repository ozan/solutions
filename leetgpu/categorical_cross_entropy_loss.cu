#include <cuda_runtime.h>

void __global__ compute_losses(const float *__restrict__ logits,
                               const int *__restrict__ true_labels,
                               float *__restrict__ loss, int N, int C) {
  // We use one thread per sample, followed by a block-level reduction
  __shared__ float block_losses;
  int gid = blockDim.x * blockIdx.x + threadIdx.x;

  if (threadIdx.x == 0)
    block_losses = 0.0f;
  __syncthreads();

  if (gid < N) {
    float sum = 0.0f;
    for (int i = 0; i < C; i++) {
      sum += expf(logits[gid * C + i]);
    }
    float loss_j = logf(sum) - logits[gid * C + true_labels[gid]];
    atomicAdd(&block_losses, loss_j);
  }
  __syncthreads();

  if (threadIdx.x == 0)
    atomicAdd(loss, block_losses);
}

void __global__ take_average(float *loss, int N) { *loss = *loss / N; }

// logits, true_labels, loss are device pointers
extern "C" void solve(const float *logits, const int *true_labels, float *loss,
                      int N, int C) {
  // Given:
  // N samples across C classes (e.g. we may have 20 images to categorize as one
  // of 4 dog breeds) true_labels provides the index (0 to C - 1) of correct
  // label for each of N samples logits is N x C array of log odds (-inf to inf,
  // although in this case constrained -10 to 10)

  // For a single sample (out of N) we will need to iterate over all classes in
  // that row, exponentiate each one, sum, and take the log, then subtract the
  // log prob at the index determined by true_labels

  // As a final pass, we will add the losses and divide by N

  // As a naive approach we could use one thread per sample. This would be fine
  // for large numbers of samples? For fewer, it would be better to split each
  // sample across multiple threads, and stride.

  int threadsPerBlock = 128;
  int numBlocks = (N + threadsPerBlock - 1) / threadsPerBlock;

  compute_losses<<<numBlocks, threadsPerBlock>>>(logits, true_labels, loss, N,
                                                 C);
  take_average<<<1, 1>>>(loss, N);
}

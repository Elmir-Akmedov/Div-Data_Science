import pycuda.autoinit
import pycuda.driver as cuda
import numpy as np
from pycuda.compiler import SourceModule
import math

def gpu_primes_sieve(max_n):
    # Allocate memory for the sieve
    sieve = np.ones(max_n, dtype=np.bool_)  # Use boolean dtype for better memory efficiency
    sieve[:2] = False  # Mark 0 and 1 as non-prime

    # Transfer memory to GPU
    sieve_gpu = cuda.mem_alloc(sieve.nbytes)
    cuda.memcpy_htod(sieve_gpu, sieve)

    # CUDA Kernel for marking non-primes
    mod = SourceModule("""
    __global__ void mark_non_primes(bool *sieve, int max_n, int sqrt_max_n) {
        int idx = blockIdx.x * blockDim.x + threadIdx.x + 2;
        if (idx > sqrt_max_n) return;

        // Check if the number is prime
        if (sieve[idx]) {
            for (int j = idx * idx; j < max_n; j += idx) {
                sieve[j] = false;  // Mark multiples as non-prime
            }
        }
    }
    """)
    mark_non_primes = mod.get_function("mark_non_primes")

    # Configure grid and block sizes
    block_size = 256
    sqrt_max_n = int(math.sqrt(max_n))
    grid_size = (sqrt_max_n - 1 + block_size - 1) // block_size

    # Launch the kernel
    mark_non_primes(sieve_gpu, np.int32(max_n), np.int32(sqrt_max_n), 
                    block=(block_size, 1, 1), grid=(grid_size, 1, 1))

    # Copy results back to the host
    cuda.memcpy_dtoh(sieve, sieve_gpu)

    # Return the indices of primes
    return np.nonzero(sieve)[0]

# Calculate primes in the range 2-50,000,000
max_range = 50_000_000
primes = gpu_primes_sieve(max_range)
print(f"Found {len(primes)} primes up to {max_range}.")
print(f"First few primes: {primes[:10]}")
print(f"Last few primes: {primes[-10:]}")
import numpy as np
import time

def benchmark_numpy():
    print("--- NumPy Vectorization Benchmark ---")
    size = 10_000_000
    print(f"Generating arrays of size {size}...")

    a = np.random.rand(size)
    b = np.random.rand(size)

    # 1. Standard Python Loop (simulated on smaller subset for sanity)
    subset_size = 100_000
    print(f"\nRunning Python loop (subset size: {subset_size})...")
    start = time.time()
    result_loop = 0
    for i in range(subset_size):
        result_loop += a[i] * b[i]
    end = time.time()
    print(f"Python loop time: {end - start:.5f}s")

    # 2. NumPy Vectorization
    print(f"\nRunning NumPy dot product (full size: {size})...")
    start = time.time()
    result_numpy = np.dot(a, b)
    end = time.time()
    print(f"NumPy time: {end - start:.5f}s")

    print("\nConclusion: NumPy is orders of magnitude faster!")

if __name__ == "__main__":
    benchmark_numpy()

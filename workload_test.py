import time
import platform

def calculate(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

sizes = [("Small", 100_000), ("Medium", 1_000_000), ("Large", 10_000_000)]
RUNS = 5

print("WORKLOAD PERFORMANCE TEST (repeated)")
print(f"Python {platform.python_version()} on {platform.system()}")
print("-" * 60)

for name, size in sizes:
    times = []
    for _ in range(RUNS):
        start = time.perf_counter()
        result = calculate(size)
        times.append(time.perf_counter() - start)

    mean = sum(times) / RUNS
    runs = "  ".join(f"{t:.6f}" for t in times)
    print(f"{name} ({size:,})")
    print(f"  Runs (s): {runs}")
    print(f"  Mean (s): {mean:.6f}   Result: {result}")
    print("-" * 60)
    
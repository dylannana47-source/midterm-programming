import time
import statistics
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# =======================================================
# DO NOT MODIFY THE ALGORITHM IMPLEMENTATIONS
# =======================================================

def find_duplicates_slow(data):
    """An O(n^2) algorithm to find duplicates."""
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            if data[i] == data[j]:
                return True
    return False

def find_duplicates_fast(data):
    """An O(n) algorithm to find duplicates."""
    seen = set()
    for item in data:
        if item in seen:
            return True
        seen.add(item)
    return False


# =======================================================
# YOUR TASK: FIX THE BENCHMARKING SCRIPT BELOW
# =======================================================

def flawed_benchmark():
    """
    Benchmark the two duplicate-detection algorithms fairly across multiple input sizes.
    We generate the exact same data for both algorithms, use repeated trials, and time only
    the algorithm execution itself. A duplicate is placed near the end of the array so both
    algorithms must traverse a large fraction of the input before terminating.
    """
    print("Running robust benchmark...")

    sizes = [500, 1000, 2000, 4000, 8000, 16000]
    trials = 5
    slow_times = []
    fast_times = []

    for n in sizes:
        slow_runs = []
        fast_runs = []

        for _ in range(trials):
            data = list(range(n - 1))
            data.append(n - 2)
            # Warm up each function to reduce first-run noise.
            find_duplicates_slow(data)
            find_duplicates_fast(data)

            start = time.perf_counter()
            find_duplicates_slow(data)
            slow_runs.append(time.perf_counter() - start)

            start = time.perf_counter()
            find_duplicates_fast(data)
            fast_runs.append(time.perf_counter() - start)

        slow_times.append(statistics.median(slow_runs))
        fast_times.append(statistics.median(fast_runs))
        print(
            f"n={n:>5}: slow median = {slow_times[-1]:.8f}s, "
            f"fast median = {fast_times[-1]:.8f}s"
        )

    plot_results(sizes, slow_times, fast_times)


def plot_results(sizes, slow_times, fast_times):
    """Plot the benchmark results and save them as results.png."""
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, slow_times, marker="o", linewidth=2, label="O(n^2) nested loop")
    plt.plot(sizes, fast_times, marker="s", linewidth=2, label="O(n) set-based approach")
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Input size n")
    plt.ylabel("Median runtime (seconds)")
    plt.title("Duplicate-detection benchmark")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    plt.tight_layout()
    plt.savefig("results.png", dpi=300)
    plt.close()


if __name__ == "__main__":
    flawed_benchmark()
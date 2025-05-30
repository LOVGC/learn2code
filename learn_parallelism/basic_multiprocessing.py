import time
from multiprocessing import Pool, cpu_count
from concurrent.futures import ThreadPoolExecutor
import psutil
import math

physical_cores = psutil.cpu_count(logical=False)

# N = 100_000_000  # 任务规模（越大效果越明显）

N = 1_000_000  # 任务规模（越大效果越明显）

# lightweight计算任务
def compute1(x):
    return x * x

# heavyweight计算任务
def compute2(x):
    return math.factorial(500)

def benchmark(name, func):
    start = time.time()
    result = func()
    end = time.time()
    print(f"{name:<40} Time: {end - start:.2f} seconds")
    return result

if __name__ == "__main__":
    # 串行 for 循环
    benchmark("Serial for loop", lambda: [compute2(x) for x in range(N)])

    # 串行 map
    benchmark("Serial built-in map()", lambda: list(map(compute2, range(N))))


    # 多进程 multiprocessing.Pool（适合 CPU 密集）
    def run_multiprocessing_pool():
        with Pool(processes=physical_cores) as p:
            return p.map(compute2, range(N))
    benchmark("multiprocessing.Pool (multi-process)", run_multiprocessing_pool)


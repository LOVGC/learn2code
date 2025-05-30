import os
import multiprocessing
import psutil
import platform

'''multiprocessing:
- CPU 密集型：使用 physical cores 
- IO 密集型：使用 logical cores
'''


def detect_cpu_info():
    logical_cores = psutil.cpu_count(logical=True) # 获取逻辑核心数（线程数）
    physical_cores = psutil.cpu_count(logical=False) # 获取物理核心数
    cpu_name = platform.processor() or platform.uname().processor
    architecture = platform.machine()

    print("===== 🧠 CPU 架构检测 =====")
    print(f"CPU 名称           : {cpu_name}")
    print(f"CPU 架构           : {architecture}")
    print(f"逻辑核心数（线程） : {logical_cores}")
    print(f"物理核心数         : {physical_cores}")
    print(f"是否支持超线程     : {'是' if logical_cores > physical_cores else '否'}")
    print("===========================")
    return logical_cores, physical_cores


if __name__ == "__main__":
    # 运行检测
    detect_cpu_info()



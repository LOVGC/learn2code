# main.py

from scheduler import Scheduler
from tasks import square, cube

if __name__ == "__main__":
    num_workers = 4
    scheduler = Scheduler(num_workers)
    scheduler.start() # 启动所有 worker（它们会阻塞等待任务）

    task_list = [(square, (i,)) for i in range(10)] + [(cube, (i,)) for i in range(10)]
    scheduler.submit_tasks(task_list) # 主线程提交任务

    results = scheduler.collect_results(len(task_list)) # 收集结果

    for wid, res in results:
        print(f"Result from Worker {wid}: {res}")

    scheduler.stop()

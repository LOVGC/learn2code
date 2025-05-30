# worker.py

from multiprocessing import Process, Queue
import time

class Worker(Process):
    def __init__(self, id, task_queue, result_queue):
        super().__init__()
        self.id = id
        self.task_queue = task_queue
        self.result_queue = result_queue

    def run(self):
        while True:
            task = self.task_queue.get() # 这里会阻塞直到有任务
            if task is None:
                print(f"[Worker {self.id}] Shutting down.")
                break
            func, args = task
            print(f"[Worker {self.id}] Running task: {func.__name__}({args})")
            result = func(*args)  
            self.result_queue.put((self.id, result))

# scheduler.py

from multiprocessing import Queue
from worker import Worker
import time

class Scheduler:
    def __init__(self, num_workers):
        self.task_queue = Queue()
        self.result_queue = Queue()
        self.workers = [Worker(i, self.task_queue, self.result_queue) for i in range(num_workers)]

    def start(self):
        for w in self.workers:
            w.start()

    def stop(self):
        for _ in self.workers:
            self.task_queue.put(None)
        for w in self.workers:
            w.join()

    def submit_tasks(self, task_list):
        for task in task_list:
            self.task_queue.put(task)

    def collect_results(self, num_tasks):
        results = []
        for _ in range(num_tasks):
            results.append(self.result_queue.get())
        return results

import time


class TimeBenchmark:

    def set_task_name(self, task_name):
        self.task_name = task_name

    def take_time(self):
        return time.time()

    def take_start_time(self):
        self.start_time = self.take_time()
        return self.start_time

    def take_end_time(self):
        return self.take_time()

    def get_time_difference(self):
        self.time_difference = (self.take_end_time() - self.start_time)
        return self.time_difference

    def start_benchmark(self):
        self.take_start_time()

    def end_benchmark(self):
        self.take_end_time()

    def print_time_taken(self):
        print(self.task_name + " (time taken: " + str(self.time_difference) + ")")

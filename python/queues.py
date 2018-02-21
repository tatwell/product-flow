"""
Donald G Reinertsen, The Principles of Product Development Flow

Queuing Theory (p. 53)

"There are many different types of queuing process, but we can gain enormous
insight by looking at one of the simplest queues, what is called an
M/M/1/infinite queue."
"""
import numpy as np
import random
from collections import deque


class Queue(object):
    """A development queue as described Reinertsen."""
    def __init__(self, server_count=1, upper_limit=None):
        # The number "1" refers to the number of parallel servers in the system
        self.parallel_servers = server_count
        self.servers = []

        for n in range(server_count):
            server = QueueServer(self)
            self.servers.append(server)

        # The term "infinite" describes the upper limit on the queue size
        self.upper_limit = upper_limit

        self.jobs = deque()
        self.jobs_completed = []
        self.lifespan = 0
        self.age = 0

    @property
    def all_jobs(self):
        jobs_in_progress = [server.job for server in self.servers if server.job]
        return self.jobs_completed + jobs_in_progress + list(self.jobs)

    @property
    def avg_job_duration(self):
        if len(self.jobs_completed) < 1:
            return None

        total_duration = sum(job.lifespan for job in self.jobs_completed)
        return total_duration / len(self.jobs_completed)

    def simulate(self):
        while self.age < self.lifespan:
            self.tick()

    def add(self, job):
        if self.upper_limit and len(self.queued_jobs) > self.upper_limit:
            raise ValueError('Queue has exceeded capacity')
        else:
            self.jobs.append(job)

    def tick(self):
        self.process_arrivals()
        self.process_service()
        print(self)
        self.age += 1

    def process_arrivals(self):
        """The first letter "M" refers to the arrival process, in this case a
        Markov process. In a Markov process, the elapsed time between arrivals
        is exponentially distributed This simply means that short inter-arrival
        times are more probable than long ones."""
        daily_job_count = np.random.poisson(2, 1)[0]
        for n in range(daily_job_count):
            job = QueueJob()

            # The second "M" refers to the service process. It tells us that the
            # service process is also a Markov process. This means the time it
            # takes to perform the service is also exponentially distributed
            # and memoryless.
            job.lifespan = np.random.poisson(2, 1)[0]

            self.add(job)

    def process_service(self):
        """The second "m" refers to the service process. It tells us that the
        service process is also a Markov process. With"""
        for server in self.servers:
            if not server.job and len(self.jobs) > 0:
                next_job = self.jobs.popleft()
                server.job = next_job
            server.tick()

    def __repr__(self):
        f = "<Queue servers=%s jobs=%s in_queue=%s complete=%s avg_duration=%s>"
        avg_duration = self.avg_job_duration and '%.2f' % (self.avg_job_duration) or 'N/A'
        return f % (len(self.servers),
                    len(self.all_jobs),
                    len(self.jobs),
                    len(self.jobs_completed),
                    avg_duration)

class QueueServer(object):
    def __init__(self, queue):
        self.queue = queue
        self.job = None

    def assign_job(self, job):
        self.job = job

    def tick(self):
        if not self.job:
            return

        self.job.tick()
        if self.job.is_complete():
            self.queue.jobs_completed.append(self.job)
            self.job = None

class QueueJob(object):
    def __init__(self):
        self.lifespan = 0
        self.age = 0

    def tick(self):
        self.age += 1

    def is_complete(self):
        return self.age >= self.lifespan

    def is_queued(self):
        return not self.is_complete()


def main():
    parallel_servers = 4
    queue = Queue(parallel_servers)
    queue.lifespan = 1000
    queue.simulate()


if __name__ == '__main__':
    main()

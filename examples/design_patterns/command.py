import time


def small_job() -> None:
    print('Performing small job and sleeping 1 seconds.')
    time.sleep(1)


def large_job(job_name: str) -> None:
    print(f'Performing large job ({job_name}) and sleeping 5 seconds.')
    time.sleep(5)


small_job()
small_job()
large_job('Lots to do')


import time
from abc import ABC, abstractmethod


class JobCommand(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class SmallJobCommand(JobCommand):
    def execute(self) -> None:
        print('Performing small job and sleeping 1 seconds.')
        time.sleep(1)


class LargeJobCommand(JobCommand):
    def __init__(self, job_name: str) -> None:
        self.job_name = job_name
        super().__init__()

    def execute(self) -> None:
        print(f'Performing large job ({self.job_name}) and sleeping 5 seconds.')
        time.sleep(5)


job_list = [
    SmallJobCommand(),
    SmallJobCommand(),
    LargeJobCommand('Lots to do')
]

for job in job_list:
    job.execute()

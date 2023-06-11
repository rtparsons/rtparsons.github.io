---
layout: post
title:  "The Command Pattern in Python"
date:   2023-05-29 20:00:00 +0000
categories: python design-patterns
permalink: /the-command-pattern-in-python/
---

The Command Pattern is a behavioral pattern that encapsulates a request or operation as an object. This is advantageous when we may want to defer the execution of some piece of code until later or group and pass around batches of related behavior. In essence, it enables the decoupling of the sender and receiver of a request by wrapping a request as an object.

Let's look at some code and see how the pattern could help us...

```python
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
```

In this example we define two job functions. `small_job` represents a task that takes a short amount of time and sleeps 1 second, `large_job` represents a larger task which takes longer. Apart from the time taken to execute the task, they also have different arguments as `large_job` take a `job_name` as a parameter.

At the end we create a few jobs and the code produces the following output...

```
Performing small job and sleeping 1 seconds.
Performing small job and sleeping 1 seconds.
Performing large job (Lots to do) and sleeping 5 seconds.
```

This works fine, but let's say we had 10 different job types and we wanted to alter functionality here in some way, such as to introduce multi-threaded processing of jobs. This would be tricky due to the different job names and differing arguments. Let's use the Command Pattern to fix that.

```python

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
```

Here we define an interface for the jobs using an abstract base class, `JobCommand`. This interface defines one function, `execute`, which will contain the work to be done in the concrete classes. A simple concrete implementation of this can be seen in `SmallJobCommand`.

A slightly more complex implementation is `LargeJobCommand`. Along with the logic for the function to be implemented, this also batches up any data we require for the function execution as class properties. We could also have arguments passed through from the execute function at runtime, however, this would need to be defined on the interface and passed to all implementations.

Finally, we define our job list, create some jobs and then loop over and execute them. The powerful part here is that the work isn't done until we call execute. We can now apply logic to this list of jobs such as sorting them or applying additional generic logic to all!

### Aren't all functions commands and could have this pattern applied to them?

A common mistake I see from new developers learning about design patterns is to see these patterns everywhere and therefore implement the pattern. The command pattern is a common target for this as all functions are candidates for this pattern.

The key here is that it allows us to *defer execution*. Commonly you will see this pattern used in conjunction with a list, where a list of commands is built up and then acted on. If you simply create a command and call it right away, there is a good chance that it's not needed.

### Conclusion

As you can see from this example, the Command Pattern allows us to encapsulate and defer function execution to a later point in time. This allows a great amount of flexibility in generalizing the calls to the execution and extending or altering that logic. Just be careful to apply it sparingly ;)
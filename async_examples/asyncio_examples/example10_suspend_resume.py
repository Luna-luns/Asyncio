"""
https://stackoverflow.com/questions/66687549/is-it-possible-to-suspend-and-restart-tasks-in-async-python

"""

import asyncio

class Suspendable:
    def __init__(self, target):
        self._target = target
        self._can_run = asyncio.Event()
        self._can_run.set()
        self._task = asyncio.ensure_future(self)

    def __await__(self):
        target_iter = self._target.__await__()
        iter_send, iter_throw = target_iter.send, target_iter.throw
        send, message = iter_send, None
        # This "while" emulates yield from.
        while True:
            # wait for can_run before resuming execution of self._target
            try:
                while not self._can_run.is_set():
                    yield from self._can_run.wait().__await__()
            except BaseException as err:
                send, message = iter_throw, err

            # continue with our regular program
            try:
                signal = send(message)
            except StopIteration as err:
                return err.value
            else:
                send = iter_send
            try:
                message = yield signal
            except BaseException as err:
                send, message = iter_throw, err

    def suspend(self):
        self._can_run.clear()

    def is_suspended(self):
        return not self._can_run.is_set()

    def resume(self):
        self._can_run.set()

    def get_task(self):
        return self._task
    

import time

async def heartbeat():
    while True:
        print(time.time())
        await asyncio.sleep(.2)

async def main():
    task = Suspendable(heartbeat())
    for i in range(5):
        print('suspending')
        task.suspend()
        await asyncio.sleep(1)
        print('resuming')
        task.resume()
        await asyncio.sleep(1)


asyncio.run(main())
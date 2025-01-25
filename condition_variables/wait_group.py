from threading import Condition
from tkinter import NONE


class WaitGroup:
    def __init__(self):
        self.wait_count = 0
        self.cv = Condition()

    def add(self, count: int) -> None:
        with self.cv:
            self.wait_count += count

    def done(self) ->None:
      with self.cv:
        if self.wait_count == 0:
            self.cv.notify_all()
        elif self.wait_count > 0:
            self.wait_count -= 1

    def wait(self) -> None:
        with self.cv:
            while self.wait_count > 0:
                self.cv.wait()
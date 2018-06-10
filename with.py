#!/usr/bin/env python
# with_example02.py


class Sample:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print exc_type
        print exc_val
        print exc_tb

    def do_something(self):
        bar = 1 / 0
        return bar + 10


with Sample() as sample:
    sample.do_something()

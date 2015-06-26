"""
Throttle Implementation
"""

class Throttle(object):

    def __init__(self, max_capacity, rate):
        self.max_capacity = max_capacity
        self.rate = rate
        self.last_check = None
        self.capacity = capacity

    def _update_capacity(self):
        pass

    @property
    def capacity_available(self):
        pass

    def consume(self, amount=1):
        pass


class BlockingThrottle(Throttle):

    def consume(self, amount=1, timeout=1):
        pass

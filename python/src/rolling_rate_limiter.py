from collections import deque
from datetime import datetime

class RateLimiter:
    """
    Calls expensive function at most 3 times every minute
    """

    ONE_MINUTE = 60000000

    def __init__(self, fn, maxTimes):
        """
        Creates a new rate limiter with the certain parameters
        :param: fn the function to call
        :param: maxTimes the maximum number of times to call the rate limiter in a minute
        """

        self.fn = fn
        self.maxTimes = maxTimes
        self.queue = deque([])

    def rate_limit(self):
        """
        Calls the expensive function only if it doesn't pass the rate limit
        """

        currTime =  datetime.now().microsecond

        if len(self.queue) > 0:
            lastTime = self.queue[0]

            # remove values from back of queue until the difference between the last time and 
            # the current time is <= one minute
            while len(self.queue) > 0 and currTime - lastTime > RateLimiter.ONE_MINUTE:
                self.queue.popleft()
                lastTime = self.queue[0]
        
        # add current time to queue if it doesn't hit rate limit
        if len(self.queue) >= self.maxTimes:
            return
        else:
            # call function
            self.fn()
            self.queue.append(currTime)


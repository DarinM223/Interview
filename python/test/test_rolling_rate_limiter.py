import unittest
from src.rolling_rate_limiter import RateLimiter


class TestRollingRateLimiter(unittest.TestCase):

    def testNormal(self):
        """
        Tests that calling rate_limit 3 times will 
        call the function 3 times
        """

        # 'closure' scope to keep track of count
        class Object:
            pass
        scope = Object()

        scope.numCalled = 0
        numCalled = 0
        def fun():
            scope.numCalled += 1

        rateLimiter = RateLimiter(fun, 3)

        rateLimiter.rate_limit()
        rateLimiter.rate_limit()
        rateLimiter.rate_limit()

        self.assertEqual(scope.numCalled, 3)

    def testFail(self):
        """
        Tests that calling a rate_limit 4 times in a minute will not 
        call the function the 4th time
        """

        class Object:
            pass
        scope = Object()

        scope.numCalled = 0
        numCalled = 0
        def fun():
            scope.numCalled += 1

        rateLimiter = RateLimiter(fun, 3)

        rateLimiter.rate_limit()
        rateLimiter.rate_limit()
        rateLimiter.rate_limit()
        rateLimiter.rate_limit()

        self.assertEqual(scope.numCalled, 3)


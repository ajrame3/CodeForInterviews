#50
class Solution:
    def myPow(self, x: float, n: int) -> float:

        self.cache = {}

        def helper(x, n):
            if x == 0: return 0
            if n == 0: return 1

            if n in self.cache:
                return self.cache[n]

            res = helper(x, n // 2)
            res = res * res
            self.cache[n] = res
            return x * res if n%2 else res

        
        res = helper(x, abs(n))
        return res if n >= 0 else (1 / res)
        
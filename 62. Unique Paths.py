import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        m_fact = math.factorial(m-1)
        n_fact = math.factorial(n-1)
        return math.factorial(n+m-2)//(m_fact*n_fact)
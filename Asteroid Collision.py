class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        n, i = len(asteroids), 0
        while i < n - 1 and asteroids:
            ast1, ast2 = asteroids[i], asteroids[i + 1]
            if (ast1 < 0 and ast2 < 0) or (ast1 > 0 and ast2 > 0) or (ast1 < 0):
                i += 1
            else:
                if abs(ast1) >= abs(ast2):
                    del asteroids[i + 1]
                    n += -1
                if abs(ast1) <= abs(ast2):
                    del asteroids[i]
                    n += -1
                    if i > 0: i += -1
        return asteroids

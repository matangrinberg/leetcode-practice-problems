class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.partial_weights = []
        total_weight = 0
        for weight in w:
            total_weight += weight
            self.partial_weights.append(total_weight)

        self.total_weight = total_weight
        self.n = len(w)

    def pickIndex(self):
        """
        :rtype: int
        """
        sampled_number = self.total_weight * random.random()
        for i in range (0, self.n):
            if sampled_number < self.partial_weights[i]:
                return i



# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

class TimeMap(object):

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.time_map[key].append((timestamp, value))


    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """

        values = self.time_map[key]
        if not values:
            return ""

        # Binary Search of values
        left, right = 0, len(values) - 1
        while left < right:
            middle = (left + right + 1) / 2
            previous_time, value = values[middle]
            if previous_time > timestamp:
                right = middle - 1
            else:
                left = middle

        finalTime, finalValue = values[left]
        if finalTime <= timestamp:
            return finalValue
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

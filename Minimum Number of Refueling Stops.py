class Solution(object):
    def minRefuelStops(self, target, tank, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int
        """
        pq = [] # Maximum Heap, (i.e. priority queue) simulated using negative values
        prevStation, count = 0, 0
        stations.append((target, float('inf')))

        for station, fuel in stations:
            tank -= station - prevStation
            while pq and tank < 0: # this means we should have refueled before
                tank += -heapq.heappop(pq)
                count += 1
            if tank < 0: return -1
            heapq.heappush(pq, -fuel)
            prevStation = station

        return count

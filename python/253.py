"""
253. Meeting Rooms II
Medium
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""

from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]):
        size = len(intervals)
        if size<=1: return size
        sorted_intervals = sorted(intervals)
        rooms=[[sorted_intervals[0][1]]]
        for i in range(1,size):
            booked = False
            for room in rooms:
                if sorted_intervals[i][0]>=room[-1]:
                    room.append(sorted_intervals[i][1])
                    booked = True
                    break
            if not booked:rooms.append([sorted_intervals[i][1]])
        return len(rooms)

    def minMeetingRooms1(self, intervals: List[List[int]]) -> int:
        size = len(intervals)
        if size<=1: return size
        heap = []
        for interval in sorted(intervals):
            if heap and interval[0]>=heap[0]:
                heapq.heappushpop(heap,interval[1])
            else:
                heapq.heappush(heap,interval[1])
        return len(heap)


if __name__ == "__main__":
    print(Solution().minMeetingRooms1([[0, 30],[5, 10],[15, 20]]))
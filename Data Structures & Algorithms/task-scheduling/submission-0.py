from collections import Counter
import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        We always wanna do the task that happen the most at the moment, 
        use a maxheap to store the frequency of each tasks, and also a 
        heap store all the task currently under cooldown
        The workflow is, we do the task on the top of the max heap, then 
        put it do cooldown heap, and we do that do all the task until
        all task complete
        """
        freqmap = Counter(tasks)
        maxh = []
        for freq in freqmap.values():
            heapq.heappush(maxh, -freq)
        queue = deque()
        time = 0
        while maxh or queue:
            time += 1
            if maxh:
                task = -heapq.heappop(maxh)
                task -= 1
                if task > 0:
                    queue.append([time + n, task])
            if queue and queue[0][0] == time:
                heapq.heappush(maxh, -queue[0][1])
                queue.popleft()
        return time




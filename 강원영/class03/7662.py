import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())

    # min heap, max heap을 둘 다 사용하기 때문에 한쪽힙에서 값을 pop할 경우 다른쪽 힙도 pop해야 한다.
    # visted[n]이 True면 n번째 삽입한 데이터가 힙에서 삭제되지 않고 존재한다는 뜻이다.
    min_heap = []
    max_heap = []
    visited = [False] * k

    for i in range(k):
        cmd, val = input().rstrip().split()
        val = int(val)

        if cmd == "I":
            heapq.heappush(min_heap, (val, i))
            heapq.heappush(max_heap, (-val, i))
            visited[i] = True
        elif val == 1:
            # max_heap이 비어있지 않고 max_heap의 가장 큰 값이 min_heap에 존재하지 않는다면 max_heap을 pop하라
            while max_heap and not visited[max_heap[0][1]]:
                heapq.heappop(max_heap)
            
            if max_heap:
                visited[max_heap[0][1]] = False
                heapq.heappop(max_heap)
        else:
            # min_heap이 비어있지 않고 min_heap의 가장 작은 값이 max_heap에 존재하지 않는다면 min_heap을 pop하라
            while min_heap and not visited[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                visited[min_heap[0][1]] = False
                heapq.heappop(min_heap)
                
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
        
    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        print(-max_heap[0][0], min_heap[0][0])
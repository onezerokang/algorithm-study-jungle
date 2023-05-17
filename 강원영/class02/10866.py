import sys
input = sys.stdin.readline

class Deque:
    def __init__(self):
        self.deque = []
    
    def push_front(self, data):
        self.deque.insert(0, data)

    def push_back(self, data):
        self.deque.append(data)

    def pop_front(self):
        if not self.deque:
            print(-1)
            return
        print(self.deque.pop(0))

    def pop_back(self):
        if not self.deque:
            print(-1)
            return
        print(self.deque.pop())

    def size(self):
        print(len(self.deque))

    def empty(self):
        print(0 if self.deque else 1)

    def front(self):
        if not self.deque:
            print(-1)
            return
        print(self.deque[0])

    def back(self):
        if not self.deque:
            print(-1)
            return
        print(self.deque[-1])

deque = Deque()

N = int(input())
for _ in range(N):
    cmd = input().rstrip().split()

    if cmd[0] == 'push_front':
        deque.push_front(cmd[1])
    elif cmd[0] == 'push_back':
        deque.push_back(cmd[1])
    elif cmd[0] == 'pop_front':
        deque.pop_front()
    elif cmd[0] == 'pop_back':
        deque.pop_back()
    elif cmd[0] == 'size':
        deque.size()
    elif cmd[0] == 'empty':
        deque.empty()
    elif cmd[0] == 'front':
        deque.front()
    elif cmd[0] == 'back':
        deque.back()
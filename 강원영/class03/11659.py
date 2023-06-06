import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums1 = list(map(int, input().split()))
nums2 = nums1

for i in range(1, N):
    nums2[i] += nums2[i - 1]

for _ in range(M):
    a, b = map(int, input().split())
    if a - 2 < 0:
        print(nums2[b - 1])
    else:
        print(nums2[b - 1] - nums2[a - 2])
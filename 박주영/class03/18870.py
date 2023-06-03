# 좌표 압축

# 시도1. 시간 초과
# import sys
# input = sys.stdin.readline

# N = int(input().rstrip())
# origin_nums = [] * N
# origin_nums = list(map(int, input().split()))
# nums = list(sorted(set(origin_nums)))

# # print(nums)

# for i in range(len(nums)):
#     for j in range(len(origin_nums)):
#         if origin_nums[j] == nums[i]:
#             origin_nums[j] = i

# for i in range(len(origin_nums)):
#     print(origin_nums[i], end=' ')

# 2. 이진 탐색
import sys
input = sys.stdin.readline

N = int(input().rstrip())
origin_nums = [] * N
origin_nums = list(map(int, input().split()))
nums = list(sorted(set(origin_nums))) # 이 배열의 인덱스가 압축된 좌표임

def binary(arr, target, start, end):
    if start > end:
        return
    mid = (start + end) // 2
    if target < arr[mid]:
        return binary(arr, target, start, mid)
    elif target > arr[mid]:
        return binary(arr, target, mid+1, end)
    elif target == arr[mid]:
        return mid

for j in origin_nums:
    ans = binary(nums, j, 0, len(nums))
    print(ans, end=' ')
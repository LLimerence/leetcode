# 209.长度最小的子数组
# 力扣题目链接
# 给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
# 示例：输入：s = 7, nums = [2,3,1,2,4,3] 输出：2 解释：子数组 [4,3] 是该条件下的长度最小的子数组。
def minarray(nums, s):
    left, right = 0, 0
    res = float('inf')
    sum = 0
    while right < len(nums):
        sum += nums[right]
        while sum >= s:
            res = min(res, right-left+1)
            sum -= nums[right]
            left += 1
        right += 1
    if res == float("inf"):
        return 0
    else:
        return res
if __name__ =="__main__":
    # nums = [int(i) for i in input().split(" ")]
    # s = int(input())
    x = minarray( nums = [2,3,1,2,4,3], s = 7)

# 977.
# 有序数组的平方
# 给你一个按
# 非递减顺序
# 排序的整数数组
# nums，返回
# 每个数字的平方
# 组成的新数组，要求也按
# 非递减顺序
# 排序。
# 示例
# 输入：nums = [-4, -1, 0, 3, 10]
# 输出：[0, 1, 9, 16, 100]
# 解释：平方后，数组变为[16, 1, 0, 9, 100]
# 排序后，数组变为[0, 1, 9, 16, 100]
# 暴力破解
def n_sort(nums):
    new =[]
    for i in range(len(nums)):
        nums[i] = nums[i]*nums[i]
        new.append(nums[i])
    new.sort()
    print(new)
n_sort(nums = [-4, -1, 0, 3, 10])
# 双指针
def n_sort2(nums):
    # 新建一个等长度的列表
    new = [-1]*len(nums)
    i, j, k = 0, len(nums)-1, len(nums)-1
    while i <= j:
        ll = nums[i]**2
        lr = nums[j]**2
        if ll>lr:
            new[k] = ll
            i+=1
        else:
            new[k] = lr
            j-=1
        k-=1
    return new

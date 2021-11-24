

def serch(nums, tar):
    l, r = 0, len(nums)
    while l < r:
        mid = (l+r)//2
        if nums[mid] < tar:
            l = mid+1
        elif nums[mid] > tar:
            r = mid
        else:
            return mid
    return l
if __name__ == "__main__":
    nums = [int(i) for i in input().split(" ")]
    tar = int(input())
    x = serch(nums, tar)
    print(x)


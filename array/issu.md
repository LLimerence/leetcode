## 一. 二分查找（一般在有序无重复的数组中都可以使用二分查找，二分查找重要在有边界的取值情况当取len(nums)时指针不在最后一个元素，当len(nums)-1时 指针就是最后一个）
### 1. 在35中为什么返回的是left?
#### 当在循环中找不到目标值的时候 说明已经跳出循环 此时的left肯定等于right+1 所以返回的插入位置就是left或者right+1
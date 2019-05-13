# 输入三个整数x,y,z，请把这三个数由小到大输出。

nums = []
for i in range(3):
    x = input('num:')
    nums.append(x)
nums.sort()
print(nums)

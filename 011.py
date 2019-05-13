# 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子
# 假如兔子都不死，问每个月的兔子总数为多少？

m = input('月份：')
if m == 1:
    rabbits = 1
elif m == 2:
    rabbits = 1
else:
    rabbits = (1 / (5 ** 0.5)) * (((1 + (5 ** 0.5)) / 2) ** m - ((1 - (5 ** 0.5)) / 2) ** m)
print(rabbits)

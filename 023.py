#打印出如下图案（菱形）:
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *

n = int(input("请输入行数 n："))
for i in range(0,n):
    a = abs(i - int(n/2))
    b = n - abs(i - int(n/2))
    print(" "*a+"*"*(b-a))
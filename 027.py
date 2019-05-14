# 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

s = input("请输入字符：")
for i in range(len(s) - 1, -1, -1):
    print(s[i], end="")

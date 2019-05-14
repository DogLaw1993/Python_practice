# 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

x=input('请输入一个数:')
a = len(x)
print('这是一个{}位数'.format(a))
b = -1
while a != 0:
    a -= 1
    if b == -1:
        print(x[-1:],end=' ')
        b=b-1
    else :
        print(x[b:b+1],end=' ')
        b=b-1

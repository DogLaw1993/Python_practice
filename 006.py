# 斐波那契数列。
# F(0)=0,F(1)=1,F(n)=F(n-1)+F(n-2)

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# 判断101-200之间有多少个素数，并输出所有素数。
from math import sqrt


def isPrime(n):
    if n <= 1:
        return False
    else:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                return False
            return True


prime = []
for j in range(100, 200):
    if isPrime(j) == True:
        prime.append(j)
print(prime)

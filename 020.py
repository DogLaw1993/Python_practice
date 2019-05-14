# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

m = 100
n = int(input("请输入反弹次数："))
total = []
l = []
for i in range(1, n + 1):
    if i == 1:
        total.append(m)
    else:
        total.append(2 * m)
    m = 0.5 * m
    l.append(m)
print(l)
print(total)
print("第%d次反弹的高度是：%f" % (n, l[n - 1]))
print("第%d次落地共经过%f米" % (n, sum(total)))

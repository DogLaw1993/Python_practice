# 输入某年某月某日，判断这一天是这一年的第几天？

y = int(input('year:\n'))
m = int(input('month:\n'))
d = int(input('day:\n'))

if m == 1:
    sum = d
elif m == 2:
    sum = 31 + d
elif (m >= 3) and ((y % 4 == 0 and y % 100 != 0) or y % 400 == 0):
    if m == 3:
        sum = 31 + 29 + d
    if m == 4:
        num = 31 + 29 + 31 + d
    if m == 5:
        sum = 31 + 29 + 31 + 30 + d
    if m == 6:
        num = 31 + 29 + 31 + 30 + 31 + d
    if m == 7:
        num = 31 + 29 + 31 + 30 + 31 + 30 + d
    if m == 8:
        num = 31 + 29 + 31 + 30 + 31 + 30 + 31 + d
    if m == 9:
        num = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + d
    if m == 10:
        num = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + d
    if m == 11:
        num = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + d
    if m == 12:
        num = 31 + 29 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + d
else:
    if m == 3:
        num = 31 + 28 + d
    if m == 4:
        num = 31 + 28 + 31 + d
    if m == 5:
        num = 31 + 28 + 31 + 30 + d
    if m == 6:
        num = 31 + 28 + 31 + 30 + 31 + d
    if m == 7:
        num = 31 + 28 + 31 + 30 + 31 + 30 + d
    if m == 8:
        num = 31 + 28 + 31 + 30 + 31 + 30 + 31 + d
    if m == 9:
        num = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + d
    if m == 10:
        num = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + d
    if m == 11:
        num = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + d
    if m == 12:
        num = 31 + 28 + 31 + 30 + 31 + 30 + 31 + 31 + 30 + 31 + 30 + d

print('第' + str(num) + '天')


#
# months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
# if 0 < m <= 12:
#     sum = months[m - 1]
# else:
#     print('error')
# sum += d
# leap = 0
# if (y % 400 == 0) or ((y % 4 == 0) and (y % 100 != 0)):
#     leap = 1
# if (leap == 1) and (m > 2):
#     sum += 1
# print('第' + str(num) + '天')
# 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。

week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def fun(s, week):
    a = input("please input a letter:")
    s = s + a
    result = []
    for i in week:
        if i.startswith(s):
            result.append(i)
    if len(result) == 1:
        return result
    else:
        return fun(s, result)


s = ''
print(fun(s, week))

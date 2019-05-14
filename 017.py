# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

import string

line = input('请输入一个字符串:')
letters = 0
numbers = 0
space = 0
others = 0
for i in line:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        numbers += 1
    elif i.isspace():
        space += 1
    else:
        others += 1
print('char=%d,num=%d,space=%d,others=%d' % (letters, numbers, space, others))

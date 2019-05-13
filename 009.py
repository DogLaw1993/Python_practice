# 暂停一秒输出。

import time

myD = {1: 'a', 2: 'b'}
for k, v in dict.items(myD):
    print(k, v)
    time.sleep(1)

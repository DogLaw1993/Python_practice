# 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%；
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

I = int(input('利润：'))
if I < 10:
    price = I * 0.1
elif I < 20:
    price = 1 + (I - 10) * 0.075
elif I < 40:
    price = 1 + 0.75 + (I - 20) * 0.05
elif I < 60:
    price = 1 + 0.75 + 1 + (I - 40) * 0.03
elif I < 100:
    price = 1 + 0.75 + 1 + 0.6 + (I - 60) * 0.015
elif I > 100:
    price = 1 + 0.75 + 1 + 0.6 + 0.6 + (I - 100) * 0.01

print(price)

# 3-1 最大公約数を求る関数
def gcf(num_1, num_2):
    stop = min(num_1, num_2)
    # 最大公約数：Greatest common divisor
    gcd = 0
    for i in range(1, stop):
        if num_1 % i == 0 and num_2 % i == 0:
            gcd = i
    return gcd
    
print(gcf(150,138))
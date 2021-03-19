# 3-1 最大公約数を求る関数
def gcf(num_1, num_2):
    stop = min(num_1, num_2)
    # 最大公約数：Greatest common divisor
    gcd = 0
    for i in range(1, stop):
        if num_1 % i == 0 and num_2 % i == 0:
            gcd = i
    return gcd

# 3-2
def average(a, b):
    return (a + b) / 2

def square_root(num, low, high):
    for i in range(20):
        guess = average(low, high)
        # print(guess)
        if guess ** 2 == num:
            break
        elif guess ** 2 > num:  # 小さいと予想する
            high = guess
        else:  # 大きいと予想する
            low = guess
    print(guess)

print(gcf(150,138))

# 200   14と15の間
square_root(200, 14, 15)
# 1000  31と32の間
square_root(1000, 31, 32)
# 50000 31と32の間
square_root(50000, 223, 224)
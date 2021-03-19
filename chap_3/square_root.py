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

square_root(60, 7, 8)

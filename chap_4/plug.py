def g(x):
    return 6 * x ** 3 + 31 * x ** 2 + 3 * x - 10

# 1時方程式(2x + 5 = 13)の解を求める関数
def plug():
    x = -100
    while x < 100:
        if g(x) == 0:
            print("x =", x)
        x += 1
    print("完了。")

plug()
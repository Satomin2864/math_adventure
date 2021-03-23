def equation(a, b, c, d):
    """ax + b =cx + d """
    return (d - b) / (a - c)

# 4-1
# Q. 12x + 18 = -34x + 67を解け
# A. 1.065217391304348
print(equation(12, 18, -34, 67))

# 4-2
# Q. 1/2x + 2/3 = 1/5x + 7/8
# A. 0.6944444444444446
print(equation(1 / 2, 2 / 3, 1 / 5, 7 / 8))


# 2-1
# 例：1~100の合計値を計算したい場合
# begin_num = 1, end_num = 100
def to_sum(begin_num, end_num):
    ans = 0
    for i in range(begin_num, end_num):
        ans += i
    return ans

# Q. 何かしらのパターンがあるか
# A. 桁が１つ増えると9と0が１つ
print(to_sum(1, 100))     # 4950
print(to_sum(1, 1000))    # 499500
print(to_sum(1, 10000))   # 49995000
print(to_sum(1, 100000))  # 4999950000

# 2-2
d = [53, 28, 54, 84, 65, 60, 22, 93, 62, 27, 16, 25, 74, 42, 4, 42, 15, 96, 11, 70, 83, 97, 75]
avg = sum(d) / len(d)
print(avg)
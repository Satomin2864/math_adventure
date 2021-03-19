def factors(num):
    """numの約数リストを返す"""
    facorList = []
    for i in range(1, num + 1):
        if num % i == 0:
            facorList.append(i)
    return facorList
print(factors(100))
from random import randint

def numberGame():
    number = randint(1, 100)
    print("number当てゲームです。")
    print("1~100までの数字を当ててください。")

    guess = int(input("いくつかと思いますか？"))
    while True:
        if number == guess:
            print("正解です")
            break
        elif number > guess:
            print("不正解です。もっと大きいです。")
        else:
            print("不正解です。もっと小さいです。")
        guess = int(input("いくつかと思いますか？"))

numberGame()
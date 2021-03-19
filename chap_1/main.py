from turtle import *

# 1-1
def square(sidelength=100):
    for i in range(4):
        forward(sidelength)
        right(90)

# 1-2
def squareCircle():
    for i in range(60):
        square(200)
        right(5)

# 1-3 辺の長さを指定して三角形を書く関数
def triangle(sidelength=100):
    for i in range(3):
        forward(sidelength)
        right(120)

# 1-4 引数に渡した数の辺をもつ図形を描画するか関数
def polygon(side_num=3):
    tmp = 360 / side_num
    for i in range(side_num):
        forward(100)
        right(tmp)

# 1-5
def turtleSpiral(length=5):
    for i in range(60):
        right(5)
        square(length)
        length += 5

# 1-6
def star(length=100):
    for i in range(5):
        forward(length)
        right(144)

def star_spiral():
    length = 100
    for i in range(60):
        right(5)
        star(length)
        length += 5

shape('turtle')
speed(0)

# square
# square_circle()
# triangle()
# polygon(12)
# turtle_spiral()
# star_spiral()
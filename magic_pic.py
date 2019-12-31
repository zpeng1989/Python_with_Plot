import turtle as tr
import numpy as np
import math

radiusBig = 360  # 大圆
radiusSmall = 340  # 小圆


def circle():
    tr.pensize(2)

    # 画大圆
    tr.penup()
    tr.right(90)
    tr.forward(radiusBig)
    tr.left(90)
    tr.pendown()  # 将圆形放置于画布中心
    tr.circle(radiusBig)
    # 画小圆
    tr.penup()
    tr.right(90)
    tr.backward(radiusBig - radiusSmall)
    tr.left(90)
    tr.pendown()  # 将圆形放置于画布中心
    tr.circle(radiusSmall)


def repeat(repeatNum):
    """
    绘制重复部分
    """
    # 修改画笔粗细
    tr.penup()
    tr.right(90)
    tr.backward(radiusSmall * 2)
    tr.right(90)
    tr.pendown()
    radius = radiusSmall
    for num in range(repeatNum):

        tr.pensize(2 / (num + 1))

        # 计算五角星边长(np.square：取平方，math.radians：度转弧度)
        pentagramLen = np.sqrt(
            np.square(radius) * 2 - np.square(radius) * 2 * math.cos(math.radians(144)))

        # 计算缩小值
        shrink = np.sqrt(np.square(radius) + np.square(radius * math.sin(math.radians(144))) -
                         2 * radius * radius * math.sin(math.radians(144)) * math.cos(
            math.radians(54)))

        # 从顶部开始绘制五边形
        tr.circle(radius, steps=5)  # 半径为radius圆的内切正steps边形

        # 绘制五角星
        tr.penup()
        tr.right(108)
        tr.pendown()
        for i in range(5):
            tr.right(144)
            tr.forward(pentagramLen)

        # 画圆
        tr.penup()
        tr.left(18)
        tr.backward(radius - shrink)
        tr.left(90)
        tr.pendown()  # 将圆形放置于画布中心
        tr.circle(shrink, extent=396)  # 绘制半径为shrink，角度为396的圆

        radius = shrink


def main():
    tr.screensize(bg="#262626")  # 设置背景颜色
    tr.pencolor('#F8F8FF')  # 修改画笔颜色
    tr.speed(10)  # 加快绘制速度
    tr.hideturtle()  # 隐藏画笔形状
    # 画圆
    circle()
    # 画圆里面的部分
    repeat(2)
    tr.exitonclick()  # 点击画布退出


if __name__ == '__main__':
    main()

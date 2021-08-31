from turtle import *
from random import *
from math import *

def tree(n,l):
    pd()
    # Shadow
    t = cos(radians(heading()+45))/8+0.25
    pencolor(t,t,t)
    pensize(n/3)
    forward(l)#画树枝

    if n>0:
        b = random()*15+10
        c = random()*15+10
        d = l*(random()*0.25+0.7)
        # Right branch
        right(b)
        tree(n-1,d)
        # Left branch
        left(b+c)
        tree(n-1,d)
        # Turn back
        right(c)
    else:
        # Leaves
        right(90)
        n=cos(radians(heading()-45))/4+0.5
        pencolor(n,n*0.8,n*0.8)
        circle(3)
        left(90)

        if(random()>0.7):
            pu()

            t = heading()
            an = -40 +random()*40
            setheading(an)
            dis = int(800*random()*0.5 + 400*random()*0.3 + 200*random()*0.2)
            forward(dis)
            setheading(t)

            pd()
            right(90)
            n = cos(radians(heading()-45))/4+0.5
            pencolor(n*0.5+0.5,0.4+n*0.4,0.4+n*0.4)
            circle(2)
            left(90)
            pu()

            t = heading()
            setheading(an)
            backward(dis)
            setheading(t)
    pu()
    backward(l)

def main():
    bgcolor(0.5, 0.5, 0.5)  # 背景色
    ht()  # 隐藏turtle
    speed(0)  # 速度 1-10渐进，0 最快
    tracer(0, 0)
    pu()  # 抬笔
    backward(100)
    left(90)  # 左转90度
    pu()  # 抬笔
    backward(300)  # 后退300
    tree(12, 100)  # 递归7层
    done()

if __name__ == "__main__":
    main()




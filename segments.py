import turtle as t
    
seg = ["7s0.gif","7s1.gif","7s2.gif","7s3.gif","7s4.gif","7s5.gif","7s6.gif","7s7.gif","7s8.gif","7s9.gif","7s10.gif"]
dot = "dot.gif"

digit1X= -100
digit2X= 115
digit1Y = 0
digit2Y = 0
isdotted = False

def disp_num(k, x,y):
    t.goto(x,y)
    t.shape(seg[k])
    t.stamp()

def disp_dot():
    t.goto(-15,-90)
    t.shape(dot)
    t.stamp()


def key_0():
    if isdotted:
        disp_num(0,digit2X, digit2Y)

    else:
        disp_num(0,digit1X, digit1Y)

def key_1():
    if isdotted:
        disp_num(1,digit2X, digit2Y)

    else:
        disp_num(1,digit1X, digit1Y)

def key_2():
    if isdotted:
        disp_num(2,digit2X, digit2Y)

    else:
        disp_num(2,digit1X, digit1Y)

def key_3():
    if isdotted:
        disp_num(3,digit2X, digit2Y)

    else:
        disp_num(3,digit1X, digit1Y)

def key_4():
    if isdotted:
        disp_num(4,digit2X, digit2Y)

    else:
        disp_num(4,digit1X, digit1Y)

def key_5():
    if isdotted:
        disp_num(5,digit2X, digit2Y)

    else:
        disp_num(5,digit1X, digit1Y)

def key_6():
    if isdotted:
        disp_num(6,digit2X, digit2Y)
    else:
        disp_num(6,digit1X, digit1Y)

def key_7():
    if isdotted:
        disp_num(7,digit2X, digit2Y)
    else:
        disp_num(7,digit1X, digit1Y)

def key_8():
    if isdotted:
        disp_num(8,digit2X, digit2Y)

    else:
        disp_num(8,digit1X, digit1Y)

def key_9():
    if isdotted:
        disp_num(9,digit2X, digit2Y)

    else:
        disp_num(9,digit1X, digit1Y)

def key_10():
    global isdotted
    disp_num(10,digit2X, digit2Y)
    disp_num(10,digit1X, digit1Y)
    isdotted = False


# 점을 표시하기 위한 함수.
def key_dot():
    global isdotted
    disp_dot()
    isdotted= True
        
        
t.setup(800,400)
s = t.Screen()
t.hideturtle()
t.speed(0)

for i in range(11):
    s.addshape(seg[i])
s.addshape(dot)

disp_num(10, digit1X, digit1Y)
disp_num(10, digit2X, digit2Y)

s.onkey(key_0, "0")
s.onkey(key_1, "1")
s.onkey(key_2, "2")
s.onkey(key_3, "3")
s.onkey(key_4, "4")
s.onkey(key_5, "5")
s.onkey(key_6, "6")
s.onkey(key_7, "7")
s.onkey(key_8, "8")
s.onkey(key_9, "9")
s.onkey(key_10, "r")
s.onkey(key_dot,".")
s.listen()

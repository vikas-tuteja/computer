import turtle
def tree(branchLen,t):
    if branchLen > 5:
        if branchLen >= 5 and branchLen < 20:
            t.width(1)
        elif branchLen >= 20 and branchLen < 35:
            t.width(2)
        elif branchLen >= 35 and branchLen < 50:
            t.width(3)
        elif branchLen >= 50 and branchLen < 65:
            t.width(4)
        elif branchLen >= 65 and branchLen < 80:
            t.width(5)

        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

def main():
    import pdb; pdb.set_trace()
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()
main()

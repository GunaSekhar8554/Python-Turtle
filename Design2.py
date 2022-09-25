import turtle
t = turtle.Turtle()
r = turtle.Turtle()
t.speed(10000000000000000000000000000000000000000000000)
r.speed(10000000000000000000000000000000000000000000000)
r.left(180)
c = 3
for x in range(500):
    t.left(5)
    t.circle(c)
    r.left(5)
    r.circle(c)
    c+=2


turtle.done()
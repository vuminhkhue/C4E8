from turtle import*

shape("turtle")
colors=['red','blue','brown','yellow','grey']
n=5
for i in range(n):
    color(colors[i])
    begin_fill()
    fd(50)
    left(90)
    fd(100)
    left(90)
    fd(50)
    left(90)
    fd(100)
    left(90)
    end_fill()
    fd(50)

import turtle as t
import colorsys

t.bgcolor("black")
t.tracer(50)

def draw():
    h = 0
    n = 50
    t.width(2)
    
    for i in range(300):
        c = colorsys.hsv_to_rgb(h, 1, 1)
        h += 1 / n
        t.color(c)
        t.forward(i * 1.5)
        t.left(59)
        t.circle(i * 0.5, 180)
        t.right(120)
        t.forward(i * 0.5)
    
draw()
t.done()

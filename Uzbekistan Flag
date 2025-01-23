from turtle import *

def yurish(turtle,tomon,gradus,x):
 if tomon==1:
  turtle.lt(gradus)
 if tomon==2:
  turtle.rt(gradus)
 turtle.fd(x)

def turtburchak(turtle,a,b):
 yurish(turtle,1,0,a)
 yurish(turtle,1,90,b)
 yurish(turtle,1,90,a)
 yurish(turtle,1,90,b)
 yurish(turtle,1,90,0)

def bulak(turtle,x,y,color,a,b):
 turtle.up()
 turtle.goto(x,y)
 turtle.down()
 turtle.begin_fill()
 turtle.fillcolor(color)
 turtburchak(turtle,a,b)
 turtle.end_fill()
 
def yulduz(turtle,x,y):
 turtle.up()
 turtle.goto(x,y)
 turtle.down()
 turtle.begin_fill()
 turtle.fillcolor('white')
 for m in range(5):
  turtle.fd(30)
  turtle.lt(216)
 turtle.end_fill()
 
def oy(turtle,x,y):
 turtle.up()
 turtle.goto(x,y)
 turtle.down()
 turtle.begin_fill()
 turtle.fillcolor('white')
 turtle.lt(45)
 turtle.circle(40,-270)
 turtle.lt(10)
 turtle.circle(33,270)
 turtle.end_fill()

oyna = Screen()
oyna.bgcolor('#aaffff')
oyna.title('Ozbekiston Respublikasi bayrogi')

qal = Turtle()
qal.speed(0)
qal.hideturtle()

bulak(qal,-200,-160,'green',450,100)
bulak(qal,-200,-60,'red',450,10)
bulak(qal,-200,-50,'white',450,100)
bulak(qal,-200,50,'red',450,10)
bulak(qal,-200,60,'blue',450,100)

qal2 = Turtle()
qal2.speed(0)
qal2.hideturtle()

#1-qator
yulduz(qal2,-110,80)
yulduz(qal2,-80,80)
yulduz(qal2,-50,80)
yulduz(qal2,-20,80)
yulduz(qal2,10,80)

#2-qator
yulduz(qal2,-80,115)
yulduz(qal2,-50,115)
yulduz(qal2,-20,115)
yulduz(qal2,10,115)

#3-qator
yulduz(qal2,-50,145)
yulduz(qal2,-20,145)
yulduz(qal2,10,145)

#oy
oy(qal2,-120,85)


oyna.mainloop()

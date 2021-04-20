import turtle
import random 

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing Ball Simulator")
wn.tracer(0)

balls = []

for _ in range(10):
    balls.append(turtle.Turtle())

colors = [ "red", "white", "grey", "green", "lightblue", "purple"]
shape = [ 'circle', 'triangle', 'square']

for ball in balls:
    ball.shape(random.choice(shape))
    ball.color(random.choice(colors))
    ball.penup()
    ball.speed(0)
    x = random.randint(-290, 290)
    y = random.randint(200, 400)
    ball.goto(x,y)
    ball.dy = 0
    ball.dx = random.randint(-3, 3)
    ball.da = random.randint(-5, 5)






gravity = 0.1

while True:
    wn.update()


    for ball in balls:
        ball.rt(ball.da)
        ball.dy -= gravity 
        ball.sety(ball.ycor() + ball.dy)

        ball.setx(ball.xcor() + ball.dx)

        #Check for collision and change ball color
        if ball.xcor() > 300:
            ball.dx *= -1
            ball.color(random.choice(colors))
            ball.shape(random.choice(shape))

        if ball.xcor() < -300:
            ball.dx *= -1
            ball.color(random.choice(colors))
            ball.shape(random.choice(shape))



        #Check for a bounce
        if ball.ycor() < -300:
            ball.dy *= -1

    














wn.mainloop()
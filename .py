import turtle

my_turtle = turtle.Turtle()
my_turtle.color("purple")
my_turtle.speed(5)

def circle(n,angle):
    for i in range(4):
        my_turtle.forward(n)
        my_turtle.right(angle)

for i in range(500):
    circle(200,90)
    my_turtle.right(11)
    

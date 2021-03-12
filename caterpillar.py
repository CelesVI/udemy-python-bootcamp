import turtle as t
import random as rand


t.bgcolor('yellow')

caterpie = t.Turtle()
caterpie.shape('square')
caterpie.speed(0)
caterpie.penup()
caterpie.hideturtle()

game_started = False
leaf = t.Turtle()
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('leaf',leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed()

text_turtle = False
text_turtle = t.Turtle()
text_turtle.write('Press space to start', align='center', font=('Arial',18,'bold')) 

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

def outsideWindow():
    left_wall = -t.window_width()/2
    right_wall = t.window_width()/2
    top_wall = t.window_height()/2
    bottom_wall = -t.window_height()/2
    (x,y) = caterpie.pos()
    out = x < left_wall or  x > right_wall or  y < bottom_wall or y > top_wall
    return out

def placeLeaf():
    leaf.hideturtle()
    leaf.setx(rand.randint(-200,200))
    leaf.sety(rand.randint(-200,200))
    leaf.showturtle()

def gameOver():
    caterpie.color('yellow')
    leaf.color('yellow')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER', align='center', font=('Arial',18,'bold'))


def displayScore(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width()/2) - 50
    y = (t.window_height()/2) - 50
    score_turtle.setpos(x,y)
    score_turtle.write(str(current_score), align='right', font=('Arial',40, 'bold'))


def startGame():
    global game_started
    if game_started:
        return
    game_started = True
    score = 0
    text_turtle.clear()
    caterpie_speed = 3
    caterpie_length = 3
    caterpie.shapesize(1,caterpie_length,1)
    caterpie.showturtle()
    displayScore(score)
    placeLeaf()

    while True:
        caterpie.forward(caterpie_speed)
        if caterpie.distance(leaf)<20:
            placeLeaf()
            caterpie_length += 1
            caterpie.shapesize(1,caterpie_length,1)
            caterpie_speed += 1
            score += 10
            displayScore(score)
        if outsideWindow():
            gameOver()
            break

def moveUp():
    if caterpie.heading() == 0 or caterpie.heading() == 180:
        caterpie.setheading(90)

def moveDown():
    if caterpie.heading() == 0 or caterpie.heading() == 180:
        caterpie.setheading(270)

def moveLeft():
    if caterpie.heading() == 90 or caterpie.heading() == 270:
        caterpie.setheading(180)

def moveRight():
    if caterpie.heading() == 90 or caterpie.heading() == 270:
        caterpie.setheading(0)

t.onkey(startGame, 'space')
t.onkey(moveUp, 'Up')
t.onkey(moveDown, 'Down')
t.onkey(moveLeft, 'Left')
t.onkey(moveRight, 'Right')
t.listen()
t.mainloop()
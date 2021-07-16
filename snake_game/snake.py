import turtle as t
import time as ti
import random as rd

t.bgcolor('yellow')
t.title('SNAKE game')
snake = t.Turtle()
snake.shape('square')
snake.speed(0)
snake.penup()
snake.hideturtle()

leaf = t.Turtle()
leaf_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('leaf',leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.speed()
leaf.hideturtle()

game_started = False
text = t.Turtle()
text.write('Press SPACE  to start' , align = 'center' , font = ('Arial',16,'bold'))
text.hideturtle()

score = t.Turtle()
score.hideturtle()
score.speed(0)


def outside_window():
	left = -t.window_width()/2
	right =t.window_width()/2
	up =t.window_height()/2
	bottom =-t.window_height()/2
	(x,y) = snake.pos()
	outside = x < left or x > right or y > up or y < bottom
	return outside

def game_over(fscore):
	snake.color('yellow')
	leaf.color('yellow')
	score.hideturtle()
	t.penup()
	t.hideturtle()
	t.write('GAME OVER!',str(fscore),align='center' , font=('Aerial',30,'normal'))

def display_score(current_score):
	score.clear()
	score.penup()
	x = (t.window_width()/2)-50
	y= (t.window_height()/2)-50
	score.setpos(x,y)
	score.write(str(current_score) , align = 'right',font=('Arial',40,'bold'))


def leaf_place():
	leaf.hideturtle()
	leaf.setx(rd.randint(-200,200))
	leaf.sety(rd.randint(-200,200))
	leaf.showturtle()

def start_game():
	global game_started
	if game_started:
		return
	
	game_started = True 

	score = 0
	text.clear()

	snake_speed = 2
	snake_length = 3
	snake.shapesize(1,snake_length,1)
	snake.showturtle()
	display_score(score)
	leaf_place()

	while True:
		snake.forward(snake_speed)
		if snake.distance(leaf)<20:
			leaf_place()
			snake_length = snake_length + 1
			snake.shapesize(1,snake_length,1)
			snake_speed = snake_speed + 1
			score= score + 10
			display_score(score)

		if outside_window():
			game_over(score)
			break
def move_up():
	if snake.heading()==0 or snake.heading()==180:
		snake.setheading(90)

def move_down():
	if snake.heading()==0 or snake.heading()==180:
		snake.setheading(270)

def move_left():
	if snake.heading()==90 or snake.heading()==270:
		snake.setheading(180)

def move_right():
	if snake.heading()==90 or snake.heading()==270:
		snake.setheading(0)


t.onkey(start_game,'space')
t.onkey(move_up,'Up')
t.onkey(move_right,'Right')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.listen()
t.mainloop()

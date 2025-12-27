
from tkinter.font import names
from turtle import Turtle, Screen
import random

screen=Screen()
screen.setup(height=400,width=500)
bet=screen.textinput(title="Make a bet",prompt="Which turtle will win the race?Enter a color: ")


rainbow_color=["red","orange","yellow","green","blue","purple"]
player=[]
def turtlee(name,x,y,color):
    name=Turtle()
    name.shape("turtle")
    name.color(color)
    name.penup()
    name.goto(x,y)
    player.append(name)


player_name=["Faisal","Sharique","Awaise","Aquib","Adil","Azim"]


y_cord=[-100,-50,0,50,100,150]


if bet:
    is_race_on=True


for i in range(0,len(player_name)):
    turtlee(player_name[i],-230,y_cord[i],rainbow_color[i])


while is_race_on:

    for n in player:

        n.forward(random.randint(0,10))
        if n.xcor()>230:
            is_race_on=False
            winner=n.pencolor()
            if bet==winner:
                print(f"You've won! {winner} turtle is the winner!")
            else:
                print(f"You've lost ! {winner} turtle is the winner!")



screen.exitonclick()


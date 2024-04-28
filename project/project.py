
import pgzrun
import random
from random import randint
WIDTH=562
HEIGHT=480
score=0
total_score=0
level_up=False
game_complete=False
game_over=False
final_level=2
current_level=1
car=Actor("car4")
coin=Actor("coin")
car.pos=WIDTH/2,HEIGHT-50
coin.pos=300,200
speed=3
bricks=[]
bricks.append(Actor("brick"))

def draw():
    global score,current_level,game_complete,game_over,total_score
    screen.clear()
    screen.blit("road",(0,0))
    car.draw()
    coin.draw() 
    screen.draw.text("Score:"+str(score),color="black",topleft=(10,10))
    screen.draw.text("Level:"+str(current_level),color="black",topleft=(500,10))
    brick_collide=car.colliderect(bricks)
    if game_complete==True:
        screen.fill("white")
        screen.draw.text("YOU WON!",color="red",topleft=(170,210),fontsize=60)
    elif game_over==True:
        screen.fill("black")
        screen.draw.text("Level:"+str(current_level),color="red",topleft=(170,180),fontsize=40)
        screen.draw.text("Final Score : "+str(total_score) ,color="red",topleft=(170,210), fontsize=40)
        screen.draw.text("Game Over",color="red",topleft=(170,240),fontsize=40)
    else:
        for brick in bricks:
            brick.draw()
            if brick_collide:
                game_over=True
def place_coin():
    coin.x=randint(40,(WIDTH-80))
    coin.y=randint(40,(HEIGHT-80))
place_coin()
def update():
    global score,current_level,level_up,game_complete,game_over,speed,total_score
    if keyboard.left:
        car.x=car.x-3
    elif keyboard.right:
        car.x=car.x+3
    elif keyboard.up:
        car.y=car.y-3
    elif keyboard.down:
        car.y=car.y+3
    coin_collide=car.colliderect(coin)
    brick_collide=car.colliderect(bricks)
    for brick in bricks:
        brick.y+=speed
        if brick.y>HEIGHT+20:
            brick.y=-30
            brick.x=randint(40,WIDTH-40)
    if brick_collide:
        game_over=True
    if coin_collide:
        score+=10
        total_score+=10
        place_coin()
    
    if score==50:
        if current_level==final_level:
            game_complete=True
        else:
            level_up=True            
    if level_up==True:
        current_level+=1
        speed=speed+1
        level_up=False
        score=0
       

pgzrun.go()

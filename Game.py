import turtle 
import time 
import random
########################### GETTING NUMBER OF RACERS #####################
racers = 0 
f=0
while True:
    racers = input("Enter The Number Of Racers (2-5):")
    if racers.isdigit():
        racers = int(racers)
    else:
        print("Input Is Not Numeric , Try Again")
        continue
    if 2<= racers <= 5:
        screen = turtle.Screen()
        screen.setup(700, 600)
        screen.title('Turtle Racing!')
        colors = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']
        random.shuffle(colors)
        colors1 = colors[:racers]
        turtles = []
        Gaps = 600//(len(colors1)+ 1)
############################ CREATING TURTLES ###########################        
        for i,color in enumerate(colors1):
            racer = turtle.Turtle()
            racer.color(color)
            racer.shape('turtle')
            racer.left(90)
            racer.penup()
            racer.setpos(-600//2 + (i + 1) * Gaps, -700//2 + 20)
            racer.pendown()
            turtles.append(racer)
############################ STARTING THE GAME ##########################################            
        while True:
            for racer in turtles:
                distance = random.randrange(1, 20)
                racer.forward(distance)

                x, y = racer.pos()
                if y >= 700// 2 - 5:
                    print("The Winner Of The Race Is ",end="")
                    print(colors[turtles.index(racer)]) 
                    f = 1 
                    break 
            if f==1:
                break    


    else:
        print("Number Is Not In Range of 2-5, Try Again") 

    time.sleep(5)
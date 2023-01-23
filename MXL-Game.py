# Wirtten by Mohaned Mohammed Sherhan , The LEGEND .

import turtle as t
wind1 = t.Screen()
wind1.title("MXL-Game")
wind1.bgcolor("#9BCD9B")
wind1.setup(width=1000,height=600)
wind1.tracer(0)
wind1.listen()


def The_Game():
    Scarin.clear()
    Scarin2.clear()

    wind = t.Screen()
    wind.title("MXL-Game")
    wind.bgcolor("#1874CD")
    wind.setup(width=1000,height=600)
    wind.tracer(0)

    ## The points ##############################
    points_num = 0
    points  = t.Turtle()
    points.color("#9400D3")
    points.penup()
    points.hideturtle()
    points.goto(-440,-290)

    ### The area #############################



    # The frist area
    area1 = t.Turtle()
    area1.shape("square")
    area1.color("red")
    area1.penup()
    area1.shapesize(stretch_wid=2, stretch_len=60)
    area1.goto(0,-150)

    # The area 2 
    area2 = t.Turtle()
    area2.shape("square")
    area2.color("red")
    area2.penup()
    area2.shapesize(stretch_wid=2, stretch_len=60)
    area2.goto(0,-40)

    # The area 3 
    area3 = t.Turtle()
    area3.shape("square")
    area3.color("red")
    area3.penup()
    area3.shapesize(stretch_wid=2, stretch_len=60)
    area3.goto(0,60)

    # The area 4 
    area4 = t.Turtle()
    area4.shape("square")
    area4.color("red")
    area4.penup()
    area4.shapesize(stretch_wid=2, stretch_len=60)
    area4.goto(0,150)

    # The last area 
    last_area = t.Turtle()
    last_area.shape("square")
    last_area.color("red")
    last_area.penup()
    last_area.shapesize(stretch_wid=2, stretch_len=60)
    last_area.goto(0,290)

    ### The Body safe in area 1 and 2 and 3 and 4 ##########################################

    # body safe 1 in area 1
    safe1_1 = t.Turtle()
    safe1_1.shape("square")
    safe1_1.color("white")
    safe1_1.penup()
    safe1_1.shapesize(stretch_wid=2)
    safe1_1.goto(300,-150)

    # body safe 2 in area 1
    safe2_1 = t.Turtle()
    safe2_1.shape("square")
    safe2_1.color("white")
    safe2_1.penup()
    safe2_1.shapesize(stretch_wid=2)
    safe2_1.goto(-300,-150)

    # body safe 1 in area 2
    safe1_2 = t.Turtle()
    safe1_2.shape("square")
    safe1_2.color("white")
    safe1_2.penup()
    safe1_2.shapesize(stretch_wid=2)
    safe1_2.goto(100,-40)

    # body safe 2 in area 2
    safe2_2 = t.Turtle()
    safe2_2.shape("square")
    safe2_2.color("white")
    safe2_2.penup()
    safe2_2.shapesize(stretch_wid=2)
    safe2_2.goto(-100,-40)

    # body safe 3 in area 2
    safe3_2 = t.Turtle()
    safe3_2.shape("square")
    safe3_2.color("white")
    safe3_2.penup()
    safe3_2.shapesize(stretch_wid=2)
    safe3_2.goto(-300,-40)

    # body safe 1 in area 3
    safe1_3 = t.Turtle()
    safe1_3.shape("square")
    safe1_3.color("white")
    safe1_3.penup()
    safe1_3.shapesize(stretch_wid=2)
    safe1_3.goto(-400,60)

    # body safe 1 in area 4
    safe1_4 = t.Turtle()
    safe1_4.shape("square")
    safe1_4.color("white")
    safe1_4.penup()
    safe1_4.shapesize(stretch_wid=2)
    safe1_4.goto(-250,150)

    # body safe 2 in area 4
    safe2_4 = t.Turtle()
    safe2_4.shape("square")
    safe2_4.color("white")
    safe2_4.penup()
    safe2_4.shapesize(stretch_wid=2)
    safe2_4.goto(130,150)

    # The last safe body in the last aera 
    safe_last = t.Turtle()
    safe_last.shape("square")
    safe_last.color("#00FFFF")
    safe_last.penup()
    safe_last.shapesize(stretch_wid=2)
    safe_last.goto(-20,290)

    ### The Enemy move in area 1 ############################

    # enemy 1 to move in area 1
    enemy = t.Turtle()
    enemy.shape("arrow")
    enemy.color("blue")
    enemy.shapesize(stretch_wid=1.5)
    enemy.penup()
    enemy.goto(0,-150)
    enemy.speed(0)
    enemy.dx = 0.5
    # enemy 2 to move in area 1
    enemy2 = t.Turtle()
    enemy2.shape("arrow")
    enemy2.color("blue")
    enemy2.shapesize(stretch_wid=1.5)
    enemy2.penup()
    enemy2.goto(-40,-150)
    enemy2.speed(0)
    enemy2.dx = 2
    # enemy 3 to move in area 1
    enemy3 = t.Turtle()
    enemy3.shape("arrow")
    enemy3.color("blue")
    enemy3.shapesize(stretch_wid=1.5)
    enemy3.penup()
    enemy3.goto(-80,-150)
    enemy3.speed(0)
    enemy3.dx = 0.6
    # enemy 4 to move in area 1
    enemy4 = t.Turtle()
    enemy4.shape("arrow")
    enemy4.color("blue")
    enemy4.shapesize(stretch_wid=1.5)
    enemy4.penup()
    enemy4.goto(-150,-150)
    enemy4.speed(0)
    enemy4.dx = 1
    # enemy 5 to move in area 1
    enemy5 = t.Turtle()
    enemy5.shape("arrow")
    enemy5.color("blue")
    enemy5.shapesize(stretch_wid=1.5)
    enemy5.penup()
    enemy5.goto(-350,-150)
    enemy5.speed(0)
    enemy5.dx = 1.5

    ### The Enemy move in area 2 ############################
    # enemy 1 to move in area 2
    enemy_2 = t.Turtle()
    enemy_2.shape("arrow")
    enemy_2.color("blue")
    enemy_2.shapesize(stretch_wid=1.5)
    enemy_2.penup()
    enemy_2.goto(-200,-40)
    enemy_2.speed(0)
    enemy_2.dx = 0.6
    # enemy 2 to move in area 2
    enemy2_2 = t.Turtle()
    enemy2_2.shape("arrow")
    enemy2_2.color("blue")
    enemy2_2.shapesize(stretch_wid=1.5)
    enemy2_2.penup()
    enemy2_2.goto(40,-40)
    enemy2_2.speed(0)
    enemy2_2.dx = 0.4
    # enemy 3 to move in area 2
    enemy3_2 = t.Turtle()
    enemy3_2.shape("arrow")
    enemy3_2.color("blue")
    enemy3_2.shapesize(stretch_wid=1.5)
    enemy3_2.penup()
    enemy3_2.goto(0,-40)
    enemy3_2.speed(0)
    enemy3_2.dx = 0.7
    # enemy 4 to move in area 2
    enemy4_2 = t.Turtle()
    enemy4_2.shape("arrow")
    enemy4_2.color("blue")
    enemy4_2.shapesize(stretch_wid=1.5)
    enemy4_2.penup()
    enemy4_2.goto(-40,-40)
    enemy4_2.speed(0)
    enemy4_2.dx = 0.8
    # enemy 5 to move in area 2
    enemy5_2 = t.Turtle()
    enemy5_2.shape("arrow")
    enemy5_2.color("blue")
    enemy5_2.shapesize(stretch_wid=1.5)
    enemy5_2.penup()
    enemy5_2.goto(340,-40)
    enemy5_2.speed(0)
    enemy5_2.dx = 0.9


    ### The Enemy move in area 3 ############################
    # enemy 1 to move in area 3
    enemy_3 = t.Turtle()
    enemy_3.shape("arrow")
    enemy_3.color("blue")
    enemy_3.shapesize(stretch_wid=1.5)
    enemy_3.penup()
    enemy_3.goto(-200,60)
    enemy_3.speed(0)
    enemy_3.dx = 0.6
    # enemy 2 to move in area 3
    enemy2_3 = t.Turtle()
    enemy2_3.shape("arrow")
    enemy2_3.color("blue")
    enemy2_3.shapesize(stretch_wid=1.5)
    enemy2_3.penup()
    enemy2_3.goto(40,60)
    enemy2_3.speed(0)
    enemy2_3.dx = 2
    # enemy 3 to move in area 3
    enemy3_3 = t.Turtle()
    enemy3_3.shape("arrow")
    enemy3_3.color("blue")
    enemy3_3.shapesize(stretch_wid=1.5)
    enemy3_3.penup()
    enemy3_3.goto(0,60)
    enemy3_3.speed(0)
    enemy3_3.dx = 0.7
    # enemy 4 to move in area 3
    enemy4_3 = t.Turtle()
    enemy4_3.shape("arrow")
    enemy4_3.color("blue")
    enemy4_3.shapesize(stretch_wid=1.5)
    enemy4_3.penup()
    enemy4_3.goto(-40,60)
    enemy4_3.speed(0)
    enemy4_3.dx = 0.8
    # enemy 5 to move in area 3
    enemy5_3 = t.Turtle()
    enemy5_3.shape("arrow")
    enemy5_3.color("blue")
    enemy5_3.shapesize(stretch_wid=1.5)
    enemy5_3.penup()
    enemy5_3.goto(340,60)
    enemy5_3.speed(0)
    enemy5_3.dx = 0.9
    # enemy 6 to move in area 3
    enemy6_3 = t.Turtle()
    enemy6_3.shape("arrow")
    enemy6_3.color("blue")
    enemy6_3.shapesize(stretch_wid=1.5)
    enemy6_3.penup()
    enemy6_3.goto(-450,60)
    enemy6_3.speed(0)
    enemy6_3.dx = 1


    ### The Enemy move in area 4 ############################
    # enemy 1 to move in area 4
    enemy_4 = t.Turtle()
    enemy_4.shape("arrow")
    enemy_4.color("blue")
    enemy_4.shapesize(stretch_wid=1.5)
    enemy_4.penup()
    enemy_4.goto(-200,150)
    enemy_4.speed(0)
    enemy_4.dx = 0.6
    # enemy 2 to move in area 4
    enemy2_4 = t.Turtle()
    enemy2_4.shape("arrow")
    enemy2_4.color("blue")
    enemy2_4.shapesize(stretch_wid=1.5)
    enemy2_4.penup()
    enemy2_4.goto(40,150)
    enemy2_4.speed(0)
    enemy2_4.dx = 0.4
    # enemy 3 to move in area 4
    enemy3_4 = t.Turtle()
    enemy3_4.shape("arrow")
    enemy3_4.color("blue")
    enemy3_4.shapesize(stretch_wid=1.5)
    enemy3_4.penup()
    enemy3_4.goto(0,150)
    enemy3_4.speed(0)
    enemy3_4.dx = 0.7
    # enemy 4 to move in area 4
    enemy4_4 = t.Turtle()
    enemy4_4.shape("arrow")
    enemy4_4.color("blue")
    enemy4_4.shapesize(stretch_wid=1.5)
    enemy4_4.penup()
    enemy4_4.goto(-40,150)
    enemy4_4.speed(0)
    enemy4_4.dx = 3
    # enemy 5 to move in area 4
    enemy5_4 = t.Turtle()
    enemy5_4.shape("arrow")
    enemy5_4.color("blue")
    enemy5_4.shapesize(stretch_wid=1.5)
    enemy5_4.penup()
    enemy5_4.goto(340,150)
    enemy5_4.speed(0)
    enemy5_4.dx = 1
    # enemy 6 to move in area 4
    enemy6_4 = t.Turtle()
    enemy6_4.shape("arrow")
    enemy6_4.color("blue")
    enemy6_4.shapesize(stretch_wid=1.5)
    enemy6_4.penup()
    enemy6_4.goto(-450,150)
    enemy6_4.speed(0)
    enemy6_4.dx = 1
    # enemy 6 to move in area 4
    enemy7_4 = t.Turtle()
    enemy7_4.shape("arrow")
    enemy7_4.color("blue")
    enemy7_4.shapesize(stretch_wid=1.5)
    enemy7_4.penup()
    enemy7_4.goto(-350,150)
    enemy7_4.speed(0)
    enemy7_4.dx = 1.5


    ### The player ###########################
    player = t.Turtle()
    player.shape("circle")
    player.color("black")
    player.shapesize(stretch_wid=1,stretch_len=1)
    player.penup()
    player.goto(-20,-270)

    ### def to mova The player ##########################
    def mova_up():
        y = player.ycor()
        y += 5
        player.sety(y)
    def mova_down():
        y = player.ycor()
        y -= 5
        player.sety(y)
    def mova_right():
        x = player.xcor()
        x += 5
        player.setx(x)
    def mova_left():
        x = player.xcor()
        x -= 5
        player.setx(x)

    wind.listen()
    wind.onkeypress(mova_up,"Up")
    wind.onkeypress(mova_down,"Down")
    wind.onkeypress(mova_right,"Right")
    wind.onkeypress(mova_left,"Left")


    ### While Loop To the game .#########################
    while True:
        ### updata The screen . ############################
        wind.update()

        ### Move the enemy in area 1 . ########################
        enemy.setx(enemy.xcor() + enemy.dx)
        enemy2.setx(enemy2.xcor() + enemy2.dx)
        enemy3.setx(enemy3.xcor() + enemy3.dx)
        enemy4.setx(enemy4.xcor() + enemy4.dx)
        enemy5.setx(enemy5.xcor() + enemy5.dx)

        ### Move the enemy in area 2 . ########################
        enemy_2.setx(enemy_2.xcor() + enemy_2.dx)
        enemy2_2.setx(enemy2_2.xcor() + enemy2_2.dx)
        enemy3_2.setx(enemy3_2.xcor() + enemy3_2.dx)
        enemy4_2.setx(enemy4_2.xcor() + enemy4_2.dx)
        enemy5_2.setx(enemy5_2.xcor() + enemy5_2.dx)

        ### Move the enemy in area 3 . ########################
        enemy_3.setx(enemy_3.xcor() + enemy_3.dx)
        enemy2_3.setx(enemy2_3.xcor() + enemy2_3.dx)
        enemy3_3.setx(enemy3_3.xcor() + enemy3_3.dx)
        enemy4_3.setx(enemy4_3.xcor() + enemy4_3.dx)
        enemy5_3.setx(enemy5_3.xcor() + enemy5_3.dx)
        enemy6_3.setx(enemy6_3.xcor() + enemy6_3.dx)

        ### Move the enemy in area 4 . ########################
        enemy_4.setx(enemy_4.xcor() + enemy_4.dx)
        enemy2_4.setx(enemy2_4.xcor() + enemy2_4.dx)
        enemy3_4.setx(enemy3_4.xcor() + enemy3_4.dx)
        enemy4_4.setx(enemy4_4.xcor() + enemy4_4.dx)
        enemy5_4.setx(enemy5_4.xcor() + enemy5_4.dx)
        enemy6_4.setx(enemy6_4.xcor() + enemy6_4.dx)
        enemy7_4.setx(enemy7_4.xcor() + enemy7_4.dx)


        ### change color of enemy when reaching the safe area 1 ###############################

        # change color of enemy1 when reaching the safe area 1 .
        if enemy.xcor() > 275 and enemy.xcor() < 315 :
            enemy.color("white")
        elif enemy.xcor() > 315:
            enemy.color("blue")
        else:
            if enemy.xcor() < -275 and enemy.xcor() > -315 :
                enemy.color("white")
            elif enemy.xcor() > -315:
                enemy.color("blue")
        # change color of enemy2 when reaching the safe area 1 .
        if enemy2.xcor() > 275 and enemy2.xcor() < 315 :
            enemy2.color("white")
        elif enemy2.xcor() > 315:
            enemy2.color("blue")
        else:
            if enemy2.xcor() < -275 and enemy2.xcor() > -315 :
                enemy2.color("white")
            elif enemy2.xcor() > -315:
                enemy2.color("blue")
        # change color of enemy3 when reaching the safe area 1 .
        if enemy3.xcor() > 275 and enemy3.xcor() < 315 :
            enemy3.color("white")
        elif enemy3.xcor() > 315:
            enemy3.color("blue")
        else:
            if enemy3.xcor() < -275 and enemy3.xcor() > -315 :
                enemy3.color("white")
            elif enemy3.xcor() > -315:
                enemy3.color("blue")
        # change color of enemy4 when reaching the safe area 1 .
        if enemy4.xcor() > 275 and enemy4.xcor() < 315 :
            enemy4.color("white")
        elif enemy4.xcor() > 315:
            enemy4.color("blue")
        else:
            if enemy4.xcor() < -275 and enemy4.xcor() > -315 :
                enemy4.color("white")
            elif enemy4.xcor() > -315:
                enemy4.color("blue")
        # change color of enemy5 when reaching the safe area 1 .
        if enemy5.xcor() > 275 and enemy5.xcor() < 315 :
            enemy5.color("white")
        elif enemy5.xcor() > 315:
            enemy5.color("blue")
        else:
            if enemy5.xcor() < -275 and enemy5.xcor() > -315 :
                enemy5.color("white")
            elif enemy5.xcor() > -315:
                enemy5.color("blue")

        ### change color of enemy when reaching the safe area 2 ###############################

        # change color of enemy1 when reaching the safe area 2 .
        if enemy_2.xcor() > 70 and enemy_2.xcor() < 117 :
            enemy_2.color("white")
        elif enemy_2.xcor() > 115:
            enemy_2.color("blue")
        elif enemy_2.xcor() < -70 and enemy_2.xcor() > -130 :
            enemy_2.color("white")
        elif enemy_2.xcor() > -130:
            enemy_2.color("blue")
        elif enemy_2.xcor() < -280 and enemy_2.xcor() > -320 :
            enemy_2.color("white")
        elif enemy_2.xcor() > -320:
            enemy_2.color("blue")
        # change color of enemy2 when reaching the safe area 2 .
        if enemy2_2.xcor() > 70 and enemy2_2.xcor() < 117 :
            enemy2_2.color("white")
        elif enemy2_2.xcor() > 115:
            enemy2_2.color("blue")
        elif enemy2_2.xcor() < -70 and enemy2_2.xcor() > -130 :
            enemy2_2.color("white")
        elif enemy2_2.xcor() > -130:
            enemy2_2.color("blue")
        elif enemy2_2.xcor() < -280 and enemy2_2.xcor() > -320 :
            enemy2_2.color("white")
        elif enemy2_2.xcor() > -320:
            enemy2_2.color("blue")
        # change color of enemy3 when reaching the safe area 2 .
        if enemy3_2.xcor() > 70 and enemy3_2.xcor() < 117 :
            enemy3_2.color("white")
        elif enemy3_2.xcor() > 115:
            enemy3_2.color("blue")
        elif enemy3_2.xcor() < -70 and enemy3_2.xcor() > -130 :
            enemy3_2.color("white")
        elif enemy3_2.xcor() > -130:
            enemy3_2.color("blue")
        elif enemy3_2.xcor() < -280 and enemy3_2.xcor() > -320 :
            enemy3_2.color("white")
        elif enemy3_2.xcor() > -320:
            enemy3_2.color("blue")
        # change color of enemy4 when reaching the safe area 2 .
        if enemy4_2.xcor() > 70 and enemy4_2.xcor() < 117 :
            enemy4_2.color("white")
        elif enemy4_2.xcor() > 115:
            enemy4_2.color("blue")
        elif enemy4_2.xcor() < -70 and enemy4_2.xcor() > -130 :
            enemy4_2.color("white")
        elif enemy4_2.xcor() > -130:
            enemy4_2.color("blue")
        elif enemy4_2.xcor() < -280 and enemy4_2.xcor() > -320 :
            enemy4_2.color("white")
        elif enemy4_2.xcor() > -320:
            enemy4_2.color("blue")
        # change color of enemy5 when reaching the safe area 2 .
        if enemy5_2.xcor() > 70 and enemy5_2.xcor() < 117 :
            enemy5_2.color("white")
        elif enemy5_2.xcor() > 115:
            enemy5_2.color("blue")
        elif enemy5_2.xcor() < -70 and enemy5_2.xcor() > -130 :
            enemy5_2.color("white")
        elif enemy5_2.xcor() > -130:
            enemy5_2.color("blue")
        elif enemy5_2.xcor() < -280 and enemy5_2.xcor() > -320 :
            enemy5_2.color("white")
        elif enemy5_2.xcor() > -320:
            enemy5_2.color("blue")


        ### change color of enemy when reaching the safe area 3 ###############################
        # change color of enemy1 when reaching the safe area 3 .
        if enemy_3.xcor() > -420 and enemy_3.xcor() < -380 :
            enemy_3.color("white")
        elif enemy_3.xcor() > -380:
            enemy_3.color("blue")
        # change color of enemy2 when reaching the safe area 3 .
        if enemy2_3.xcor() > -420 and enemy2_3.xcor() < -380 :
            enemy2_3.color("white")
        elif enemy2_3.xcor() > -380:
            enemy2_3.color("blue")
        # change color of enemy3 when reaching the safe area 3 .
        if enemy3_3.xcor() > -420 and enemy3_3.xcor() < -380 :
            enemy3_3.color("white")
        elif enemy3_3.xcor() > -380:
            enemy3_3.color("blue")
        # change color of enemy4 when reaching the safe area 3 .
        if enemy4_3.xcor() > -420 and enemy4_3.xcor() < -380 :
            enemy4_3.color("white")
        elif enemy4_3.xcor() > -380:
            enemy4_3.color("blue")
        # change color of enemy5 when reaching the safe area 3 .
        if enemy5_3.xcor() > -420 and enemy5_3.xcor() < -380 :
            enemy5_3.color("white")
        elif enemy5_3.xcor() > -380:
            enemy5_3.color("blue")
        # change color of enemy6 when reaching the safe area 3 .
        if enemy6_3.xcor() > -420 and enemy6_3.xcor() < -380 :
            enemy6_3.color("white")
        elif enemy6_3.xcor() > -380:
            enemy6_3.color("blue")


        ### change color of enemy when reaching the safe area 4 ###############################
        # change color of enemy1 when reaching the safe area 4 .
        if enemy_4.xcor() > 110 and enemy_4.xcor() < 150 :
            enemy_4.color("white")
        elif enemy_4.xcor() > 150:
            enemy_4.color("blue")
        elif enemy_4.xcor() < -220 and enemy_4.xcor() > -270 :
            enemy_4.color("white")
        elif enemy_4.xcor() > -220:
            enemy_4.color("blue")
        # change color of enemy2 when reaching the safe area 4 .
        if enemy2_4.xcor() > 110 and enemy2_4.xcor() < 150 :
            enemy2_4.color("white")
        elif enemy2_4.xcor() > 150:
            enemy2_4.color("blue")
        elif enemy2_4.xcor() < -220 and enemy2_4.xcor() > -270 :
            enemy2_4.color("white")
        elif enemy2_4.xcor() > -220:
            enemy2_4.color("blue")
        # change color of enemy3 when reaching the safe area 4 .
        if enemy3_4.xcor() > 110 and enemy3_4.xcor() < 150 :
            enemy3_4.color("white")
        elif enemy3_4.xcor() > 150:
            enemy3_4.color("blue")
        elif enemy3_4.xcor() < -220 and enemy3_4.xcor() > -270 :
            enemy3_4.color("white")
        elif enemy3_4.xcor() > -220:
            enemy3_4.color("blue")
        # change color of enemy4 when reaching the safe area 4 .
        if enemy4_4.xcor() > 110 and enemy4_4.xcor() < 150 :
            enemy4_4.color("white")
        elif enemy4_4.xcor() > 150:
            enemy4_4.color("blue")
        elif enemy4_4.xcor() < -220 and enemy4_4.xcor() > -270 :
            enemy4_4.color("white")
        elif enemy4_4.xcor() > -220:
            enemy4_4.color("blue")
        # change color of enemy5 when reaching the safe area 4 .
        if enemy5_4.xcor() > 110 and enemy5_4.xcor() < 150 :
            enemy5_4.color("white")
        elif enemy5_4.xcor() > 150:
            enemy5_4.color("blue")
        elif enemy5_4.xcor() < -220 and enemy5_4.xcor() > -270 :
            enemy5_4.color("white")
        elif enemy5_4.xcor() > -220:
            enemy5_4.color("blue")
        # change color of enemy6 when reaching the safe area 4 .
        if enemy6_4.xcor() > 110 and enemy6_4.xcor() < 150 :
            enemy6_4.color("white")
        elif enemy6_4.xcor() > 150:
            enemy6_4.color("blue")
        elif enemy6_4.xcor() < -220 and enemy6_4.xcor() > -270 :
            enemy6_4.color("white")
        elif enemy6_4.xcor() > -220:
            enemy6_4.color("blue")
        # change color of enemy7 when reaching the safe area 4 .
        if enemy7_4.xcor() > 110 and enemy7_4.xcor() < 150 :
            enemy7_4.color("white")
        elif enemy7_4.xcor() > 150:
            enemy7_4.color("blue")
        elif enemy7_4.xcor() < -220 and enemy7_4.xcor() > -270 :
            enemy7_4.color("white")
        elif enemy7_4.xcor() > -220:
            enemy7_4.color("blue")

        # Not Out of the screen for The enemy in area 1 .#########################################
        # enemy 1 area 1
        if enemy.xcor() > 500:
            enemy.setx(-500)
        # enemy 2 area 1
        if enemy2.xcor() > 500:
            enemy2.setx(-500)
        # enemy 3 area 1
        if enemy3.xcor() > 500:
            enemy3.setx(-500)
        # enemy 4 area 1
        if enemy4.xcor() > 500:
            enemy4.setx(-500)
        # enemy 5 area 1
        if enemy5.xcor() > 500:
            enemy5.setx(-500)

        # Not Out of the screen for The enemy in area 2 .#########################################
        # enemy 1 area 2
        if enemy_2.xcor() > 500:
            enemy_2.setx(-500)
        # enemy 2 area 2
        if enemy2_2.xcor() > 500:
            enemy2_2.setx(-500)
        # enemy 3 area 2
        if enemy3_2.xcor() > 500:
            enemy3_2.setx(-500)
        # enemy 4 area 2
        if enemy4_2.xcor() > 500:
            enemy4_2.setx(-500)
        # enemy 5 area 2
        if enemy5_2.xcor() > 500:
            enemy5_2.setx(-500)

        # Not Out of the screen for The enemy in area 3 .#########################################
        # enemy 1 area 3
        if enemy_3.xcor() > 500:
            enemy_3.setx(-500)
        # enemy 2 area 3
        if enemy2_3.xcor() > 500:
            enemy2_3.setx(-500)
        # enemy 3 area 3
        if enemy3_3.xcor() > 500:
            enemy3_3.setx(-500)
        # enemy 4 area 3
        if enemy4_3.xcor() > 500:
            enemy4_3.setx(-500)
        # enemy 5 area 3
        if enemy5_3.xcor() > 500:
            enemy5_3.setx(-500)
        # enemy 6 area 3
        if enemy6_3.xcor() > 500:
            enemy6_3.setx(-500)

        # Not Out of the screen for The enemy in area 4 .#########################################
        # enemy 1 area 4
        if enemy_4.xcor() > 500:
            enemy_4.setx(-500)
        # enemy 2 area 4
        if enemy2_4.xcor() > 500:
            enemy2_4.setx(-500)
        # enemy 3 area 4
        if enemy3_4.xcor() > 500:
            enemy3_4.setx(-500)
        # enemy 4 area 4
        if enemy4_4.xcor() > 500:
            enemy4_4.setx(-500)
        # enemy 5 area 4
        if enemy5_4.xcor() > 500:
            enemy5_4.setx(-500)
        # enemy 6 area 4
        if enemy6_4.xcor() > 500:
            enemy6_4.setx(-500)
        # enemy 7 area 4
        if enemy7_4.xcor() > 500:
            enemy7_4.setx(-500)


        ### player ##################
        if player.xcor() == enemy.xcor() and player.ycor() == enemy.ycor():
            player.goto(-20,-270)
        if player.xcor() == enemy2.xcor() and player.ycor() == enemy2.ycor():
            player.goto(-20,-270)
        if player.xcor() == enemy3.xcor() and player.ycor() == enemy3.ycor():
            player.goto(-20,-270)
        if player.xcor() == enemy4.xcor() and player.ycor() == enemy4.ycor():
            player.goto(-20,-270)
        if player.xcor() == enemy5.xcor() and player.ycor() == enemy5.ycor():
            player.goto(-20,-270)
        #  aera 2
        if player.xcor() == enemy_2.xcor() and player.ycor() == enemy_2.ycor():
            player.goto(-20,-270)
        if player.xcor() == enemy2_2.xcor() and player.ycor() == enemy2_2.ycor():
            player.goto(-20,-270)
        if player.xcor() == enemy3_2.xcor() and player.ycor() == enemy3_2.ycor():
            player.goto(-20,-270)
        if player.xcor() == enemy4_2.xcor() and player.ycor() == enemy4_2.ycor():
            player.goto(-20,-270)
        if player.xcor() == enemy5_2.xcor() and player.ycor() == enemy5_2.ycor():
            player.goto(-20,-270)
        #  aera 3
        if player.xcor() == enemy_3.xcor() and player.ycor() == enemy_3.ycor():
            player.goto(-20,-270)
        if player.xcor() == enemy2_3.xcor() and player.ycor() == enemy2_3.ycor():
            player.goto(-20,-270)
        if player.xcor() == enemy3_3.xcor() and player.ycor() == enemy3_3.ycor():
            player.goto(-20,-270)
        if player.xcor() == enemy4_3.xcor() and player.ycor() == enemy4_3.ycor():
            player.goto(-20,-270)
        if player.xcor() == enemy5_3.xcor() and player.ycor() == enemy5_3.ycor():
            player.goto(-20,-270)
        if player.xcor() == enemy6_3.xcor() and player.ycor() == enemy6_3.ycor():
            player.goto(-20,-270) 
        #  aera 4
        if player.xcor() == enemy_4.xcor() and player.ycor() == enemy_4.ycor():
            player.goto(-20,-270)
        if player.xcor() == enemy2_4.xcor() and player.ycor() == enemy2_4.ycor():
            player.goto(-20,-270)
        if player.xcor() == enemy3_4.xcor() and player.ycor() == enemy3_4.ycor():
            player.goto(-20,-270)
        if player.xcor() == enemy4_4.xcor() and player.ycor() == enemy4_4.ycor():
            player.goto(-20,-270)
        if player.xcor() == enemy5_4.xcor() and player.ycor() == enemy5_4.ycor():
            player.goto(-20,-270)
        if player.xcor() == enemy6_4.xcor() and player.ycor() == enemy6_4.ycor():
            player.goto(-20,-270)  
        if player.xcor() == enemy7_4.xcor() and player.ycor() == enemy7_4.ycor():
            player.goto(-20,-270) 

        ### Points ##################################
        if (player.ycor() > 260 ) and (player.xcor() > -32 and player.xcor() < -12 ):
            points_num += 1
            points.clear()
            player.goto(-20,-270)
            points.write("The points is : {}".format(points_num),font=("Courier", 15, "normal"))



        ### if when it exceeds the prpared area 1 . ####################################
        if (player.ycor()  > -180 and player.ycor() < -120 ) and (player.xcor() < 280 and player.xcor() > -280):
            player.goto(-20,-270)
        elif (player.ycor()  > -180 and player.ycor() < -120 ) and (player.xcor() < -320 and player.xcor() > -600):
            player.goto(-20,-270)
        elif (player.ycor()  > -180 and player.ycor() < -120 ) and (player.xcor() > 320 and player.xcor() < 600):
            player.goto(-20,-270)

        ### if when it exceeds the prpared area 2 . ####################################
        if (player.ycor()  > -70 and player.ycor() < -10 ) and (player.xcor() < 600 and player.xcor() > 110):
            player.goto(-20,-270)
        elif (player.ycor()  > -70 and player.ycor() < -10 ) and (player.xcor() < 90 and player.xcor() > -90):
            player.goto(-20,-270)
        elif (player.ycor()  > -70 and player.ycor() < -10 ) and (player.xcor() > -290 and player.xcor() < -110):
            player.goto(-20,-270)
        elif (player.ycor()  > -70 and player.ycor() < -10 ) and (player.xcor() > -600 and player.xcor() < -310):
            player.goto(-20,-270)

        ### if when it exceeds the prpared area 3 . ####################################    
        if (player.ycor()  > 30 and player.ycor() < 90 ) and (player.xcor() < 600 and player.xcor() > -390):
            player.goto(-20,-270)
        elif (player.ycor()  > 30 and player.ycor() < 90 ) and (player.xcor() < -410 and player.xcor() > -600):
            player.goto(-20,-270)

        ### if when it exceeds the prpared area 4 . ####################################
        if (player.ycor()  > 120 and player.ycor() < 180 ) and (player.xcor() < 600 and player.xcor() > 140):
            player.goto(-20,-270)
        elif (player.ycor()  > 120 and player.ycor() < 180 ) and (player.xcor() < 120 and player.xcor() > -240):
            player.goto(-20,-270)
        elif (player.ycor()  > 120 and player.ycor() < 180) and (player.xcor() > -600 and player.xcor() < -260):
            player.goto(-20,-270)

        ### if when it exceeds the prpared area The last 290 . ####################################    
        if (player.ycor()  > 260 ) and (player.xcor() < 600 and player.xcor() > -10):
            player.goto(-20,-270)
        elif (player.ycor()  > 260 ) and (player.xcor() < -30 and player.xcor() > -600):
            player.goto(-20,-270)


        ### if for The player #############################
        if player.xcor() > 500 :
            player.setx(-500)
        if player.xcor() < -500:
            player.setx(500)
        if player.ycor() < -280:
            player.sety(-280)

### GIF ###########################

Scarin = t.Turtle()

Scarin.color ("black")
Scarin.penup()
Scarin.hideturtle()
Scarin.goto(-160,0)
Scarin.write("Press The Letter 'a'",font=("Courier", 15, "normal"))

Scarin2 = t.Turtle()
Scarin2.penup()
Scarin2.hideturtle()
Scarin2.color ("black")
Scarin2.goto(-180,-180)
Scarin2.write("*The instrucions :\n1- To move Up press The Up key \n2- To move Down press Doen key \n3- To move right press right key \n4- To move left press left key \n \nProgrammed by Mohaned Mohammed Sherhan \nMy account in Github : Mohaned2023 \n      23-1-2023 , 3;40 PM",font=("Courier", 10, "normal"))
wind1.onkeypress(The_Game,"a")

while True:
    wind1.update()


import random
import curses #imports cursers into the script

s = curses.initscr() #Initiating the screen
curses.curs_set(0) #Seting the intital location
sh, sw = s.getmaxyx() #setting the screen height and screen width, geting both the maximum x and y positions of the screen
w= curses.newwin(sh, sw, 0, 0) #This opens a window for the game
w.keypad(1) #initise the keypad as an input
w.timeout(100) #Have the window refresh itself ever 100ms

#creating snake intital position
snk_x = sw/4 #Snake starting position at the middle of the screen
snk_y = sh/2 #The y center for the snake starting position
snake = [ # an array to draw the snake on the screen
    [snk_y,snk_x],
    [snk_y,snk_x-1],
    [snk_y,snk_x-2],
]

#Drawing the food
food = [sh/2,sw/2]
#Adding the food to the screen
w.addch(food[0],food[1], curses.ACS_PI)

key=curses.KEY_RIGHT#telling the snake where to go initially

while True:#setting the keyboard lookup loop
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    #Checking to see if the person has lost the game
    if snake[0][0] in [0,sh] or snake[0][1] in [0,sw] or snake[0] in snake [1:]: curses.endwin()
    quit()

    new_head = [snake[0][0],snake[0][1]]

    if key==curses.KEY_UP:
        new_head[0] -=1
    if key==curses.KEY_DOWN:
        new_head[0] +=1
    if key==curses.KEY_RIGHT:
        new_head[1] +=1
    if key==curses.KEY_LEFT:
        new_head[1] -=1

    snake_insert(0, new_head)

    if snake[0] == food:#if food has been ate
        food = None #snake has not ate
        while food is None:#generates new food
            nf= [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None
        w.addch(food[0], food[1], curses.ACS_PI)
    else:
        tail=snake.pop()
        w.addch(tail[0],tail[1], ' ')

    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

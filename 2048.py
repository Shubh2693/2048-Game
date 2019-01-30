from tkinter import *  
from random import *
from tkinter import messagebox
import copy

score = 0
previous_score=0
highscore = 0
state = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
previous_state = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
cell_color_map = {  0:"#9fbedf",2:"#eee4da", 4:"#ede0c8", 8:"#f2b179", 16:"#f59563", 
                    32:"#f67c5f", 64:"#f65e3b", 128:"#edcf72", 256:"#edcc61",
                    512:"#edc850", 1024:"#edc53f", 2048:"#edc22e" 
                 }

def new_game():
    global state
    state = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    x = randint(0,3)
    y = randint(0,3)
    state[x][y] = 2
    x = randint(0,3)
    y = randint(0,3)
    while(state[x][y]!=0):
        x = randint(0,3)
        y = randint(0,3)    
    state[x][y] = 2
    display()

def previous():
    global state
    global previous_state
    global score
    global previous_score
    for i in range(4):
        for j in range(4):
            state[i][j]=previous_state[i][j]
    score = previous_score
    display()


def restart():
    global highscore
    global score
    if score > highscore:
        highscore = score
    score = 0
    new_game()

def add2():
    global state
    x = randint(0,3)
    y = randint(0,3)
    while(state[x][y]!=0):
        x = randint(0,3)
        y = randint(0,3)    
    state[x][y] = 2


def right():
    print("Right")
    global state
    global score
    global previous_state
    global previous_score
    previous_score = score
    fp=3
    sp=3
    
    for i in range(4):
        for j in range(4):
            previous_state[i][j]=state[i][j]
  
    for i in range(4):
        fp=3
        sp=3
        for j in [3,2,1,0]:
            if(state[i][j]!=0):
                if(fp==3 and j==3):
                    fp-=1
                    sp = 3
                    continue
                else:    
                    if(state[i][j]==state[i][sp] and j!=sp):
                        state[i][sp] = 2*(state[i][sp])
                        score+=state[i][sp]
                        state[i][j]=0
                        sp-=1
                    else:
                        if(j==fp):
                            fp-=1
                            sp-=1
                        else:
                            if(state[i][sp]!=0):
                                sp-=1
                            state[i][fp]=state[i][j]
                            state[i][j]=0
                            fp-=1

    # check_state()

    temp = win()
    if(temp==1):
        restart()
    check = lose()
    if(check==0):
        messagebox.showinfo("Better Luck Next Time!!", "You Lose")
        restart()
    else:
        if(check==1):
            add2()
        else:
            pass
    display()

def left():
    print("Left")
    global state
    global score
    global previous_state
    global previous_score
    previous_score = score
    
    fp=0
    sp=0
    for i in range(4):
        for j in range(4):
            previous_state[i][j]=state[i][j]

    for i in range(4):
        fp=0
        sp=0
        for j in range(4):
            if(state[i][j]!=0):
                if(fp==0 and j==0):
                    fp+=1
                    sp = 0
                    continue
                else:    
                    if(state[i][j]==state[i][sp] and j!=sp):
                        state[i][sp] = 2*(state[i][sp])
                        score+=state[i][sp]
                        state[i][j]=0
                        sp+=1
                    else:
                        if(j==fp):
                            fp+=1
                            sp+=1
                        else:
                            if(state[i][sp]!=0):
                                sp+=1
                            state[i][fp]=state[i][j]
                            state[i][j]=0
                            fp+=1

    temp = win()
    if(temp==1):
        restart()
    check = lose()
    if(check==0):
        messagebox.showinfo("You Lose", "Better Luck Next Time!!")
        restart()
    else:
        if(check==1):
            add2()
        else:
            pass
    display()

def down():
    print("Down")
    global state
    global score
    global previous_state
    global previous_score
    previous_score = score
    
    fp=3
    sp=3
    for i in range(4):
        for j in range(4):
            previous_state[i][j]=state[i][j]

    for j in range(4):
        fp=3
        sp=3
        for i in [3,2,1,0]:
            if(state[i][j]!=0):
                if(fp==3 and i==3):
                    fp-=1
                    sp=3
                    continue
                else:    
                    if(state[i][j]==state[sp][j] and i!=sp):
                        state[sp][j] = 2*(state[sp][j])
                        score+=state[sp][j]
                        state[i][j]=0
                        sp-=1
                    else:
                        if(i==fp):
                            fp-=1
                            sp-=1
                        else:
                            if(state[sp][j]!=0):
                                sp-=1
                            state[fp][j]=state[i][j]
                            state[i][j]=0
                            fp-=1

    temp = win()
    if(temp==1):
        restart()
    check = lose()
    if(check==0):
        messagebox.showinfo("Better Luck Next Time!!", "You Lose")
        restart()
    else:
        if(check==1):
            add2()
        else:
            pass
    display()

def up():
    print("Up")
    global state
    global score
    global previous_state
    global previous_score
    previous_score = score
    
    fp=0
    sp=0
    for i in range(4):
        for j in range(4):
            previous_state[i][j]=state[i][j]
     
    for j in range(4):
        fp=0
        sp=0
        for i in range(4):
            if(state[i][j]!=0):
                if(fp==0 and i==0):
                    fp+=1
                    sp = 0
                    continue
                else:    
                    if(state[i][j]==state[sp][j] and i!=sp):
                        state[sp][j] = 2*(state[sp][j])
                        score+=state[sp][j]
                        state[i][j]=0
                        sp+=1
                    else:
                        if(i==fp):
                            fp+=1
                            sp+=1
                        else:
                            if(state[sp][j]!=0):
                                sp+=1
                            state[fp][j]=state[i][j]
                            state[i][j]=0
                            fp+=1

    
    temp = win()
    if(temp==1):
        restart()
    check = lose()
    if(check==0):
        messagebox.showinfo("Better Luck Next Time!!", "You Lose")
        restart()
    else:
        if(check==1):
            add2()
        else:
            pass
    display()

def win():
    global state
    global score
    global highscore
    if(highscore<score):
        highscore=score
    for i in range(4):
        for j in range(4):
            if(state[i][j]==2048):
                messagebox.showinfo("Congrats!!", "You Win")
                return 1
    return 0

def lose():
    global state
    main_frame = copy.deepcopy(state)
    for l in main_frame: 
        if 0 in l: 
            return 1
   
    for l in main_frame:
        l.insert(0,99)
        l.append(99)
    main_frame.insert(0,[99,99,99,99,99])
    main_frame.append([99,99,99,99,99])

    
    for x in range(1,5):
        for y in range(1,5):
            if main_frame[x][y] == main_frame[x-1][y]or  main_frame[x][y] == main_frame[x+1][y]or main_frame[x][y] == main_frame[x][y+1] or main_frame[x][y]==main_frame[x][y-1]:
                return 2

    return 0
        
def display():
    global state
    global score
    global highscore
    global cell_color_map
    for i in range(4):
        for j in range(4):
            canvas.create_rectangle(50+j*100,100+i*100,j*100+150,i*100+200,fill=cell_color_map[state[i][j]])
            if(state[i][j]):
                canvas.create_text(j*100+100,i*100+150,font=("Times",50,"bold"),text = state[i][j])
            
        
    canvas.create_rectangle(250,50,330,80,fill="white")
    canvas.create_rectangle(350,50,440,80,fill="white")
    canvas.create_text(285,30,font=("Times",14,"bold"),text="Score")
    canvas.create_text(390,30,font=("Times",14,"bold"),text="High Score")
    canvas.create_text(290,65,font=("Times",12,"bold"),text=score)
    canvas.create_text(395,65,font=("Times",12,"bold"),text=highscore)


root = Tk()
root.geometry("900x900")
root.title("2048")
canvas= Canvas(root,width=500,height=700,bg="#b3cce6")
canvas.create_text(80,50,font=("Times",50,"bold"),text=2048)
canvas.place(relx= 0.5, rely = 0.5, anchor= CENTER)
new_game()
display()

button_previous = Button(root,text="Previous",command =lambda: previous())
button_previous.place(x = 550 , y= 640,width =100,height=30) 


button_restart = Button(root,text="Restart",command =lambda: restart())
button_restart.place(x = 250 , y= 640,width =100,height=30) 

button_up = Button(root,text="w",command =lambda: up())
button_up.place(x = 440 , y= 610,width =30,height=30) 
button_down = Button(root,text ="s",command = lambda : down())
button_down.place(x = 440 , y = 640,width = 30, height =30)
button_left = Button(root,text ="a",command = lambda : left())
button_left.place(x = 410 , y = 639,width =30, height =30)
button_right = Button(root,text= "d",command = lambda: right())
button_right.place(x=470,y = 639,width =30,height =30)

root.bind('w', lambda event: up())
root.bind('a', lambda event: left())
root.bind('s', lambda event: down())
root.bind('d', lambda event: right())

# root.bind('w', lambda event: up())
# root.bind('a', lambda event: left())
# root.bind('s', lambda event: down())
# root.bind('d', lambda event: right())

root.resizable(0,0)
root.mainloop()








#tetris7.py
import tkinter
import random

#variable declaration
mouseX = 0
mouseY = 0
mouseC = 0
cursorX = 0
cursorY = 0

#function for the mouse positions
def mouse_move(e):
    global mouseX, mouseY
    mouseX = e.x
    mouseY = e.y
#function  to get the mouse click
def mouse_press(e):
    global mouseC
    mouseC = 1

board = []
check = []
for i in range(10):
    board.append([0,0,0,0,0,0,0,0])
    check.append([0,0,0,0,0,0,0,0])

def draw_piece():
    cvs.delete("PUZZLE")
    for y in range(10):
        for x in range(8):
            if board[y][x] > 0:
                cvs.create_image(x*72+60, y*72+60, image = p_img[board[y][x]],tag ="PUZZLE")

def check_cross():
    for y in range(10):
        for x in range(8):
            check[y][x] = board[y][x]

    for y in range(1,9):
        for x in range(8):
            if check[y][x] > 0:
                if check[y-1][x] == check[y][x] and check[y+1][x] == check[y][x]:
                    board[y-1][x] = 7
                    board[y][x] = 7
                    board[y+1][x] = 7

    for y in range(10):
        for x in range(1,7):
            if check[y][x]>0:
                if check[y][x-1] == check[y][x] and check[y][x+1] == check[y][x]:
                    board[y][x-1]= 7
                    board[y][x] = 7
                    board[y][x+1] = 7

    for y in range(1,9):
        for x in range(1,7):
            if check[y][x] > 0:
                if check[y-1][x-1] == check[y][x] and check[y+1][x+1] == check[y][x]:
                    board[y-1][x-1] = 7
                    board[y][x] = 7
                    board[y+1][x+1]=7
                if check[y+1][x-1] == check[y][x] and check[y-1][x+1] == check[y][x]:
                    board[y+1][x-1] = 7
                    board[y][x] = 7
                    board[y-1][x+1] = 7

def game_main():
    global cursorX, cursorY, mouseC
    if 660 <= mouseX and mouseX < 840 and 100 <= mouseY and mouseY < 160 and mouseC == 1:
        mouseC = 0
        check_cross()
    if 24 <= mouseX and mouseX < 24+72*8 and 24 <= mouseY and mouseY < 24*72+10:
            cursorX = int((mouseX -24)/72)
            cursorY = int((mouseY-24)/72)
            if mouseC == 1:
                mouseC = 0
                board[cursorY][cursorX] = random.randint(1,2)
    cvs.delete("CURSOR")
    cvs.create_image(cursorX*72+60, cursorY*72+60, image=cursor, tag="CURSOR")
    cvs.delete("PUZZLE")
    draw_piece()
    root.after(100,game_main)

#main driver
root = tkinter.Tk()
root.title("practice")
root.resizable(False,False)
root.bind("<Motion>",mouse_move)
root.bind("<ButtonPress>",mouse_press)
cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()

bg = tkinter.PhotoImage(file="neko_bg.png")
cursor = tkinter.PhotoImage(file="neko_niku.png")

p_img = [
    None,
    tkinter.PhotoImage(file="pokeball.gif"),
    tkinter.PhotoImage(file="victory.png"),
    tkinter.PhotoImage(file="heart.png"),
    tkinter.PhotoImage(file="kirby.gif"),
    tkinter.PhotoImage(file = "pika.png"),
    tkinter.PhotoImage(file="star.gif"),
    tkinter.PhotoImage(file = "neko_niku.png")
]

cvs.create_image(456,384, image = bg)
cvs.create_rectangle(660,100,840,160, fill = "white")
cvs.create_text(750,130, text="test",fill = "red", font = ("Times New Roman",30))
game_main()
root.mainloop()

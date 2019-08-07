#tetris2.py
#import the necessary drivers
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
#array for the tetris game
board = [
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0]
]

def draw_piece():
    for y in range(10):
        for x in range(8):
            if board[y][x] > 0:
                cvs.create_image(x*72+60, y*72+60, image = p_img[board[y][x]],tag ="PUZZLE")
#function to drop the pieces
def drop():
    for y in range(8,-1,1):
        for x in range(8):
            if puzzle[y][x] != 0 and puzzle[y+1][x] == 0:
                puzzle[y+1][x] = puzzle[y][x]
                puzzle[y][x] = 0

#function for the game
def game_main():
    global cursorX, cursorY, mouseC
    drop()
    if 24 <= mouseX and mouseX < 24+72*8 and 24 <= mouseY and mouseY < 24*72+10:
            cursorX = int((mouseX -24)/72)
            cursorY = int((mouseY-24)/72)
            if mouseC == 1:
                mouseC = 0
                puzzle[cursorY][cursorX] = random.randint(1,6)
    cvs.delete("CURSOR")
    cvs.create_image(cursorX*72+60, cursorY*72+60, image=cursor, tag="CURSOR")
    cvs.delete("PUZZLE")
    draw_piece()
    root.after(100,game_main)
    cvs.pack()

#main driver
root = tkinter.Tk()
root.title("practice")
root.resizable(False,False)
root.bind("<Motion>",mouse_move)
cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()

bg = tkinter.PhotoImage(file="neko_bg.png")
cursor = tkinter.PhotoImage(file="neko_niku.png")
p_img = [
None,
tkinter.PhotoImage(file="pokeball.png"),
tkinter.PhotoImage(file="superball.png"),
tkinter.PhotoImage(file="masterball.png"),
tkinter.PhotoImage(file="rain.png"),
tkinter.PhotoImage(file = "sun.png"),
tkinter.PhotoImage(file="premier-ball.png"),
tkinter.PhotoImage(file = "neko_cursor.png")
]

cvs.create_image(456,384, image = bg)
game_main()
root.mainloop()

#tetris1.py
import tkinter

#variable declaration
mouseX = 0
mouseY = 0
cursorX = 0
cursorY = 0


def mouse_move(e):
    global mouseX, mouseY
    mouseX = e.x
    mouseY = e.y

def game_main():
    global cursorX, cursorY
    if 24 <= mouseX and mouseX < 24+72*8 and 24 <= mouseY and mouseY < 24*72+10:
            cursorX = int((mouseX -24)/72)
            cursorY = int((mouseY-24)/72)
    cvs.delete("CURSOR")
    cvs.create_image(cursorX*72+60, cursorY*72+60, image=cursor, tag="CURSOR")
    root.after(100,game_main)

root = tkinter.Tk()
root.title("practice")
root.resizable(False,False)
root.bind("<Motion>",mouse_move)
cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()
#create the background image
bg = tkinter.PhotoImage(file="neko_bg.png")
#create the image of the cursor
cursor = tkinter.PhotoImage(file="neko_niku.png")

cvs.create_image(456,384, image = bg)
game_main()
root.mainloop()

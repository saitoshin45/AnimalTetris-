#saitoshin45 tetris game
import tkinter

#variables for the positions
mouseX = 0
mouseY = 0
mouseC = 0
cursorX = 0
cursorY = 0

#function to get the mouse's positions
def mouse_move(e):
    global mouseX, mouseY
    mouseX = e.x
    mouseY = e.y

def mouse_press(e):
    global mouseC
    mouseC = 1

def mouse_release(e):
    global mouseC
    mouseC = 0

def game_main():
    fnt =("Times New Roman", 30)
    txt = "mouse({},{}){}".format(mouseX, mouseY, mouseC)
    cvs.delete("test")
    cvs.create_text(456, 384, text=txt, fill="black",font=fnt,tag="test")
    root.after(100, game_main)

root = tkinter.Tk()
root.title("mouse input")
root.resizable(False, False)
root.bind("<Motion>", mouse_move)
root.bind("<ButtonPress>",mouse_press)
root.bind("<ButtonRelease>",mouse_release)
cvs = tkinter.Canvas(root, width=912, height = 768)
cvs.pack()
game_main()
root.mainloop()

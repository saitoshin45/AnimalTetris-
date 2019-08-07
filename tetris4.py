#teris4.py
import tkinter
#board array
#array for the tetris game
board = [
[1,0,0,0,0,0,1,2],
[0,2,0,0,0,0,3,4],
[0,0,3,0,0,0,0,0],
[0,0,0,4,0,0,0,0],
[0,0,0,0,5,0,0,0],
[0,0,0,0,0,6,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0],
[0,0,1,2,3,4,5,6]
]

def draw_piece():
    for y in range(10):
        for x in range(8):
            if board[y][x] > 0:
                cvs.create_image(x*72+60, y*72+60, image = p_img[board[y][x]],tag ="PUZZLE")

#function to drop the pieces
def drop():
    for y in range(8,-1,-1):
        for x in range(8):
            if board[y][x] != 0 and board[y+1][x] == 0:
                board[y+1][x] = board[y][x]
                board[y][x] = 0

def game_main():
    drop()
    cvs.delete("PUZZLE")
    draw_piece()
    root.after(100,game_main)

root = tkinter.Tk()
root.title("practice")
root.resizable(False,False)
cvs = tkinter.Canvas(root, width=912, height=768)
cvs.pack()

bg = tkinter.PhotoImage(file="neko_bg.png")
p_img = [
    None,
    tkinter.PhotoImage(file="pokeball.gif"),
    tkinter.PhotoImage(file="victory.png"),
    tkinter.PhotoImage(file="heart.png"),
    tkinter.PhotoImage(file="kirby.gif"),
    tkinter.PhotoImage(file = "pika.png"),
    tkinter.PhotoImage(file="star.gif"),
    tkinter.PhotoImage(file = "neko_cursor.png")
]

cvs.create_image(456,384, image = bg)
game_main()
root.mainloop()

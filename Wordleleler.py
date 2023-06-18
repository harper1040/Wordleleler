import random
import webbrowser
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

intro = "Welcome to wordleleler the shameless knock off of another game :D. " \
        "Come and play a game based around the one subject most of us hated in high school," \
        "YAY! Vocabulaly. Psshh forget spelling ;). Seriously though spell thing correctly " \
        "in game."

gameRow = 0
gameCol = 0
Round = 0
gameNum = 0


def alphaCom(letter):
        global gameRow
        global gameCol
        global Round
        global gameNum

        GameBoard(gameWindow, letter, gameRow, gameCol)
        num = gameNum - 1
        if letter == '< BACK':
            GameBoard(gameWindow, ' ', gameRow, gameCol)
            gameCol -= 1
            if gameCol < 0:
                gameCol = 0
        else:
            gameCol += 1
            if gameCol > num:
                gameCol = num

        print(gameCol)
        print(num)
        #print(letter)


class GameBoard(ttk.Frame):
        def __init__(self, parent, num, row, col):
                super().__init__(master=parent)

                self.rowconfigure(0, weight=1)
                self.columnconfigure((0, 1, 2), weight=1)
                ttk.Button(self, text=str(num), command=lambda: alphaCom(num)).grid(row=0, column=0)

                self.grid(row=row, column=col)


def createGame(num):
        global gameWindow
        global gameNum
        gameNum = num

        def crunkLever():
                pop = random.randint(0, 6)
                pop2 = random.randint(0, 6)
                GameBoard(gameWindow, 'pop', pop2, pop)


        def Playfield():
                for c in range(0, num):
                        for r in range(0, 6):
                                GameBoard(gameWindow, num, r, c)
                                #print(r)


        def Keyboard():
                c = 0
                r = 9
                home = 0
                for i in alpha:
                    if c == 10 and home == 0:
                        r += 1
                        c = 0
                        home = 1
                    elif c == 9 and home == 1:
                        r += 1
                        c = 1
                    GameBoard(gameWindow, i, r, c)
                    c += 1
        alpha = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
                 'c', 'v','b', 'n', 'm', '< BACK']
        gameWindow = Toplevel(root)
        gameWindow.title(f"WORDLELELER {num} LETTER")
        gameWindow.geometry('1000x800')
        Playfield()
        Keyboard()
        #print(num)
        b1 = tk.Button(gameWindow, text='test', command=crunkLever)
        b1.grid(row=8, column=3)




root = Tk()
root.title("WORDLELELER!!")
root.geometry("1000x800")
root.configure(background='blue')

img = ImageTk.PhotoImage(file='Media/wordleleler1.png')
img2 = ImageTk.PhotoImage(file='Media/words2.png')

labelPic = tk.Label(root, image=img)
labelPic.pack()

labelPic2 = tk.Label(root, image=img2)
labelPic2.pack()

label = tk.Label(root, background='blue')
label.pack(pady=20)

mainframe = tk.Frame(root)
mainframe.pack()

b1 = tk.Button(mainframe, text='5 Letters', command=lambda:createGame(5))
b1.grid(row=0, column=0)
b2 = tk.Button(mainframe, text='6 Letters', command=lambda:createGame(6))
b2.grid(row=0, column=1)
b3 = tk.Button(mainframe, text='7 Letters', command=lambda:createGame(7))
b3.grid(row=0, column=2)
b4 = tk.Button(mainframe, text='8 Letters', command=lambda:createGame(8))
b4.grid(row=0, column=3)
#label = tk.Text(root, height=3, width=125)
#label.pack(padx=10, pady=10)

#label.insert('1.0', intro)

root.mainloop()
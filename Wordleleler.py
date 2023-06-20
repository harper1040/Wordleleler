import random
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk
import Wordlists as wrls

gameRow = 0
gameCol = -1
Round = 0
gameNum = 0
guessWord = []
ranWord = []


class GameAnswer(ttk.Frame):
    def __init__(self, parent, num, row, col, color):
        super().__init__(master=parent)

        self.rowconfigure(0, weight=1)
        self.columnconfigure((0, 1, 2), weight=1)
        ttk.Label(self, text=str(num), font='seraph 14', justify=CENTER, background=color, border=1, relief='solid', width=5).grid(row=0, column=0)

        self.grid(row=row, column=col, padx=20, pady=20)

# Layout for the play field where you word guesses go.
class GameBoard(ttk.Frame):
        def __init__(self, parent, num, row, col):
                super().__init__(master=parent)

                self.rowconfigure(0, weight=1)
                self.columnconfigure((0, 1, 2), weight=1)
                ttk.Label(self, text=num, font='seraph 14', justify=CENTER, border=1, relief="solid",width=5).grid(row=0, column=0)

                self.grid(row=row, column=col, padx=20, pady=20)


class f(ttk.Frame):
    def __init__(self, parent, num, row, col):
        super().__init__(master=parent)

        self.rowconfigure(0, weight=1)
        self.columnconfigure((0, 1, 2), weight=1)
        ttk.Button(self, text=str(num),image=w, command=lambda: alphaCom(num)).grid(row=0, column=0)

        self.grid(row=row, column=col, padx=3, pady=2)


# Layout for the keyboard.
class KeyBoard(ttk.Frame):
    def __init__(self, parent, num, row, col):
        super().__init__(master=parent)

        self.rowconfigure(0, weight=1)
        self.columnconfigure((0, 1, 2), weight=1)
        ttk.Button(self, text=str(num), command=lambda: alphaCom(num)).grid(row=0, column=0)

        self.grid(row=row, column=col, padx=3, pady=2)


# This will run multiple checks to verify a letters existence and position in the ranWord. This it will color in the
# appropriate word with the right color to tell the player what is and isn't in the word as well as what is there but in
# the wrong place.
def infoColor(guess, ranWord, Round):
    green = []
    yellow = []
    grey = []
    gray = []
    check = []
    for i in range(0, len(guess)):
        if guess[i] == ranWord[i]:
            GameAnswer(gameWindow, guess[i], Round, i, "green")
            print(guess[i] + ' green ' + str(i))
            green.append(guess[i])
            for a in wrls.alpha:
                pass
        else:
            for l in ranWord:
                if l == guess[i]:
                    check.append(guess[i])

                else:
                    grey.append(guess[i])

    for i in set(grey):
        gray.append(i)
    for i in set(check):
        yellow.append(i)
    for i in yellow:
        for l in gray:
            if i == l:
                gray.remove(l)
    for i in range(0, len(guess)):
        for l in yellow:
            if l == guess[i]:
                GameAnswer(gameWindow, guess[i], Round, i, "yellow")
                print(guess[i] + " Yellow " + str(i))
    for i in range(0, len(guess)):
        for l in gray:
            if l == guess[i]:
                GameAnswer(gameWindow, guess[i], Round, i, "grey")
                print(guess[i] + " Gray " + str(i))


# Yay the player figured out the word and gets to take a victory lap in the form of a pop up. *golf clap*
def Winner():
    global gameRow
    global gameCol
    global Round
    endGame = Toplevel(root)
    endGame.title(f"WORDLELELER WINNER")
    endGame.geometry('1000x800')
    tk.Label(endGame, text='YAY YOU WON GOOD FOR YOU!!', font=20).pack()
    tk.Button(endGame, text='close', font=20, command=lambda:endGame.destroy()).pack()
    gameWindow.destroy()
    gameRow = 0
    gameCol = -1
    Round = 0

# Compares random word to the guessed word and is probably a useless function.
def isRight(guess):
    global ranWord
    if ranWord == guess:
        Winner()

# After 6 failed guesses this will pop up a new screen bemoaning your performance.
def loser():
    global gameRow
    global gameCol
    global Round
    endGame = Toplevel(root)
    endGame.title(f"WORDLELELER LOSER")
    endGame.geometry('1000x800')
    tk.Label(endGame, text=wrls.loser, font=20).pack()
    tk.Button(endGame, text='close', font=20, command=lambda:endGame.destroy()).pack()
    gameWindow.destroy()
    gameRow = 0
    gameCol = -1
    Round = 0

# Check to see if the word guessed is the random word. Play respective function for win or lose.
def checkGuess():
    global Round
    global gameCol
    global guessWord
    if Round == 5:
        isRight(guessWord)
        loser()
    else:
        isRight(guessWord)
        try:
            infoColor(guessWord, ranWord, Round)
            Round +=1
            gameCol = -1
            print(guessWord)
            #if win == guessWord:
            #    pass

            tk.Button(gameWindow, image=no, state=DISABLED).grid(row=8, column=4)
        except:
            pass
    guessWord = []

# Check if the word guessed is in the list of words.
def isReal():
    global guessWord
    global gameNum
    global numList
    w = ""
    guessWord = "".join(guessWord)
    print('I IS RUNNING!')
    print(w)
    print(guessWord)
    for i in numList:
        if i == guessWord:
            tk.Button(gameWindow, image=sub, command=checkGuess).grid(row=8, column=4)

# Used to tell the keyboard what to do when you click a letter or Back.
def alphaCom(letter):
        global gameRow
        global gameCol
        global Round
        global gameNum
        global guessWord
        tempWord = []

        num = gameNum - 1

        # Check to see if letters are typed if not disable back if so use back as normal. All back presses will pop
        # last entry to check var.
        if letter == '< BACK' and gameCol < 0:
            pass
        elif letter == '< BACK' and gameCol > num:
            for i in guessWord:
                tempWord.append(i)
            guessWord = tempWord
            gameCol -= 1
            GameBoard(gameWindow, ' ', Round, gameCol)
            guessWord.pop()
            tk.Button(gameWindow, image=no, state=DISABLED).grid(row=8, column=4)

        elif letter == '< BACK':
            gameCol -= 1
            GameBoard(gameWindow, ' ', Round, gameCol)
            guessWord.pop()

        # Check the state of the gameCol var. At the start of the game increment and type, if already playing type as
        # normal. Finaly prevent typing past the full word length. All typing will append to the check var.
        elif gameCol < 0:
            gameCol = 0
            GameBoard(gameWindow, letter, Round, gameCol)
            gameCol += 1
            guessWord.append(letter)

        elif gameCol > num:
            pass
        else:
            GameBoard(gameWindow, letter, Round, gameCol)
            gameCol += 1
            guessWord.append(letter)

        if gameCol > num:
            isReal()
        print(gameCol)
        print(num)
        #print(letter)

# Creates all the game field elements.
def createGame(variable, num):
        global gameWindow
        global gameNum
        global gameCol
        global numList
        global Round
        global gameCol
        global guessWord
        guessWord = []
        gameNum = num
        numList = variable
        Round = 0
        gameCol = 0


        def pickWord():
            global ranWord
            pick = variable[random.randint(0, len(variable))]
            ranWord = pick
            print(ranWord)


        def Playfield():
                for c in range(0, num):
                        for r in range(0, 6):
                                GameBoard(gameWindow, ' ', r, c)
                                #print(r)

        def Padding():
            c = 0
            r = 0
            skip = True
            while skip:
                GameBoard(gameWindow, ' ', r, c)
                r += 1
                if r == 12 and c == 11:
                    r = 0
                    c = 12
                elif r == 12 and c == 1:
                    r = 0
                    c = 11
                elif r == 12:
                    r = 0
                    c = 1

        def Keyboard():
                c = 0
                r = 9
                home = 0
                for i in wrls.alpha:
                    if c == 10 and home == 0:
                        r += 1
                        c = 0
                        home = 1
                    elif c == 9 and home == 1:
                        r += 1
                        c = 1
                    KeyBoard(gameWindow, i, r, c)
                    c += 1


        gameWindow = Toplevel(root)
        gameWindow.title(f"WORDLELELER {num} LETTER")
        gameWindow.geometry('1000x800')
        pickWord()
        Playfield()
        Keyboard()
        #print(num)
        tk.Button(gameWindow, image=no, state=DISABLED).grid(row=8, column=4)



# Create the opening window to choose which game to play.
root = Tk()
root.title("WORDLELELER!!")
root.geometry("1000x800")
root.configure(background='blue')

img = ImageTk.PhotoImage(file='Media/wordleleler1.png')
img2 = ImageTk.PhotoImage(file='Media/words2.png')
no = PhotoImage(file='Media/NoButton.png')
sub = PhotoImage(file='Media/SubmitButton.png')
w = PhotoImage(file='Media/NoButton.png')

labelPic = tk.Label(root, image=img)
labelPic.pack()

labelPic2 = tk.Label(root, image=img2)
labelPic2.pack()

label = tk.Label(root, background='blue')
label.pack(pady=20)

mainframe = tk.Frame(root)
mainframe.pack()

b1 = tk.Button(mainframe, text='5 Letters', command=lambda:createGame(wrls.Five, 5))
b1.grid(row=0, column=0)
b2 = tk.Button(mainframe, text='6 Letters', command=lambda:createGame(wrls.Six, 6))
b2.grid(row=0, column=1)
b3 = tk.Button(mainframe, text='7 Letters', command=lambda:createGame(wrls.Seven, 7))
b3.grid(row=0, column=2)
b4 = tk.Button(mainframe, text='8 Letters', command=lambda:createGame(wrls.Eight, 8))
b4.grid(row=0, column=3)

root.mainloop()
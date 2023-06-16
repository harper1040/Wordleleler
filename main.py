import random
import webbrowser

Five = ["anime", "stand", "drive", "grass", "trees", "doors", "notes", "shelf", "truck", "phone",
        "drill", "alarm", "light", "board", "mower", "sport", "chain", "table", "video", "molar",
        "radio", "house", "paint", "total", "cycle", "motor", "first", "third", "fifth",
        "rouge", "hobby", "glove", "towel", "space", "demon", "angel", "world", "touch", "cable",
        "lunch", "feast", "plate", "trash", "green", "mauve", "digit", "money", "index", "audio",
        "focus", "alpha", "clear", "media", "steam", "water", "broom", "brush", "clean", "power",
        "sword", "glory", "daisy", "flame", "brick", "spicy", ]

Six = ["figure", "weapon", "stairs", "hunter", "bottle", "mantle", "camera", "bypass", "active",
       "engine", "inhale", "second", "fourth", "catnip", "create", "gentle", "washer", "poison",
       "advice", "nozzle", "cowboy", "outlaw", "pirate", "planet", "record", "vision", "handle",
       "pepper", "tablet", "screen", "copper", "petrol", "dinner", "orange", "purple", "violet",
       "pliers", "basket", "soccer", "update", "native", "bridge", "export", "office", 
       "window", "supply", "pencil", "reader", "forget", "zinnia", "flower", "please",
       "retain", "public", "folder", "coupon", "ignite", "burner", "column", "drawer", "hearth", 
       "spouse", "lonely", "doctor", "falcon", "fabric",]

Seven = ["vehicle", "firearm", "setting", "roadway", "highway", "drillbit", "caution", "recycle", 
         "battery", "surface", "squeeze", "contact", "discard", "medical", "product", "minimum",
         "maximum", "machine", "network", "connect", "printer", "program", "sawdust", "android",
         "propane", "monitor", "fallout", "digital", "plywood", "upgrade", "browser", "dolphin",
         "project", "display", "malware", "shortcut", "charger", "cleaner", "measure", "reading",
         "morning", "receipt", "balance", "payment", "stapler", "lighter", "burning", "diploma",
         "pathway", "antenna", "falconer", "finally", "police", "husband", "flipper",  "crimson", ]

Eight = ["shoulder", "hibiscus", "transfer", "telepath", "scramble", "solution", "children",
         "glycerin", "keyboard", "gasolene", "windmill", "burgandy", "terminal", "bookcase",
         "digitize", "scissors", "baseball", "football", "lacrosse", "untitled", "purified",
         "computer", "calipers", "cucumber", "recharge", "purchase", "customer", "pedestal",
         "mushroom", "announce", "lifetime", ]

def count():
    for i in range(0, len(Eight)):
        word = len(Eight[i])
        if word != 8:
            print(Eight[i])
    print(len(Eight))

def Winner():
    print(" CONGRATULATIONS YOU WON YOU SMARTY YOU!!!")
    webbrowser.open('https://media0.giphy.com/media/tCV2LrPPYfqCY/giphy.gif?cid=ecf05e47hx1or12u1gwpxz2ma3scbkcsdjwala489l14ayr7&ep=v1_gifs_search&rid=giphy.gif&ct=g')

def checkIt(word, guess):
    checked = []
    for i in range(0, len(guess)):
        if word[i] == guess[i]:
            checked.append(guess[i])
        else:
            checked.append("/")
    print(checked)

    return(checked)

def doesExist(word, guess):
    similar = []
    for i in range(0, len(guess)):
        a = 0
        for l in word:
            if l == guess[i]:
                similar.append(word[a])

            a = a + 1
    print(set(similar))


def gameFive():
    print("This is Game Five")
    pick = Five[random.randint(0, len(Five))]
    i = 1
    while True:
        C1 = input(f"What is Guess {i}? ")
        if len(C1) < 5 or len(C1) > 5:
            C1 = input("Please guess a five letter word!")
        i = i + 1
        check1 = checkIt(pick, C1)
        doesExist(pick, C1)
        if C1 == pick:
            Winner()
            break
        if i == 7:
            break
    print(pick)
    print(check1)
    shallBegin()

def gameSix():
    print("This is Game Six")
    pick = Six[random.randint(0, len(Six))]
    i = 1
    while True:
        C1 = input(f"What is Guess {i}? ")
        if len(C1) < 6 or len(C1) > 6:
            C1 = input("Please guess a six letter word!")
        i = i + 1
        check1 = checkIt(pick, C1)
        doesExist(pick, C1)
        if C1 == pick:
            Winner()
            break
        if i == 7:
            break
    print(pick)
    print(check1)
    shallBegin()


def gameSeven():
    print("This is Game Seven")
    pick = Seven[random.randint(0, len(Seven))]
    i = 1
    while True:
        C1 = input(f"What is Guess {i}? ")
        if len(C1) < 7 or len(C1) > 7:
            C1 = input("Please guess a seven letter word!")
        i = i + 1
        check1 = checkIt(pick, C1)
        doesExist(pick, C1)
        if C1 == pick:
            Winner()
            break
        if i == 7:
            break
    print(pick)
    print(check1)
    shallBegin()

def gameEight():
    print("This is Game Eight")
    pick = Eight[random.randint(0, len(Eight))]
    i = 1
    while True:
        C1 = input(f"What is Guess {i}? ")
        if len(C1) < 8 or len(C1) > 8:
            C1 = input("Please guess a eight letter word!")
        i = i + 1
        check1 = checkIt(pick, C1)
        doesExist(pick, C1)
        if C1 == pick:
            Winner()
            break
        if i == 7:
            break
    print(pick)
    print(check1)
    shallBegin()

def shallBegin():
    Start = input("Welcome to Wordleleler... I guess, Choose a Number From 5 - 8 to Start!! ")
    Start = Start.lower()
    if Start == ("5"):
        gameFive()
    elif Start == ("6"):
        gameSix()
    elif Start == ("7"):
        gameSeven()
    elif Start == ("8"):
        gameEight()
    elif Start == ("exit"):
        print("GOODBYE!!")
    else:
        shallBegin()

'count()'
shallBegin()





import random
import webbrowser
import cv2

Five = ['about', 'other', 'which', 'their', 'there', 'first', 'would', 'these', 'click', 'price',
        'state', 'email', 'world', 'music', 'after', 'video', 'where', 'books', 'links', 'years',
        'order', 'items', 'group', 'under', 'games', 'could', 'great', 'hotel', 'store', 'terms',
        'right', 'local', 'those', 'using', 'phone', 'forum', 'based', 'black', 'check',
        'being', 'women', 'today', 'south', 'pages', 'found', 'house', 'photo', 'power', 'while',
        'three', 'total', 'place', 'think', 'north', 'posts', 'media', 'since', 'guide', 'board',
        'white', 'small', 'times', 'sites', 'level', 'hours', 'image', 'title', 'shall', 'class',
        'still', 'money', 'every', 'visit', 'tools', 'reply', 'value', 'press', 'learn', 'print',
        'stock', 'point', 'sales', 'large', 'table', 'start', 'model', 'human', 'movie', 'march',
        'yahoo', 'going', 'study', 'staff', 'again', 'april', 'never', 'users', 'topic', 'below',
        'anime', 'stand', 'drive', 'grass', 'trees', 'doors', 'notes', 'shelf', 'truck', 'phone',
        'drill', 'alarm', 'light', 'board', 'mower', 'sport', 'chain', 'table', 'molar',
        'radio', 'house', 'paint', 'total', 'cycle', 'motor', 'first', 'third', 'fifth', 'rouge',
        'hobby', 'glove', 'towel', 'space', 'demon', 'angel', 'world', 'touch', 'cable', 'lunch',
        'feast', 'plate', 'trash', 'green', 'mauve', 'digit', 'money', 'index', 'audio', 'focus',
        'alpha', 'clear', 'media', 'steam', 'water', 'broom', 'brush', 'clean', 'power', 'sword',
        'glory', 'daisy', 'flame', 'brick', 'spicy', "boner"]

Six = ['search', 'online', 'people', 'health', 'should', 'system', 'policy', 'number', 'please', 'rights',
       'public', 'school', 'review', 'united', 'center', 'travel', 'report', 'member', 'before', 'hotels',
       'office', 'design', 'posted', 'within', 'states', 'family', 'prices', 'sports', 'county', 'access',
       'change', 'rating', 'during', 'return', 'events', 'little', 'movies', 'source', 'author', 'around',
       'course', 'canada', 'credit', 'estate', 'select', 'photos', 'thread', 'market', 'really', 'action',
       'series', 'second', 'forums', 'better', 'friend', 'server', 'issues', 'street', 'things', 'person',
       'mobile', 'offers', 'recent', 'stores', 'memory', 'social', 'august', 'create', 'single', 'latest',
       'status', 'browse', 'seller', 'always', 'result', 'groups', 'making', 'future', 'london', 'become',
       'garden', 'listed', 'energy', 'images', 'notice', 'others', 'format', 'months', 'safety', 'having',
       'common', 'living', 'called', 'period', 'window', 'france', 'region', 'island', 'record', 'direct',
       'figure', 'weapon', 'stairs', 'hunter', 'bottle', 'mantle', 'camera', 'bypass', 'active', 'engine',
       'inhale', 'second', 'fourth', 'catnip', 'create', 'gentle', 'washer', 'poison', 'advice', 'nozzle',
       'cowboy', 'outlaw', 'pirate', 'planet', 'record', 'vision', 'handle', 'pepper', 'tablet', 'screen',
       'copper', 'petrol', 'dinner', 'orange', 'purple', 'violet', 'pliers', 'basket', 'soccer', 'update',
       'native', 'bridge', 'export', 'office', 'window', 'supply', 'pencil', 'reader', 'forget', 'zinnia',
       'flower', 'please', 'retain', 'public', 'folder', 'coupon', 'ignite', 'burner', 'column', 'drawer',
       'hearth', 'spouse', 'lonely', 'doctor', 'falcon', 'fabric', 'police']

Seven = ['contact', 'service', 'product', 'support', 'message', 'through', 'privacy', 'company', 'general',
         'january', 'reviews', 'program', 'details', 'because', 'results', 'address', 'subject', 'between',
         'special', 'project', 'version', 'section', 'related', 'members', 'network', 'systems', 'without',
         'current', 'control', 'history', 'account', 'digital', 'profile', 'another', 'quality', 'listing',
         'content', 'country', 'private', 'compare', 'include', 'college', 'article', 'provide', 'process',
         'science', 'english', 'windows', 'gallery', 'however', 'october', 'library', 'medical', 'looking',
         'comment', 'working', 'against', 'payment', 'student', 'problem', 'options', 'america', 'example',
         'changes', 'release', 'request', 'picture', 'meeting', 'similar', 'schools', 'million', 'popular',
         'stories', 'journal', 'reports', 'central', 'council', 'archive', 'society', 'friends', 'edition',
         'further', 'updated', 'already', 'studies', 'several', 'display', 'limited', 'powered', 'natural',
         'whether', 'average', 'records', 'present', 'written', 'federal', 'hosting', 'tickets', 'finance',
         'minutes', 'vehicle', 'firearm', 'setting', 'roadway', 'highway', 'caution', 'recycle', 'battery',
         'surface', 'squeeze', 'contact', 'discard', 'medical', 'product', 'minimum', 'maximum', 'machine',
         'network', 'connect', 'printer', 'program', 'sawdust', 'android', 'propane', 'monitor', 'fallout',
         'digital', 'plywood', 'upgrade', 'browser', 'dolphin', 'project', 'display', 'malware', 'charger',
         'cleaner', 'measure', 'reading', 'morning', 'receipt', 'balance', 'payment', 'stapler', 'lighter',
         'burning', 'diploma', 'pathway', 'antenna', 'finally', 'husband', 'flipper', 'crimson', "arduous"]


Eight = ['business', 'services', 'products', 'software', 'research', 'comments', 'national', 'internet', 'shipping',
         'reserved', 'security', 'american', 'computer', 'download', 'pictures', 'personal', 'location', 'children',
         'students', 'shopping', 'previous', 'property', 'customer', 'december', 'training', 'advanced', 'category',
         'register', 'november', 'features', 'industry', 'provided', 'required', 'articles', 'feedback', 'complete',
         'standard', 'programs', 'language', 'password', 'question', 'building', 'february', 'analysis', 'possible',
         'problems', 'interest', 'learning', 'delivery', 'original', 'includes', 'messages', 'provides', 'specific',
         'director', 'planning', 'database', 'official', 'district', 'calendar', 'resource', 'document', 'material',
         'together', 'function', 'economic', 'projects', 'included', 'received', 'archives', 'magazine', 'policies',
         'position', 'listings', 'wireless', 'purchase', 'response', 'practice', 'hardware', 'designed', 'discount',
         'remember', 'increase', 'european', 'activity', 'although', 'contents', 'regional', 'supplies', 'exchange',
         'continue', 'benefits', 'anything', 'mortgage', 'solution', 'addition', 'clothing', 'military', 'decision',
         'division', 'shoulder', 'hibiscus', 'transfer', 'telepath', 'scramble', 'solution', 'children', 'glycerin',
         'keyboard', 'gasoline', 'windmill', 'burgundy', 'terminal', 'bookcase', 'digitize', 'scissors', 'baseball',
         'football', 'lacrosse', 'untitled', 'purified', 'computer', 'calipers', 'cucumber', 'recharge', 'purchase',
         'customer', 'pedestal', 'mushroom', 'announce', 'lifetime', 'falconer', 'shortcut']

loser = "GOOD JOB YOU LOST... WE CAN\'T WIN EM ALL AND YOU DIDN\'T WIN THIS ONE. THAT\'S OK THOUGH IT\'S JUST A GAME AND YOU CAN AND SHOULD PLAY AGAIN :D!!!"

# Word checking method to verify word length and number of words in a list.
def count(var, num):
    for i in range(0, len(var)):
        word = len(var[i])
        if word != num:
            print(var[i])
    print(len(var))

# Ran to display a win if player finds the word.
def Winner():
    print(" CONGRATULATIONS YOU WON YOU SMARTY YOU!!!")
    #webbrowser.open('https://media0.giphy.com/media/tCV2LrPPYfqCY/giphy.gif?cid=ecf05e47hx1or12u1gwpxz2ma3scbkcsdjwala489l14ayr7&ep=v1_gifs_search&rid=giphy.gif&ct=g')
    vid = cv2.VideoCapture('Media/RDJThumbs.mp4')

    if (vid.isOpened() == False):
        print("Video Fail")

    while (vid.isOpened()):
        ret, frame = vid.read()
        if ret:
            cv2.imshow('Frame', frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break
    input()
    vid.release()
    cv2.destroyAllWindows()

def Loser():
    print(loser)

# This compares the guess made to the word chosen and provides a list of letters in the right spot and slashes if not.
def checkIt(word, guess):
    checked = []
    for i in range(0, len(guess)):
        if word[i] == guess[i]:
            checked.append(guess[i])
        else:
            checked.append("/")
    print("\n")
    print("YOUR GUESS --- ", checked)

# This checks to see if a letter in the guess is in the chosen word. Returns letters that are in the word but not in the right position.
def doesExist(word, guess):
    similar = []
    for i in range(0, len(guess)):
        a = 0
        for l in word:
            if l == guess[i] and word[i] != guess[i]:
                similar.append(word[a])

            a = a + 1
    if set(similar) != set():
        print("In Wrong Position!")
        print(set(similar))


# This starts the game loop. It takes in the variable or word list and the chosen game number. Then it picks a random
# word from the numbered list and asks for up to 6 guesses.
def gameStart(variable, number):
    print(f"This is a Game of {number}")
    pick = variable[random.randint(0, len(variable))]
    count = 1
    #print(pick)
    while True:
        C1 = input(f"What is Guess {count}? ")
        if len(C1) < number or len(C1) > number:
            C1 = input(f"Please guess a {number} letter word!")
        count = count + 1
        checkIt(pick, C1)
        doesExist(pick, C1)
        if C1 == pick:
            Winner()
            break
        if count == 7:
            Loser()
            break
    final = pick.upper()
    print("\n")
    print(f"THE WORD WAS - {pick}")
    print("\n")
    #print(check1)


# This method allows a player to choose which number of letters their word has in it.
def Main():
    while True:
        Start = input("\nWelcome to Wordleleler... I guess, Choose a Number From 5 - 8 to Start!! ").lower()
        if Start == ("5"):
            gameStart(Five, 5)
        elif Start == ("6"):
            gameStart(Six, 6)
        elif Start == ("7"):
            gameStart(Seven, 7)
        elif Start == ("8"):
            gameStart(Eight, 8)
        elif Start == ("q"):
            print("GOODBYE!!")
            return
        else:
            print("Please choose a valid option!")
        

#count(Seven, 7)
Main()





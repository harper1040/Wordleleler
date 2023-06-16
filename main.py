import random
import webbrowser

Five = ['about', 'other', 'which', 'their', 'there', 'first', 'would', 'these', 'click', 'price',
        'state', 'email', 'world', 'music', 'after', 'video', 'where', 'books', 'links', 'years',
        'order', 'items', 'group', 'under', 'games', 'could', 'great', 'hotel', 'store', 'terms',
        'right', 'local', 'those', 'using', 'phone', 'forum', 'based', 'black', 'check', 'index',
        'being', 'women', 'today', 'south', 'pages', 'found', 'house', 'photo', 'power', 'while',
        'three', 'total', 'place', 'think', 'north', 'posts', 'media', 'since', 'guide', 'board',
        'white', 'small', 'times', 'sites', 'level', 'hours', 'image', 'title', 'shall', 'class',
        'still', 'money', 'every', 'visit', 'tools', 'reply', 'value', 'press', 'learn', 'print',
        'stock', 'point', 'sales', 'large', 'table', 'start', 'model', 'human', 'movie', 'march',
        'yahoo', 'going', 'study', 'staff', 'again', 'april', 'never', 'users', 'topic', 'below',
        'anime', 'stand', 'drive', 'grass', 'trees', 'doors', 'notes', 'shelf', 'truck', 'phone',
        'drill', 'alarm', 'light', 'board', 'mower', 'sport', 'chain', 'table', 'video', 'molar',
        'radio', 'house', 'paint', 'total', 'cycle', 'motor', 'first', 'third', 'fifth', 'rouge',
        'hobby', 'glove', 'towel', 'space', 'demon', 'angel', 'world', 'touch', 'cable', 'lunch',
        'feast', 'plate', 'trash', 'green', 'mauve', 'digit', 'money', 'index', 'audio', 'focus',
        'alpha', 'clear', 'media', 'steam', 'water', 'broom', 'brush', 'clean', 'power', 'sword',
        'glory', 'daisy', 'flame', 'brick', 'spicy']

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
         'burning', 'diploma', 'pathway', 'antenna', 'finally', 'husband', 'flipper', 'crimson']


Eight = ["shoulder", "hibiscus", "transfer", "telepath", "scramble", "solution", "children",
         "glycerin", "keyboard", "gasolene", "windmill", "burgandy", "terminal", "bookcase",
         "digitize", "scissors", "baseball", "football", "lacrosse", "untitled", "purified",
         "computer", "calipers", "cucumber", "recharge", "purchase", "customer", "pedestal",
         "mushroom", "announce", "lifetime", "falconer",  "shortcut"]

def count(var, num):
    for i in range(0, len(var)):
        word = len(var[i])
        if word != num:
            print(var[i])
    print(len(var))

def Winner():
    print(" CONGRATULATIONS YOU WON YOU SMARTY YOU!!!")
"""    webbrowser.open('https://media0.giphy.com/media/tCV2LrPPYfqCY/giphy.gif?cid=ecf05e47hx1or12u1gwpxz2ma3scbkcsdjwala489l14ayr7&ep=v1_gifs_search&rid=giphy.gif&ct=g')
"""
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
            if l == guess[i] and word[i] != guess[i]:
                similar.append(word[a])

            a = a + 1
    if set(similar) != set():
        print("In Wrong Position!")
        print(set(similar))


def gameStart(variable, number):
    print(f"This is Game {number}")
    pick = variable[random.randint(0, len(variable))]
    i = 1
    while True:
        C1 = input(f"What is Guess {i}? ")
        if len(C1) < number or len(C1) > number:
            C1 = input(f"Please guess a {number} letter word!")
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
        gameStart(Five, 5)
    elif Start == ("6"):
        gameStart(Six, 6)
    elif Start == ("7"):
        gameStart(Seven, 7)
    elif Start == ("8"):
        gameStart(Eight, 8)
    elif Start == ("exit"):
        print("GOODBYE!!")
    else:
        shallBegin()

'count(Seven, 7)'
shallBegin()





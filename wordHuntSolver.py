import time
import functions
import pyttsx3


engine = pyttsx3.init()
engine.setProperty("rate", 15)

n = -1
minimum = 3

printOver = 5

# udslccnttfleefib

if n == -1:
    n = 16

wordSet: set = functions.get_word_set(n, minimum)
subWordsSet = functions.generateSubWordsSet(wordSet)

board = []
letter_list = []
inp = input("Enter all letters: ")

time1 = time.time()

for ro in range(4):
    row = []
    for co in range(4):
        row.append(inp[co + 4 * ro])
        letter_list.append(inp[co + 4 * ro])
    board.append(row)

solsList = []
already_printed = []
for _ in range(n - 2):
    solsList.append([])


def move(word: str, pos: tuple, prevPositions: list):
    if word in wordSet and word not in solsList[len(word) - 3]:
        solsList[len(word) - 3].append(word)

    prevPositions.append(pos)

    # check all possible next letters that could be added to a word
    # start top left
    for r in range(3):
        r += pos[0] - 1
        for c in range(3):
            c += pos[1] - 1
            if ((r, c) not in prevPositions) and 0 <= r < 4 and 0 <= c < 4:
                # add to possibleWords
                possibleWord = word + board[r][c]
                if functions.check_possible(possibleWord, subWordsSet):
                    move(possibleWord, (r, c), prevPositions.copy())


for i in range(4):
    for j in range(4):
        move(board[i][j], (i, j), [])
    print(i + 1)

print("Time: " + str(time.time() - time1))

solsList.reverse()
print(solsList)

for solList in solsList:
    if len(solList) != 0:
        n = 0
        for sol in solList:
            if sol not in already_printed:
                n += 1
                the_word = ""
                for letter in sol:
                    the_word = the_word + letter.upper()
                print(the_word, end="")
                engine.say(the_word)
                engine.runAndWait()
                if n % 3 == 0:
                    input("\n...")
                print("")

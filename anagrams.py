import pyttsx3
import functions

engine = pyttsx3.init()
engine.setProperty("rate", 150)

n = -1

functions.get_word_list(n)

let_set = []

inp = input("Enter the letters: ")
for i in range(n):
    let_set.append(inp[i].lower())

solsList = []

for _ in range(n - 1):
    solsList.append([])


def iterate(word, rem_lets):
    if len(rem_lets) == 8:
        print("+1/9")
    if word in functions.wordList and word not in solsList[len(word) - 2]:
        solsList[len(word) - 2].append(word)

    # check if the word is still possible

    if (len(word) < n) and functions.check_possible(word, rem_lets):
        for let in rem_lets:
            temp_word = word.copy()
            temp_word.append(let)

            temp_rem_lets = rem_lets.copy()
            temp_rem_lets.remove(let)

            iterate(temp_word, temp_rem_lets)


print(let_set)
iterate([], let_set)
print("Done.")

solsList.reverse()
for solList in solsList:
    if len(solList) != 0:
        c = 0
        for sol in solList:
            c += 1
            the_word = ""
            for letter in sol:
                the_word = the_word + letter.upper()
            print(the_word, end="")
            engine.say(the_word)
            engine.runAndWait()
            if c % 5 == 0:
                input("\n...")
            print("")


import json
import os
import shutil
import functions

input("Run manipulatingFiles.py?")


def analyzeLetterFrequencies():
    letterDict = {}
    for i in range(97, 123):
        letterDict[chr(i)] = 0

    with open("hopefulFile.txt", "r") as file:
        for word in file.readlines():
            letterDict[word[0]] += 1

    print(letterDict, "\n")

    for i in range(97, 123):
        print(chr(i) + ": " + str(letterDict[chr(i)]))

    print()

    freqDict = {"a": 53000, "b": 44000, "c": 67000, "d": 43000, "e": 31000, "f": 27000, "g": 26000, "h": 34000,
                "i": 25000,
                "j": 6300, "k": 13000, "l": 23000, "m": 53000, "n": 29000, "o": 23000, "p": 70000, "q": 4300,
                "r": 36000,
                "s": 79000, "t": 40000, "u": 25000, "v": 12000, "w": 15000, "x": 1900, "y": 3500, "z": 4200}

    for i in range(97, 123):
        print(chr(i) + ": ", end="")
        for _ in range(int(letterDict[chr(i)] / 1000)):
            print("_", end="")
        print("\n" + chr(i) + ": ", end="")
        for _ in range(int(0.35 * freqDict[chr(i)] / 1000)):
            print("-", end="")
        print("")


def addWordsFromFiles():
    megaSet: set = set()
    numFiles = len(os.listdir("/Users/ryanmarshall/Downloads/Word CSV Files/"))
    counter = 0

    for fileName in os.listdir("/Users/ryanmarshall/Downloads/Word CSV Files/"):
        if fileName == ".DS_Store":
            continue

        with open("/Users/ryanmarshall/Downloads/Word CSV Files/" + fileName, "r") as file:
            wordList = file.read().split()
            if len(wordList) > 0:
                print("\r" + str(100 * counter / numFiles) + "%" + "\tFile: " + fileName + " (" + wordList[0] + ")",
                      end="")

            for rawWord in wordList:
                word = rawWord.lower()
                if functions.validWord(word, 3, 16):
                    megaSet.add(word)

            file.close()
            counter += 1

    bigWordList: list = list(megaSet)
    bigWordList.sort()

    with open("hopefulFile.txt", "w") as file:
        for word in bigWordList:
            file.write(word + "\n")
        file.close()


analyzeLetterFrequencies()

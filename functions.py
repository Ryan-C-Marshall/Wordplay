import json


def get_word_list(n, minimum) -> list:
    wordList = []
    with open("otherWordList.txt", "r") as file:
        for line in file:
            line = line[:len(line) - 1].lower()
            if n >= len(line) >= minimum:
                wordList.append(list(line))
        file.close()
    return wordList


def get_word_set(n, minimum) -> set:
    wordsSet = set()
    with open("collinsScrabbleDictionary.txt", "r") as file:
        for line in file.readlines():
            line = line[:len(line) - 1]
            if n >= len(line) >= minimum:
                wordsSet.add(line)
        file.close()

    # with open("allWords.txt", "r") as file:
    #     for line in file.readlines():
    #         line = line[:len(line) - 1].lower()
    #         if n >= len(line) >= minimum:
    #             wordsSet.add(line)
    #     file.close()

    return wordsSet


def generateSubWordsSet(wordSet: set) -> set:
    subWordsSet = set()
    for word in wordSet:
        for i in range(3, len(word) + 1):
            subWordsSet.add(word[:i])

    return subWordsSet


def check_possible(word: str, subWordsSet: set):
    return len(word) < 3 or word in subWordsSet


def validWord(word: str, minLength, maxLength) -> bool:
    blackList = [
        "<",
        ">",
        "=",
        "#",
        "-",
        "'",
        "\\",
        "/",
        "@",
        ".",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10"
    ]
    whiteList = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z"
    ]

    """
    for element in blackList:
        if element in word:
            return False
    """
    """
    for letter in word:
        if letter not in whiteList:
            return False
    """

    return minLength <= len(word) <= maxLength

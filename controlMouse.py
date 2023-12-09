import time

import pyautogui as pgi
from pynput import mouse, keyboard
from PIL import ImageGrab

TEXTBOX_X = 850
TEXTBOX_Y = 360  # 260  # 360
TEXTBOX_POS = (TEXTBOX_X, TEXTBOX_Y)

CHECKER_X = 580
CHECKER_Y = 350
CHECKER_POS = (CHECKER_X, CHECKER_Y)
CHECKER_DONE_RGB = (243, 231, 202)
CHECKER_NOT_DONE_RGB = (246, 239, 214)

SAVE_DOWNLOAD_X = 1120
SAVE_DOWNLOAD_Y = 690
SAVE_DOWNLOAD_POS = (SAVE_DOWNLOAD_X, SAVE_DOWNLOAD_Y)
SAVE_DOWNLOAD_COLOUR = (56, 125, 247)  # (56, 125, 247)  # (52, 110, 202)

OK_BUTTON_X = 950
OK_BUTTON_Y = 240
OK_BUTTON_POS = (OK_BUTTON_X, OK_BUTTON_Y)
OK_BUTTON_COLOURS = (141, 170, 226)

ERROR_X = CHECKER_X
ERROR_Y = CHECKER_Y + 20
ERROR_POS = ERROR_X, ERROR_Y
ERROR_COLOUR = (243, 231, 202)

CHECK_WORDS_X = CHECKER_X - 80
CHECK_WORDS_Y = CHECKER_Y + 50
CHECK_WORDS_POS = CHECK_WORDS_X, CHECK_WORDS_Y
WORDS_EXIST_COLOUR = (238, 228, 204)

DOWNLOAD_X = 525
DOWNLOAD_Y = 320
DOWNLOAD_POS = (DOWNLOAD_X, DOWNLOAD_Y)


def getColour(position):
    x, y = position
    box = (x, y, x + 1, y + 1)
    image = ImageGrab.grab(bbox=box)
    return image.getpixel((0, 0))[:3]


def waitForComplete():
    colour = CHECKER_NOT_DONE_RGB
    while colour != CHECKER_DONE_RGB:
        time.sleep(0.1)
        colour = getColour(CHECKER_POS)
    return True


def coloursEqual(colour1, colour2):
    for c in range(3):
        if abs(colour1[c] - colour2[c]) > 3:
            return False
    return True


def waitForColour(colour, position):
    while not coloursEqual(getColour(position), colour):
        time.sleep(0.1)
    return True


def waitForMultipleColours(colours, positions):
    while True:
        for j in range(len(colours)):
            if coloursEqual(getColour(positions[j]), colours[j]):
                return j
        time.sleep(0.1)


def addMoreChars(cList):
    cList.append("A")


def nextChar(cList):
    last = len(cList) - 1
    if cList[last] == "Z":
        cList.pop()
        nextChar(cList)
        return

    cList[last] = chr(ord(cList[last]) + 1)


for i in range(3, 0, -1):
    print(i)
    time.sleep(1)

charList = ["M", "O", "Q"]

pgi.moveTo(TEXTBOX_POS)
pgi.click()
time.sleep(1)

while charList != ["O"]:
    time1 = time.time()
    pgi.moveTo(TEXTBOX_POS)
    pgi.click()

    pgi.press("backspace", presses=(len(charList) + 1))
    pgi.write("".join(charList) + "\n")
    calmMessage = waitForMultipleColours([CHECKER_DONE_RGB, SAVE_DOWNLOAD_COLOUR], [CHECKER_POS, OK_BUTTON_POS])
    time.sleep(0.1)

    if calmMessage == 1:
        pgi.moveTo(OK_BUTTON_POS)
        time.sleep(2)
        pgi.click()
        waitForColour(CHECKER_DONE_RGB, CHECKER_POS)

    if getColour(ERROR_POS) == ERROR_COLOUR:
        if getColour(CHECK_WORDS_POS) == WORDS_EXIST_COLOUR:
            # there were more than 1000 words
            addMoreChars(charList)
        else:
            nextChar(charList)
    else:
        # only download if there are words and there are not 1000 words
        time.sleep(0.1)
        pgi.moveTo(DOWNLOAD_POS)
        pgi.click()

        waitForColour(SAVE_DOWNLOAD_COLOUR, SAVE_DOWNLOAD_POS)
        pgi.press("return")

        waitForComplete()
        nextChar(charList)

    time.sleep(max(0.0, 10 - (time.time() - time1)))

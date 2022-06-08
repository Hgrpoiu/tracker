import threading
from tkinter import *
from datetime import datetime
from win32gui import GetWindowText, GetForegroundWindow
import time
import matplotlib as mpl
import matplotlib.pyplot as plt

windict = {}
saving = False
pause = False
closing = False

root = Tk()


def logger():
    global windict
    curWin = GetWindowText(GetForegroundWindow())
    windict[curWin] = [0.0, time.time()]  # An array with total time and last time.
    # This loop will record all times within windows ASAP
    while not saving:
        last = GetWindowText(GetForegroundWindow())
        while (curWin == last):  # breakout when curWin is diff
            if (saving):
                return
            while (pause):
                print("paused")
                continue
            last = curWin
            curWin = GetWindowText(GetForegroundWindow())
        windict[last][0] += time.time() - windict[last][1]
        if curWin not in windict:
            windict[curWin] = [0, time.time()]
        else:
            windict[curWin][1] = time.time()


# Expects a dict in the specified format
# returns a string in a the following format:
# App : TotalTime
# App : TotalTime
# ... : ...
# TotalApps : TotalTime
def datForm(dict):
    ret = ""
    windows = list(windict.items())
    totalTime = 0
    for i in range(len(windict)):
        ret += windows[i][0]
        ret += " : "
        ret += str(windows[i][1][0]) + '\n'
        totalTime += windows[i][1][0]
    ret += str(i)
    ret += " : "
    ret += str(totalTime) + '\n'
    ret += str(datetime.now()) + '\n'
    return ret


def resumeC():
    print("resuming")
    global pause
    pause = False


def pauseC():
    print("pausing")
    global pause
    pause = True

def displayC():
    print("saving")
    return


def saveC():
    print("SAVING")
    global saving
    saving= True


def onClosing():
    global closing
    print("CLOSING")
    saveC()
    closing = True
    root.destroy()


def mainloop():
    global saving
    log = threading.Thread(target=logger)
    while not closing:
        log.start()
        while not saving:
            continue
        print("out of no save loop")
        log.join()
        out = open("prod.trkr", "a")
        out.write(datForm(windict))
        saving = False

if __name__ == '__main__':
    root.title("Productivity Tracker")
    label = Label(root, text="Currently Running")
    label.grid(row=0, column=1)

    dbutton = Button(root, text="Display Results", command=displayC)
    rbutton = Button(root, text="Resume", command=resumeC)
    pbutton = Button(root, text="Pause", command=pauseC)
    sbutton = Button(root, text="saveC", command=saveC)

    dbutton.grid(row=1, column=0)
    rbutton.grid(row=1, column=1)
    pbutton.grid(row=1, column=2)
    sbutton.grid(row=1, column=3)

    # Start of main processes

    mainl=threading.Thread(target=mainloop)
    root.protocol("WM_DELETE_WINDOW", onClosing)
    mainl.start()
    root.mainloop()

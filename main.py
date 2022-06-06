import threading
import tkinter as tk
from datetime import datetime
from win32gui import GetWindowText, GetForegroundWindow
import time

windict = {}
shutOff = False


def logger():
    curWin = GetWindowText(GetForegroundWindow())
    windict[curWin] = [0.0, time.time()]  # An array with total time and last time.
    # This loop will record all times within windows ASAP
    while not shutOff:
        last = GetWindowText(GetForegroundWindow())
        while (curWin == last):  # breakout when curWin is diff
            if(shutOff):
                return
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
        ret += str(windows[i][1][0]) +'\n'
        totalTime += windows[i][1][0]
    ret += str(i)
    ret += " : "
    ret += str(totalTime)+'\n'
    ret+= str(datetime.now())+'\n'
    return ret


if __name__ == '__main__':



    log = threading.Thread(target=logger, args=())
    log.start()
    while (input() != "stop"):
        continue
    #print("Stopping the run... Collecting information...")
    shutOff = True
    log.join()

    #print("Thread had joined!")
    out = open("prod.trkr", "a")
    out.write(datForm(windict))
    #print("Info dumped! Goodbye!")


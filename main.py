import threading
from win32gui import GetWindowText, GetForegroundWindow
import time

windict={}

def logger():
    curWin = GetWindowText(GetForegroundWindow())
    windict[curWin] = [0, time.time()]  # An array with total time and last time.
    # This loop will record all times within windows ASAP
    while (True):
        last == GetWindowText(GetForegroundWindow())
        while (curWin == last):  # breakout when curWin is diff
            last = curWin
            curWin = GetWindowText(GetForegroundWindow())
        windict[last][0] += time.time() - windict[1]
        if curWin not in windict:
            windict[curWin] = [0, time.time()]
        else:
            windict[curWin][1] = time.time()

#Expects a dict in the specified format
#returns a string in a the following format:
# App : TotalTime
# App : TotalTime
# ... : ...
# TotalApps : TotalTime
def datForm(dict):
    ret=""
    windows=windict.items()
    totalTime=0
    for i in range(len(windict)):
        ret+=windows[0]
        ret+=" : "
        ret+=windows[1][0]
        totalTime+=windows[1][0]
    ret+=i
    ret+=" : "
    ret+=totalTime

if __name__ == '__main__':
    log=threading.Thread(target=logger,args=())
    log.start()
    while(input!="stop"):
        continue
    log.terminate()
    out=open("prod.trkr","a")
    out.write(datForm(windict))




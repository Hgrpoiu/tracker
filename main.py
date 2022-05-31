from win32gui import GetWindowText, GetForegroundWindow
import time

windict={}
if __name__ == '__main__':
    curWin = GetWindowText(GetForegroundWindow())
    windict[curWin]=[0,time.time()]
    while(True):
        last == GetWindowText(GetForegroundWindow())
        while(curWin==last): #breakout when curWin is diff
            last=curWin
            curWin=GetWindowText(GetForegroundWindow())
        windict[last][0]+=time.time()-windict[1]
        if curWin not in windict:
            windict[curWin]=[0,time.time()]
        else:
            windict[curWin][1]=time.time()



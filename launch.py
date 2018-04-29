import sys
try:
    import launchpad_py as launchpad
except ImportError:
    try:
        import launchpad
    except ImportError:
        sys.exit("error loading launchpad.py")

lp = launchpad.Launchpad();
lp.Open()

# if lp.Open():
#     print("Launchpad Mk1/S/Mini")

buttons = [[False, False, False, False, False, False, False, False, False],
           [False, False, False, False, False, False, False, False, False],
           [False, False, False, False, False, False, False, False, False],
           [False, False, False, False, False, False, False, False, False],
           [False, False, False, False, False, False, False, False, False],
           [False, False, False, False, False, False, False, False, False],
           [False, False, False, False, False, False, False, False, False],
           [False, False, False, False, False, False, False, False, False],
           [False, False, False, False, False, False, False, False, False]]

def flush():
    lp.ButtonFlush()
    lp.Reset()
    lp.Close()

def setlight(x,y):

    if buttons[y][x] == False:
        lvl = 3
    if buttons[y][x] == True:
        lvl = 0
    lp.LedCtrlXY(x, y, 0, lvl)
    buttons[y][x] = not buttons[y][x]

# LaunchDraw
# By: Evan Pratten (ewpratten)
# http://retrylife.ca

import sys
try:
    import launchpad_py as launchpad
except ImportError:
    try:
        import launchpad
    except ImportError:
        sys.exit("error loading launchpad.py")
        
        
def main():
    cur = [0, 1]
    buttons = [[False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False],[False,False,False,False,False,False,False,False,False]]
    
    # create an instance
    lp = launchpad.Launchpad();

    if lp.Open():
        print("Launchpad Mk1/S/Mini")

    while True:
        if lp.ButtonChanged():
            prev = cur
            btn = lp.ButtonStateXY()
            cur = [btn[0],btn[1]]
            
            if prev != cur:
                buttons[btn[1]][btn[0]] = not buttons[btn[1]][btn[0]]
                print(btn[0])
                print(buttons)

        for y in range(0,9):
            for x in range(0,9):
                if buttons[y][x]:
                    lvl = 3
                else:
                    lvl = 0
                lp.LedCtrlXY(x, y, 0, lvl)

    lp.ButtonFlush()
    lp.Reset()
    lp.Close()


if __name__ == '__main__':

    main()

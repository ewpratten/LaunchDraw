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
    green = False
    red = True
    ct = False
    ct0 = False
    ct1 = False
    colch = False
    if green:
        lvl = 3
    else:
        lvl = 0

    if red:
        lvl0 = 3
    else:
        lvl0 = 0
    cur = [10, 10]
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

            if btn[0] == 2 and btn[1] == 0 and btn[2] == True:
                lp.ButtonFlush()
                lp.Reset()
                buttons = [[False, False, False, False, False, False, False, False, False],
                           [False, False, False, False, False, False, False, False, False],
                           [False, False, False, False, False, False, False, False, False],
                           [False, False, False, False, False, False, False, False, False],
                           [False, False, False, False, False, False, False, False, False],
                           [False, False, False, False, False, False, False, False, False],
                           [False, False, False, False, False, False, False, False, False],
                           [False, False, False, False, False, False, False, False, False],
                           [False, False, False, False, False, False, False, False, False]]

            if prev != cur:
                buttons[btn[1]][btn[0]] = not buttons[btn[1]][btn[0]]
                # print(btn[0])
                # print(buttons)

        if cur == [0, 0] and ct == False:
            colch = True
            ct = True
        else:
            ct = False

        if cur == [1, 0] and ct0 == False:
            colch = False
            ct0 = True
        else:
            ct0 = False






        if colch:
            green = True
            red = False
        else:
            green = False
            red = True

        for y in range(0,9):
            for x in range(0,9):
                if buttons[y][x]:
                    if green:
                        lvl = 3
                    else:
                        lvl = 0

                    if red:
                        lvl0 = 3
                    else:
                        lvl0 = 0
                else:
                    lvl = 0
                    lvl0 = 0
                lp.LedCtrlXY(x, y, lvl0, lvl)

    lp.ButtonFlush()
    lp.Reset()
    lp.Close()


if __name__ == '__main__':

    main()

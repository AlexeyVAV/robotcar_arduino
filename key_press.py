import sys, termios, tty, os, time
#test

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)

    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


button_delay = 0.2

while True:
    char = getch()
    print("Pressed:", ord(char))

    if (char == "p"):
        print("Stop!")
        exit(0)

    if (char == "a"):
        print("Left pressed")
        time.sleep(button_delay)

    elif (char == "d"):
        print("Right pressed")
        time.sleep(button_delay)

    elif (char == "w"):
        print("Up pressed")
        time.sleep(button_delay)

    elif (char == "s"):
        print("Down pressed")
        time.sleep(button_delay)

    elif (char == "1"):
        print("Number 1 pressed")
        time.sleep(button_delay)

    elif (char == "q"):
        print("Quit")
        exit(0)

    elif (ord(char) == 65):
        print("Up")

    elif (ord(char) == 66):
        print("Down")

    elif (ord(char) == 68):
        print("Left")

    elif (ord(char) == 67):
        print("Right")

    elif (ord(char) == 32):
        print("Space")

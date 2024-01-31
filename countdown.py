# !python3
# countdown.py - A simple countdown script.

import subprocess
import time

timeleft = 60  # variable called timeleft to hold the number of seconds left in the countdown.
while timeleft > 0:
    print(timeleft, end='')
    time.sleep(1)
    timeleft -= 1

# at the end of the countdown, play a sound file.
subprocess.Popen(['start', 'Break.txt'], shell=True)

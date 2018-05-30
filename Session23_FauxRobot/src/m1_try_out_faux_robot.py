"""
For trying out the faux (fake) robot.
"""

import rosebot.faux_rosebot as rb  # Using the FAUX robot.
import time
import tkinter
from tkinter import ttk

def main():
    """ Make a robot.  Connect.  Try making it do some things. """
    robot = rb.RoseBot()  # Makes a robot

    # DONE: Play around with a faux (fake) robot.
    #       Use the DOT trick to find out what you can do!
    #       Start by CONNECTING to the robot.
    #       Throughtout, for arguments provide fake data
    #          (whatever you want).

    robot.buzzer.play_tone(8)
    time.sleep(2.5)
    robot.buzzer.stop()

    root = tkinter.Tk()

    frame = ttk.Frame(root, padding=100)
    frame.grid()

    entrybutton1 = ttk.Entry(frame)
    entrybutton1.grid()

    entrybutton2 = ttk.Entry(frame)
    entrybutton2.grid()

    button1 = ttk.Button(frame, text='drive')
    button1['command'] = (lambda:drive(entrybutton1, entrybutton2, robot))
    button1.grid()

    button2 = ttk.Button(frame, text='turn on')
    button2['command'] = (lambda:robot.led.turn_on())
    button2.grid()

    button3 = ttk.Button(frame, text='turn off')
    button3['command'] = (lambda:robot.led.turn_off())
    button3.grid()

    root.mainloop()
#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------

def drive(entrybutton1, entrybutton2, robot):
    leftdrive = entrybutton1.get()
    rightdrive = entrybutton2.get()
    robot.motor_controller.drive_pwm(int(leftdrive), int(rightdrive))

if __name__ == '__main__':
    main()

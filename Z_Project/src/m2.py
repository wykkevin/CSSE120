"""
The Python Capstone Project.

CSSE 120 - Introduction to Software Development.
Team members: Chen Xiangbei, Liu Yushan, Wang Yuankai, Yang Jingjing (all of them).

The primary author of this module is: Liu Yushan.
"""
# DONE: Put the names of ALL team members in the above where indicated.
#       Put YOUR NAME in the above where indicated.

import m0
import m1
import m3
import m4

import tkinter
from tkinter import ttk
import rosebot.standard_rosebot as rb
import time
import random

class Louis():
    def __init__(self):
        self.leftwheel = 0
        self.rightwheel = 0
        self.number2 = 0
        self.entry_box1 = None
        self.entry_box2 = None
        self.speed_label = None
        self.time_label = None
def my_frame(root, dc):
    """
    Constructs and returns a   ttk.Frame   on the given root window.
    The frame contains all of this module's widgets.
    Does NOT   grid   the Frame, since the caller will do that.
    Also sets up callbacks for this module's widgets.

    The first argument is the  root  window (a tkinter.Tk object)
    onto which the   ttk.Frame  returned from this function
    will be placed.  The second argument is the shared DataContainer
    object that is CONSTRUCTED in m0 but USED in m1, m2, m3 and m4.

    Preconditions:
      :type root: tkinter.Tk
      :type dc:   m0.DataContainer
    """
    louis = Louis()
    frame2 = ttk.Frame(root, padding=100, relief='raised')


    speed_text = 'Left Wheel Speed Is {}'.format(louis.leftwheel), 'Right Wheel Speed Is {}'.format(louis.rightwheel)
    speed_label = ttk.Label(frame2, text=speed_text)
    speed_label.grid()
    louis.speed_label = speed_label

    label8 = ttk.Label(frame2)
    label8['text'] = ('type in a speed')
    label8.grid()

    entry1 = ttk.Entry(frame2, width=8)
    entry1.grid()
    louis.entry_box1 = entry1

    time_text = 'The Time Is {}'.format(louis.number2)
    time_label = ttk.Label(frame2, text=time_text)
    time_label.grid()
    louis.time_label = time_label

    label9 = ttk.Label(frame2)
    label9['text'] = ('type in a time')
    label9.grid()

    entry2 = ttk.Entry(frame2, width=8)
    entry2.grid()
    louis.entry_box2 = entry2

    button1 = ttk.Button(frame2, text='RUN As Speed and Time inputed')
    button1.grid()
    button1['command'] = (lambda:RUN(dc.robot, entry1, entry2, louis))

    button2 = ttk.Button(frame2, text='Run in Default Speed and Time')
    button2.grid()
    button2['command'] = (lambda:Reset(dc.robot, louis))

    button3 = ttk.Button(frame2, text='sing')
    button3.grid()
    button3['command'] = (lambda:Sing(dc.robot))

    root.bind_all('<Key-w>', lambda event: go_forward(dc.robot, louis))
    root.bind_all('<Key-a>', lambda event: go_left(dc.robot, louis))
    root.bind_all('<Key-d>', lambda event: go_right(dc.robot, louis))
    root.bind_all('<Key-s>', lambda event: go_backward(dc.robot, louis))
    root.bind_all('<Key-q>', lambda event: go_stop(dc.robot, louis))

    button4 = ttk.Button(frame2, text='Random Run')
    button4.grid()
    button4['command'] = (lambda:runwindow(root, dc))

    return frame2



def RUN(robot, entry1, entry2, louis):
    A = int(entry1.get())
    louis.leftwheel = A
    louis.rightwheel = A
    louis.speed_label['text'] = 'Left Wheel {}'.format(louis.leftwheel), 'Right Wheel {}'.format(louis.rightwheel)
    print('the speed is ', A)
    robot.motor_controller.drive_pwm(A, A)
    B = int(entry2.get())
    louis.number2 = B
    louis.time_label['text'] = 'The time is {}'.format(louis.number2)
    print('the time is ', B)
    time.sleep(B)
    robot.motor_controller.stop()

def Reset(robot, louis):
    louis.leftwheel = 40
    louis.rightwheel = 40
    louis.speed_label['text'] = 'Left Wheel {}'.format(louis.leftwheel), 'Right Wheel {}'.format(louis.rightwheel)
    print('the speed is ', 40)
    robot.motor_controller.drive_pwm(40, 40)
    louis.number2 = 3
    louis.time_label['text'] = 'The time is {}'.format(louis.number2)
    print('the time is ', 3)
    time.sleep(3)
    robot.motor_controller.stop()

def go_forward(robot, louis):
    louis.leftwheel = 40
    louis.rightwheel = 40
    louis.speed_label['text'] = 'Left Wheel {}'.format(louis.leftwheel), 'Right Wheel {}'.format(louis.rightwheel)
    print('the robot go forward')
    robot.motor_controller.drive_pwm(40, 40)
def go_left(robot, louis):
    louis.leftwheel = 0
    louis.rightwheel = 40
    louis.speed_label['text'] = 'Left Wheel {}'.format(louis.leftwheel), 'Right Wheel {}'.format(louis.rightwheel)
    print('the robot go left')
    robot.motor_controller.drive_pwm(0, 40)
def go_right(robot, louis):
    louis.leftwheel = 40
    louis.rightwheel = 0
    louis.speed_label['text'] = 'Left Wheel {}'.format(louis.leftwheel), 'Right Wheel {}'.format(louis.rightwheel)
    print('the robot go forward')
    robot.motor_controller.drive_pwm(40, 0)
def go_backward(robot, louis):
    louis.leftwheel = -40
    louis.rightwheel = -40
    louis.speed_label['text'] = 'Left Wheel {}'.format(louis.leftwheel), 'Right Wheel {}'.format(louis.rightwheel)
    print('the robot go forward')
    robot.motor_controller.drive_pwm(-40, -40)
def go_stop(robot, louis):
    louis.leftwheel = 0
    louis.rightwheel = 0
    louis.speed_label['text'] = 'Left Wheel {}'.format(louis.leftwheel), 'Right Wheel {}'.format(louis.rightwheel)
    print('the robot stop')
    robot.motor_controller.stop()
def Sing(robot):
    print('sing a song randomly')
    tone1 = [31, 33, 35, 36, 38, 40, 42, 43, 45, 47, 49, 50]
    jie = [0.5, 0.5, 0.25, 0.25, 0.5, 0.5, 0.5, 0.5, 0.25, 0.25, 0.25, 0.5, 0.5, 0.5, 0.25, 0.25, 0.5, 0.5, 0.5, 0.25, 0.25, 0.25, 0.5, 0.5]
    for k in range(len(jie)):
        m = random.randrange(0, len(tone1))
        robot.buzzer.play_tone(tone1[m])
        time.sleep(jie[k])
    robot.buzzer.stop()

def runwindow(root, dc):
    root2 = tkinter.Toplevel()
    frame3 = ttk.Frame(root2, padding=30)
    frame3.grid()
    label10 = ttk.Label(frame3)
    label10['text'] = ('type in proximity threshold(recommend:300)')
    label10.grid()
    entry_threshold = ttk.Entry(frame3, width=8)
    entry_threshold.grid()

    label11 = ttk.Label(frame3)
    label11['text'] = ('type in reflectance threshold(recommend:900)')
    label11.grid()
    entry_threshold1 = ttk.Entry(frame3, width=8)
    entry_threshold1.grid()

    button_run = ttk.Button(frame3, text='Run')
    button_run.grid()
    button_run['command'] = (lambda:randrun(dc.robot, entry_threshold, entry_threshold1, dc, root))


def randrun(robot, entry_threshold, entry_threshold1, dc, root):
    while True:
        threshold = int(entry_threshold.get())
        dangernumber = int(entry_threshold1.get())
        dc.robot.motor_controller.drive_pwm(random.randrange(-150, 151), random.randrange(-150, 151))
        time.sleep(1)
        if robot.sensor_reader.front_proximity_sensor.read() > threshold:
            robot.motor_controller.stop()
            break
        if robot.sensor_reader.left_proximity_sensor.read() > threshold:
            robot.motor_controller.drive_pwm(70, -50)
            time.sleep(0.5)
            break
        if robot.sensor_reader.right_proximity_sensor.read() > threshold:
            robot.motor_controller.drive_pwm(-50, 70)
            time.sleep(0.5)
            break

        if robot.sensor_reader.left_bump_sensor.read() == 0 or robot.sensor_reader.right_bump_sensor.read() == 0:
            robot.motor_controller.stop()
            break

        if robot.sensor_reader.left_reflectance_sensor.read() > dangernumber  or robot.sensor_reader.middle_reflectance_sensor.read() > dangernumber or robot.sensor_reader.right_reflectance_sensor.read() > dangernumber:
            break;

        if dc.stop == True:
            dc.robot.motor_controller.stop()
            break

        root.update()
    dc.robot.motor_controller.stop()
    print('Stop Run')

# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    m0.main()

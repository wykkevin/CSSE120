"""
The Python Capstone Project.

CSSE 120 - Introduction to Software Development.
Team members: PUT-YOUR-NAMES_HERE (all of them).

The primary author of this module is: CHEN XIANGBEI,LIU YUSHAN,WANG YUANKAI,
YANG JINGJING.
"""
# DONE: Put the names of ALL team members in the above where indicated.
#       Put YOUR NAME in the above where indicated.

import m0
import m2
import m3
import m4

import tkinter
from tkinter import ttk
import rosebot.standard_rosebot as rb
import time
import math



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

    Frame = ttk.Frame(root, padding=80)

    label2 = ttk.Label(Frame)
    label2['text'] = ('The pin')
    label2.grid()
    entry_pin = ttk.Entry(Frame, width=8)
    entry_pin.grid()

    connect_button = ttk.Button(Frame, text='connect')
    connect_button.grid()
    connect_button['command'] = (lambda:
                        connect(dc.robot, entry_pin))

#Wireless------------------------------------------------------------------------------------------
    label11 = ttk.Label(Frame)
    label11['text'] = ('The wireless pin')
    label11.grid()
    entry_wirelesspin = ttk.Entry(Frame, width=8)
    entry_wirelesspin.grid()


    wireless_connect_button = ttk.Button(Frame, text='wireless connect')
    wireless_connect_button.grid()
    wireless_connect_button['command'] = (lambda:
                        wirelessconnect(dc.robot, entry_wirelesspin))

    disconnect_button = ttk.Button(Frame, text='disconnect')
    disconnect_button.grid()
    disconnect_button['command'] = (lambda:
                        disconnect(dc.robot))

    label1 = ttk.Label(Frame)
    label1['text'] = 'The speed of the left wheel is ' + str(dc.robot.motor_controller.left_motor_pwm)
    label1.grid()

    plus_1_button = ttk.Button(Frame, text='plus 1')
    plus_1_button.grid()
    plus_1_button['command'] = (lambda:plus_1(dc.robot))

#     LED_on_button = ttk.Button(Frame, text='LED ON')
#     LED_on_button.grid()
#     LED_on_button['command'] = (lambda:robot_LDE_on(dc.robot))




#Feature4 RUN------------------------------------------------------------------------------

    label3 = ttk.Label(Frame)
    label3['text'] = ('The entry speed')
    label3.grid()
    entry_speed = ttk.Entry(Frame, width=6)


    entry_speed.grid()

    label4 = ttk.Label(Frame)
    label4['text'] = ('The entry distance')
    label4.grid()
    entry_distance = ttk.Entry(Frame, width=6)

    entry_distance.grid()

#     label5 = ttk.Label(Frame)
#     label5['text'] = ('The entry direction')
#     label5.grid()
#     entry_direction = ttk.Entry(Frame, width=6)
#     entry_direction.grid()

    RUN_button = ttk.Button(Frame, text='RUN')
    RUN_button.grid()
    RUN_button['command'] = (lambda:RUN(dc.robot, entry_speed,
                                         entry_distance))




#Feature 12-----------------------------------------------------------------

#     label12 = ttk.Label(Frame)
#     label12['text'] = ('The x-axis')
#     label12.grid()
#     entry_x = ttk.Entry(Frame, width=8)
#     entry_x.grid()
#
#     label13 = ttk.Label(Frame)
#     label13['text'] = ('The y-axis')
#     label13.grid()
#     entry_y = ttk.Entry(Frame, width=8)
#     entry_y.grid()
#
#     label14 = ttk.Label(Frame)
#     label14['text'] = ('X_X')
#     label14.grid()
#     entry_X_X = ttk.Entry(Frame, width=8)
#     entry_X_X.grid()
#
#     label15 = ttk.Label(Frame)
#     label15['text'] = ('Y_Y')
#     label15.grid()
#     entry_Y_Y = ttk.Entry(Frame, width=8)
#     entry_Y_Y.grid()

    move_to_button = ttk.Button(Frame, text='move to')
    move_to_button.grid()


    # move_to_button['command'] = (lambda:MOVE_TO1(dc.robot, entry_x, entry_y,
#                                             entry_speed, 100, 90, 60,
#                                             entry_X_X, entry_Y_Y))


    A = [60, 0, 60]
    B = [60, 0, 30]
    E = [A[0]]
    F = [B[0]]


    for k in range(len(A) - 1):
        E = E + [(A[k + 1] - A[k])]
        F = F + [(B[k + 1]) - B[k]]
    'move speed of move to2'

    C = 50

    'speed of spin'
    D = 50
    move_to_button['command'] = (lambda:MOVE_TO2(dc.robot, E, F, C, D))

#Feature21 tweet--------------------------------------------------------------

    A = [80, 80, 80, 80, 80, 80, 70, 80,
         80, 80, 80, 70, 80, 80, 80, 80, 70, 70, 80, 80, 80, 70, 70, 80, 80, 75, 79, 79, 72, 75, 80, 80, 80]
    TWEET = ttk.Button(Frame, text='TWEET')
    TWEET.grid()
    TWEET['command'] = (lambda:Tweet(dc.robot, A))

#Feature 23 fun things with camera----------------------------------------------

    fun_camera = ttk.Button(Frame, text='fun_camera')
    fun_camera.grid()
    fun_camera['command'] = (lambda:FUN_CAMERA(dc.robot))

#feature Camera----------------------------------------------------------------
#sing from file----------------------------------------------------------------
#NEW FRAME---------------------------------------------------------------------
    NEW_SPIN = ttk.Button(Frame, text='new_spin')
    NEW_SPIN.grid()
    NEW_SPIN['command'] = (lambda:newwindow(dc.robot))

    return Frame


def connect(robot, entrypin):
    '''
    :type robot:rb '''
    P = int(entrypin.get())

    robot.connector.connect(P)

def plus_1(robot):

    robot.motor_controller.left_motor_pwm = robot.motor_controller.left_motor_pwm + 1
    robot.motor_controller.right_motor_pwm = robot.motor_controller.right_motor_pwm + 1

    print('The speed is:', robot.motor_controller.left_motor_pwm)

def robot_LDE_on(robot):
    robot.led.turn_on()
    print('Robot Led On')

def RUN(robot, entryspeed, entrydistance):
    A = int(entryspeed.get())
    # C = entrydirection
    print(A)
    robot.motor_controller.drive_pwm(A, A)
    # robot.motor_controller.angle(C)
    B = abs(int(entrydistance.get()) / int(entryspeed.get()))

    time.sleep(B)
    robot.motor_controller.stop()

def disconnect(robot):
    robot.connector.disconnect()

def SPIN(robot, speed_left, speed_right, enterangle, entryradius):
    Leftspeed = int(speed_left.get())
    Rightspeed = int(speed_right.get())
    # Radius = int(entryradius.get())
    angle = int(enterangle.get())

    robot.motor_controller.drive_pwm(Leftspeed, Rightspeed)
    time1 = int(entryradius * angle / ((57.3 * Leftspeed)))
    time.sleep(time1)
    robot.motor_controller.stop()

    # /1.6  left(70) 180
    # /1  left(50) 90
    # /1.5 left(60) 360

def wirelessconnect(robot, entrywirelesspin):
    Wirelesspin = int(entrywirelesspin.get())
    robot.connector.connect_wireless(Wirelesspin)


# def MOVE_TO1(robot, X_AXIS, Y_AXIS,
#              Move_speed, spin_speed,
#              Spin_angle, Spin_radius,
#              X_X, Y_Y):
#     'Y_Y/X_X==abs(Y_AXIS,X_AXIS)'
#
#     X = int(X_AXIS.get())
#     Y = int(Y_AXIS.get())
#     xx=int(X_X.get())
#     Speed = int(Move_speed.get())
#     Angle = int(Spin_angle.get())
#     if Y > 0:
#         RUN(robot, Move_speed, Y_AXIS)
#
#         if X < 0:
#
#             robot.motor_controller.drive_pwm(-1 * spin_speed, spin_speed)
#             time_stop = int(Spin_radius * Spin_angle / (57.3 * spin_speed))
#             time.sleep(time_stop)
#             robot.motor_controller.stop()
#
#             RUN(robot, Move_speed, X_X)
#             'turn right to make head up'
#             robot.motor_controller.drive_pwm(spin_speed, -1 * spin_speed)
#             time_stop = int(Spin_radius * Spin_angle / (57.3 * spin_speed))
#             time.sleep(time_stop)
#             robot.motor_controller.stop()
#
#         if X > 0:
#             robot.motor_controller.drive_pwm(spin_speed, -1 * spin_speed)
#             time_stop1 = int(Spin_radius * Spin_angle / (57.3 * spin_speed))
#             time.sleep(time_stop1)
#             robot.motor_controller.stop()
#
#             RUN(robot, Move_speed, X_X)
#
#             'turn left to make head up'
#             robot.motor_controller.drive_pwm(-1 * spin_speed, spin_speed)
#             time_stop1 = int(Spin_radius * Spin_angle / (57.3 * spin_speed))
#             time.sleep(time_stop1)
#             robot.motor_controller.stop()
#
#
#
#     if Y < 0:
#         robot.motor_controller.drive_pwm(-1 * spin_speed, spin_speed)
#         time_stop = int(Spin_radius * 180 / (57.3 * spin_speed))
#         time.sleep(time_stop)
#         robot.motor_controller.stop()
#
#
#         RUN(robot, Move_speed, Y_Y)
#
#         if X < 0:
#
#             robot.motor_controller.drive_pwm(spin_speed, -1 * spin_speed)
#             time_stop = int(Spin_radius * Spin_angle / (57.3 * spin_speed))
#             time.sleep(time_stop)
#             robot.motor_controller.stop()
#
#             RUN(robot, Move_speed, X_X)
#             'turn right to make head up'
#             robot.motor_controller.drive_pwm(spin_speed, -1 * spin_speed)
#             time_stop = int(Spin_radius * Spin_angle / (57.3 * spin_speed))
#             time.sleep(time_stop)
#             robot.motor_controller.stop()
#
#         if X > 0:
#             robot.motor_controller.drive_pwm(-1 * spin_speed, spin_speed)
#             time_stop1 = int(Spin_radius * Spin_angle / (57.3 * spin_speed))
#             time.sleep(time_stop1)
#             robot.motor_controller.stop()
#
#             RUN(robot, Move_speed, X_X)
#
#             'turn left to make head up'
#             robot.motor_controller.drive_pwm(-1 * spin_speed, spin_speed)
#             time_stop1 = int(Spin_radius * Spin_angle / (57.3 * spin_speed))
#             time.sleep(time_stop1)
#             robot.motor_controller.stop()



#         SPIN(robot, Move_speed, Move_speed,
#              Spin_angle, Spin_radius)
#
#         RUN(robot, Move_speed, X_AXIS)
#     if X > 0:
#         SPIN(robot, Speed, (-1*Speed), Angle, 60)
#         RUN(robot, Speed, X)

    # if spin turn left spin, ldfe wheel speed be -/+ (keep in mind)


def MOVE_TO2(robot, X_list, Y_list, C, D):

    for k in range(len(X_list)):
        if Y_list[k] >= 0:
            robot.motor_controller.drive_pwm(C, C)
            Time1 = abs(Y_list[k] / C)

            time.sleep(Time1)
            robot.motor_controller.stop()

            if X_list[k] > 0:

                robot.motor_controller.drive_pwm(D, -1 * D)
                time_SPIN1 = int(60 * 3.14 / (2 * D))
                time.sleep(time_SPIN1)
                robot.motor_controller.stop()


                robot.motor_controller.drive_pwm(C, C)
                Time2 = abs(X_list[k] / C)
                time.sleep(Time2)
                robot.motor_controller.stop()

                'turn left to make head up'
                robot.motor_controller.drive_pwm(-1 * D, D)
                time_stop1 = int(60 * 3.14 / (2 * D))
                time.sleep(time_stop1)
                robot.motor_controller.stop()
#             if X_list[k] < 0:
            else:
                robot.motor_controller.drive_pwm(-1 * D, D)
                time_SPIN2 = int(60 * 3.14 / (2 * D))
                time.sleep(time_SPIN2)
                robot.motor_controller.stop()



                robot.motor_controller.drive_pwm(C, C)
                Time3 = abs(X_list[k] / C)
                time.sleep(Time3)
                robot.motor_controller.stop()

                robot.motor_controller.drive_pwm(D, -1 * D)
                time_stop2 = int(60 * 3.14 / (2 * D))
                time.sleep(time_stop2)
                robot.motor_controller.stop()

#         if Y_list[k] < 0:
        else:
            'turn the head of the robot down'
            robot.motor_controller.drive_pwm(D, -1 * D)
            time_STOP = int(60 * 3.14 / (2 * D))
            time.sleep(time_STOP)
            robot.motor_controller.stop()


            robot.motor_controller.drive_pwm(C, C)
            Time4 = abs(Y_list[k] / C)

            time.sleep(Time4)
            robot.motor_controller.stop()
            if X_list[k] > 0:

                robot.motor_controller.drive_pwm(-1 * D, D)
                time_SPIN3 = int(60 * 3.14 / (2 * D))
                time.sleep(time_SPIN3)
                robot.motor_controller.stop()

                robot.motor_controller.drive_pwm(C, C)
                Time5 = abs(X_list[k] / C)
                time.sleep(Time5)
                robot.motor_controller.stop()

                'turn left to make head up'
                robot.motor_controller.drive_pwm(-1 * D, D)
                time_stop3 = int(60 * 3.14 / (2 * D))
                time.sleep(time_stop3)
                robot.motor_controller.stop()


#             if X_list[k] < 0:
            else:

                robot.motor_controller.drive_pwm(D, -1 * D)
                time_SPIN4 = int(60 * 3.14 / (2 * D))
                time.sleep(time_SPIN4)
                robot.motor_controller.stop()


                robot.motor_controller.drive_pwm(C, C)
                Time6 = abs(X_list[k] / C)
                time.sleep(Time6)
                robot.motor_controller.stop()

                robot.motor_controller.drive_pwm(D, -1 * D)
                time_stop4 = int(60 * 3.14 / (2 * D))
                time.sleep(time_stop4)
                robot.motor_controller.stop()


def Tweet(robot, tone_of_play):

    for k in range(len(tone_of_play)):

        robot.buzzer.play_tone(tone_of_play[k])
        time.sleep(0.01)
        robot.buzzer.stop()

def FUN_CAMERA(robot):
    A = robot.camera.get_block()
    F = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80]
    if A is not None:
        B = A.x
#         C = A.y
#         D = A.height
#         E = A.width

        if B > 160:
            for k in range (len(F)):

                robot.buzzer.play_tone(k)
                time.sleep(0.3)
        if B < 160:
            for j in range (len(F) - 1, -1, -1):
                robot.buzzer.play_tone(j)
                time.sleep(0.3)


def newwindow(robot):
    root2 = tkinter.Toplevel()

    Frame2 = ttk.Frame(root2, padding=30)
    Frame2.grid()

    label6 = ttk.Label(Frame2)
    label6['text'] = ('The entry speed of left wheel')
    label6.grid()
    entry_speed_left = ttk.Entry(Frame2, width=6)
    entry_speed_left.grid()

    label7 = ttk.Label(Frame2)
    label7['text'] = ('The entry speed of right wheel')
    label7.grid()
    entry_speed_right = ttk.Entry(Frame2, width=6)
    entry_speed_right.grid()
# angel
    label8 = ttk.Label(Frame2)
    label8['text'] = ('The entry angel')
    label8.grid()
    entry_angle = ttk.Entry(Frame2, width=6)
    entry_angle.grid()

    # radius
#     label10 = ttk.Label(Frame2)
#     label10['text'] = ('The entry radius of robot')
#     label10.grid()
#     entry_radius = ttk.Entry(Frame2, width=6)
#     entry_radius.grid()

# SPIN
    SPIN_button = ttk.Button(Frame2, text='SPIN')
    SPIN_button.grid()

    SPIN_button['command'] = (lambda:SPIN(robot,
                                          entry_speed_left, entry_speed_right,
                                          entry_angle, 60))

    return Frame2


































# ----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
# ----------------------------------------------------------------------
if __name__ == '__main__':
    m0.main()

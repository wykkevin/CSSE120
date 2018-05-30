import tkinter
from tkinter import ttk
import rosebot.standard_rosebot as rb
import rosebot.command
import time


def main():
    root = tkinter.Tk()
    frame = ttk.Frame(root, padding=10)
    frame.grid()

    row = 1
    column = 1

    port = '/dev/cu.usbserial-AL00EWSO'
    port = '/dev/cu.usbserial-A012KMUK'
    port = '/dev/cu.usbserial-A9048HVI'
    port = '/dev/cu.usbserial-A9048HVD'  # R12
    port = '/dev/cu.usbserial-A9048HV2'  # R15


    robot = rb.RoseBot()

    function = lambda: connect(robot, port)
    make_button(frame, 'Connect',
                function, row, column)

    row += 1
    make_movement_buttons(frame, robot, row)

    row += 1
    make_sensor_buttons(frame, robot, row)

    row += 1
    make_button(frame, 'Blink', lambda: blink(robot), row, column)

    column += 1
    make_button(frame, 'Play tones',
                lambda: play_tones(robot), row, column)

    root.mainloop()




def make_button(frame, text, function, row, column):
    button = ttk.Button(frame, text=text)
    button['command'] = function
    button.grid(row=row, column=column)
    return button

def connect(robot, port):
    robot.connector.connect(port)

def move(robot, left_speed, right_speed, seconds):
    fstring1 = 'Testing movement at left/right speeds of {} and {}'
    fstring2 = 'Will run for {} seconds'
    print()
    print(fstring1.format(left_speed, right_speed))
    print(fstring2.format(seconds))

    robot.motor_controller.drive_pwm(left_speed, right_speed)
    time.sleep(seconds)
    robot.motor_controller.stop()

def sense(sensors):
    for sensor in sensors:
        print('{:5}'.format(sensor.read()), end='')
    print()

def blink(robot):
    print()
    print('Testing LED blink.  It should blink 4 times.')
    print('Test will start in 1 second:')
    time.sleep(1)
    for _ in range(4):
        time.sleep(0.5)
        robot.led.turn_off()
        time.sleep(0.5)
        robot.led.turn_on()

def play_tones(robot):
    print()
    print('Playing tones.')
    fstring = '{:6}'
    for k in range(1, 255, 40):
        print(fstring.format(round(4978 * k / 255)))
        robot.buzzer.play_tone(k)
        time.sleep(0.25)
        robot.buzzer.stop()
        time.sleep(0.25)
    robot.buzzer.stop()

def make_movement_buttons(frame, robot, row):
    make_button(frame, 'Go forward', lambda: move(robot, 100, 100, 2),
                row=row, column=1)
    make_button(frame, 'Go backward', lambda: move(robot, -100, -100, 2),
                row=row, column=2)
    make_button(frame, 'Spin left', lambda: move(robot, -100, 100, 2),
                row=row, column=3)
    make_button(frame, 'Spin right', lambda: move(robot, 100, -100, 2),
                row=row, column=4)

def make_sensor_buttons(frame, robot, row):
    make_button(frame, 'Bump sensors',
                (lambda:
                 sense([robot.sensor_reader.left_bump_sensor,
                        robot.sensor_reader.right_bump_sensor])),
                row=row, column=1)
    make_button(frame, 'Button sensor',
                (lambda:
                 sense([robot.sensor_reader.button_sensor])),
                row=row, column=2)
    make_button(frame, 'Reflectance sensors',
                (lambda:
                 sense([robot.sensor_reader.left_reflectance_sensor,
                        robot.sensor_reader.middle_reflectance_sensor,
                        robot.sensor_reader.right_reflectance_sensor])),
                row=row, column=3)
    make_button(frame, 'Proximity sensors',
                (lambda:
                 sense([robot.sensor_reader.left_proximity_sensor,
                        robot.sensor_reader.front_proximity_sensor,
                        robot.sensor_reader.right_proximity_sensor])),
                row=row, column=4)

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()

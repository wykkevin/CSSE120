"""
The top-level code for the "standard" RoseBot library.

CSSE 120 students should use ONLY the classes, instance variables
and methods defined in this module.  They should NOT use the low-level
modules that this library uses.  Nor should they use "private"
attributes (those that begin with an underscore) in any module.
"""

import rosebot.serial_communicator
import rosebot.socket_communicator

import sys
from enum import Enum, unique
import abc

# TODO: Maybe just use Position for this:
@unique
class MOTORS_ENCODERS(Enum):
    left_wheel = 1
    right_wheel = 2

@unique
class Position(Enum):
    left = 1
    right = 2
    front = 3
    back = 4
    front_left = 5
    front_middle = 6
    front_right = 7
    # TODO Add to the above as needed.

@unique
class ConnectionType(Enum):
    wired = 1
    wireless = 2

class Status(Enum):
    off = 0
    on = 1
    maximum_value = 255


@unique
class SensorType(Enum):
    analog = 1
    digital = 2
    reflectance = 3
    proximity = 4
    bump = 5

# TODO allow a simulation mode?


class RoseBot(object):

    def __init__(self):
        """
        Initializes a RoseBot that has:
          -- self.connector:
                    To connect/disconnect to/from a RoseBot.
          -- self.differential_drive:
                    To make the RoseBot move.
          -- self.camera:
                    To manipulate the Pixy camera and get blobs from it.
          -- self.buzzer:
                    To play tones (i.e., make noises).
          -- self.led:
                    To turn the built-in RoseBot LED on/off.
          -- self.sensors:
                    To sense the robot's environment
                    The standard sensors are:
              -- self.sensors.left_bump
              -- self.sensors.right_bump

              -- self.sensors.left_reflectance
              -- self.sensors.middle_reflectance
              -- self.sensors.right_reflectance

              -- self.sensors.left_proximity
              -- self.sensors.front_proximity
              -- self.sensors.right_proximity

              -- self.sensors.
              -- self.right_encoder
                    These return how many "ticks" the wheel has turned.
        """
        self.connector = Connector()
        self.differential_drive = DifferentialDrive(self.connector)
        self.camera = Camera(self.connector)
        self.buzzer = Buzzer(self.connector)
        self.led = LED(self.connector)
        self.sensor_reader = SensorReader(self.connector)


class Connector(object):
    """
    A Connector can connect to the RoseBot and disconnect from it.
    It also sets up the Communicator for the "under the hood"
    Python/Arduino communication.
    """
    def __init__(self):
        self._communicator = None  # Set when CONNECT runs.

    def connect(self, port=None, robot_number=None, simulate=False):
        """
        What comes in:  ONE of the following:
            -- port           -> Wired connection via that port
            -- robot_number   -> Wireless connection to the RoseBot
                               whose WiFly is labelled with that number
        What goes out:
           True if the connection was successful, else False.
        Side effects:
          -- Establishes a Communicator that is used "under the hood"
             for the Python program to send/receive messages and/or
             commands to/from the Arduino on the RoseBot.
        Examples:
            robot = rb.RoseBot()
               followed by ONE of the following:
            robot.connector.connect(port=4)           # Wired
            robot.connector.connect(robot_number=7)  # Wireless

        You can also use strings as port or robot_number, e.g.:
            robot.connector.connect(port='com4')
            robot.connector.connect(robot_number='r07')
        """
        # TODO: Add a "simulate" mode that ...

        # TODO Do error-handling in the following.

        if port is not None:
            # Wired connection.
            self.port = (port if type(port) is str else
                         'com' + str(port))
            self.connection_type = ConnectionType.wired
            self._communicator = (rosebot.serial_communicator.
                                  SerialCommunicator(self.port,
                                                     connect=True))

        elif robot_number is not None:
            # Wireless connection.
            # TODO Fix this to match whatever Valerie does
            self.robot_number = (robot_number
                                 if type(robot_number) is int else
                                 int(robot_number.
                                     replace('r0', '').
                                     replace('r', '')))
            self.connection_type = ConnectionType.wireless
            self._communicator = (rosebot.socket_communicator.
                                  SocketCommunicator(self.robot_number,
                                                     connect=True))
        else:
            pass  # TODO Deal with this case.

        print('Connected!  Robot is ready to run!')

    def connect_wired(self, port=None):
        pass
        # TODO or delete

    def connect_wireless(self, robot_number=None):
        pass
        # TODO or delete

    def disconnect(self):
        """ Disconnects from the RoseBot.  Program keeps running. """
        # TODO or delete

    def shutdown(self):
        """
        Disconnects from the RoseBot and exits the program gracefully.
        """
        # TODO or delete

    def _send_command(self, command, data):
        """ Private method to send commands to the robot. """
        self._communicator.send_command(command, data)

    def _get_result(self):
        # TODO Deal with messages that are more than a single byte.
        self._communicator.receive_message()


class RobotComponent(object):
    """
    Every RobotConnection (e.g. its LED) has a Connector
    that it can use to send its Commands to the robot.
    """
    def __init__(self, connector, abort_if_failure=False):
        self.connector = connector
        self.command = None  # Each component has its own Command(s).
        self.abort_if_failure = abort_if_failure

    def _send_command(self, command, data=None, source=None):
        is_failure = False
        try:
            self.connector._send_command(command, data)
        except AttributeError:
            is_failure = True
            if self.connector is None:
                RobotError_NoConnector(source).print_message()
        except:
            is_failure = True

        if not is_failure:
            return True
        elif self.abort_if_failure:
            raise
        else:
            return False

    def _get_result(self):
        # TODO Add error-handling.
        return self.connector._get_result()


class LED(RobotComponent):
    def __init__(self, connector):
        super().__init__(connector)

    def turn_on(self):
        """ Turns the LED fully ON. """
        self._send_command(rosebot.command.LEDCommand(), 1,
                           source='"on" method of the "LED"')

    def turn_off(self):
        """ Turns the LED fully OFF. """
        self._send_command(rosebot.command.LEDCommand(), 0,
                           source='"off" method of the "LED"')
    # CONSIDER Should this sensor do an ANALOG write,
    # in which case it could set the level of the light?
    # Then we woud have another method which sets the light
    # level to (say) a percent of maximum or (perhaps) 0 to 255.


class SensorReader(RobotComponent):
    def __init__(self, connector):
        super().__init__(connector)

        self.left_bump_sensor = BumpOrButtonSensor(Position.front_left)
        self.right_bump_sensor = BumpOrButtonSensor(Position.front_right)

        self.left_proximity_sensor = ProximitySensor(Position.left)
        self.front_proximity_sensor = ProximitySensor(Position.front)
        self.right_proximity_sensor = ProximitySensor(Position.right)

        self.left_reflectance_sensor = ReflectanceSensor(Position.front_left)
        self.middle_reflectance_sensor = ReflectanceSensor(Position.front_middle)
        self.right_reflectance_sensor = ReflectanceSensor(Position.front_right)

        self.left_encoder = Encoder(Position.left)
        self.right_encoder = Encoder(Position.right)


class Sensor(RobotComponent):

    def __init__(self, position_on_robot, sensor_type, is_analog=True):
        self.position_on_robot = position_on_robot
        self.sensor_type = sensor_type
        self.is_analog = is_analog

    def read(self):
        """ Returns the current value of this Sensor. """
        command = rosebot.command.SensorCommand(self.position_on_robot,
                                                self.sensor_type)
        source = '"read" method of {}'.format(self.sensor_type)
        self._send_command(command, source=source)

        return self._get_result()


class BumpOrButtonSensor(Sensor):
    """ A BumpOrButtonSensor can be bumped (1) or not bumped (0). """

    def __init__(self, position_on_robot):
        super().__init__(position_on_robot, 'bump')

    def is_pressed(self):
        """
        Returns True if this Bump Sensor is pressed, else returns False.
        """
        return self.read() == 0


class ProximitySensor(Sensor):
    """ A ProximitySensor returns distance: 0 (far) to 4095 (close). """

    def __init__(self, position_on_robot):
        super().__init__(position_on_robot, 'proximity')

    def distance_to_object_seen(self):
        """
        Returns a number from 0 to 4095 that indicates the distance
        that the nearest object detected by this Proximity Sensor
        is from this Proximity Sensor.
          small -> far distance
                    (i.e., the object is far from this Proximity Sensor)
          big   -> close distance
                    (i.e., the object is close to this Proximity Sensor)

        The readings depend on many factors including the physical
        characteristics of the sensor (no two are exactly alike),
        the ambient light, and more.
        """
        return self.read()


class ReflectanceSensor(Sensor):
    """ A ReflectanceSensor returns light: 0 (low) to 4095 (lots). """

    def __init__(self, position_on_robot):
        super().__init__(position_on_robot, 'reflectance')

    def reflectance_reading(self):
        """
        Returns a number from 0 to 4095 that indicates the amount
        of light that is bouncing back to this Reflectance Sensor.
          0    -> very little light is bouncing back.
          2048 -> lots of light is bouncing back.

        The readings depend on many factors including the physical
        characteristics of the sensor (no two are exactly alike),
        the ambient light, and more.
        """
        return self.read()


class DifferentialDrive(RobotComponent):
    """ A  DifferentialDrive  controls all robot movement. """

    def drive_pwm(self, left_wheel_power, right_wheel_power):
        """
        What comes in: Two integers, each between -255 and 255.
        What goes out: Nothing (i.e., None).
        Side effects:
          Makes the robot move at the given power levels, where
            -255 is full-speed backward and
             255 is full-speed forward.
        Examples (where   drive   is a DifferentialDrive object
        for a RoseBot that has established a Connection):
           drive.drive_pwm(255, 255)   [full speed forward]
           drive.drive_pwm(100, -100)  [spin clockwise in place]
           drive.drive_pwm(-50, -50)   [backwards, slowly]
           drive.drive_pwm(50, 180)    [forwards, veering to the left]
        Note: Depending on the power source, the actual pwm may
              be throttled to a smaller number than 255.
        Type hints:
          :type left_wheel_power:  int
          :type right_wheel_power: int
        """
#         self.connector._send_command(rosebot.command.MotorCommand(),
#                                      100)


    def stop(self):
        """
        What comes in: Nothing (i.e., no arguments).
        What goes out: Nothing (i.e., None).
        Side effects:  Makes the robot stop.
        Example (where   robot   is a RoseBot):
           robot.drive.stop()
        """
        self.drive_pwm(0, 0)




class Encoder(object):
    """
    An Encoder measures the rate (and hence also the distance)
    at which its associated Motor spins.

    It uses "ticks" as its units of distance, where "ticks" is a
    motor/encoder-dependent unit.

    The WheelSystem that includes this Encoder along with its
    associated Motor and the actual wheel itself could convert
    from "ticks" to centimeters per second that the wheel itself
    turned / traveled.
    """

    def __init__(self, which_encoder):
        self.which_encoder = which_encoder

#         if which_encoder == MOTORS_ENCODERS.left_wheel:
#             self.low_level_encoder = rbll.LeftWheelEncoder()
#         else:
#             self.low_level_encoder = rbll.RightWheelEncoder()

    def get_ticks(self):
        """
        Returns the number of "ticks" that this Encoder's associated
        Motor has spun since this Encoder was last reset.
        """
#         return self.low_level_encoder.get_ticks()

    def reset(self):
        """
        Resets this Encoder for purposes of further reporting
        by self.get_ticks()
        """
#         return self.low_level_encoder.reset()

    def read(self):
        """ A synonym for get_ticks. """
        return self.get_ticks()





class Camera(object):
    """
    Methods include:  get_block() and get_blocks().
    They return a PixyBlock and list of PixyBlocks, respectively.
    A PixyBlock has instance variables:  x, y, width, height,
    plus a method  size().
    """
    def __init__(self):
        # TODO
        pass


class Buzzer(object):
    """
    Methods include:
      - play_tone(n) plays tone  n  (try 220, 440 et al).
      - stop()
    """
    def __init__(self):
        pass

    def play_tone(self, note, duration_s=None):
        pass
#         super().play_tone(note, duration_s=duration_s)

    def stop(self):
        pass
#         super().stop()


class RobotError(Exception):
    default_message = """
    The error might have been caused by a bug in our code
    (if so, submit a bug report to your instuctor)
    or by a hardware failure (if so, get help as needed)
    or by something your code does wrong in using this library.
    """

    def __init__(self, message=None, output_file=sys.stderr):
        self.message = message
        self.output_file = output_file

    def print_message(self):
        print('An error has occurred in the RoseBot code.')
        if self.message :
            print(self.message)
        elif self.message is None:
            print(RobotError.default_message, file=self.output_file)


class RobotError_NoConnector(RobotError):
    def __init__(self, source=None):
        message = "I can't do the action you requested"
        if source:
            message += 'in the  ' + source + '  class'
        message += 'because this program is not currently'
        message += 'connected to a robot.  Nothing done.'

        super().__init__(message)


class RobotError_UnknownError(RobotError):
    pass


class __FreezeClass__ (type):
    """
    Students: IGNORE this class!  It just works behind the scenes
    to help you learn to use the  DataContainer  below.
    """
    def __setattr__(self, name, _):  # Value argument is unused.
        err = "You tried to set the instance variable '" + name + "'\n"
        err += "on the CLASS '" + self.__name__ + "'.\n"
        err += "You probably meant to set that instance variable\n"
        err += "on an INSTANCE of that CLASS.  Did you forget\n"
        err += "the () after to the word '" + self.__name__ + "',\n"
        err += "on the line where you CONSTRUCTED the instance?"

        raise SyntaxError(err)


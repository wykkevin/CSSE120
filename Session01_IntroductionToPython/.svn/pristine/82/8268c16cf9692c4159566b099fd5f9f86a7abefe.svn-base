"""
Demonstrates using OBJECTS via Turtle Graphics.
It is the same   m3_turtles.py   except that it organizes
the code into FUNCTIONS and then defines ADDITIONAL functions.

Concepts include:
  -- CONSTRUCT an INSTANCE of a CLASS (we call such instances OBJECTS).
  -- Make an object   ** DO **   something by using a METHOD.
  -- Reference an object's   ** DATA **   by using an INSTANCE VARIABLE.

Also:
  -- ASSIGNING a VALUE to a NAME (VARIABLE).
  -- ORGANIZING code into FUNCTIONS.
  -- MAIN as the place where execution starts.
  -- CALLING functions.

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         and their colleagues.  March 2016.
"""
########################################################################
#
# STUDENTS:  This is an EXAMPLE file.
#
# RUN it, and then note that:
#  -- The   example_from_m3   function below contains the SAME code
#       that you saw in the  m3_turtles   module.
#  -- There are several OTHER examples that you can use
#       for inspiration when you do the NEXT module.
#
# SKIM the examples, just so that you know what is in here.
# Then proceed directly to m6 where you will use code like that
# in this example to do cool, creative things with SimpleTurtles!
#
########################################################################

import rosegraphics as rg


def main():
    """ Calls the other functions in this module to demo them. """

    cool_turtle()

def cool_turtle():
    """
    Constructs a window and a SimpleTurtle and makes her
    draw a pretty shape on the window.
    Uses the variables (see below):
        size   angle   iterations
    to control the nature of the shape that it draws.

    Both of these settings make pretty pictures, as do other settings:
      size = 100     angle = 1     iterations = 360
      size = 150     angle = 20    iterations = 90
    """
    # Make the TurtleWindow.
    window = rg.TurtleWindow()

    # Make the SimpleTurtle.
    cool_turtle = rg.SimpleTurtle('turtle')
    cool_turtle.pen = rg.Pen('forest green', 5)  # Try thickness 5 too
    cool_turtle.speed = 1  # Slow

    # Move the SimpleTurtle to her starting position.
    start_at = rg.Point(100, -50)
    cool_turtle.pen_up()
    cool_turtle.go_to(start_at)
    cool_turtle.pen_down()

    # Set up some parameters that control the nature of the shape drawn.
    size = 100  # Try 150 too
    angle = 50  # Try 20 too
    iterations = 9  # Try 90 too

    # Store the animation speed (to reset it later).
    tracer_n, tracer_d = window.tracer(), window.delay()

    # Make the animation go much faster.
    #   First number:  bigger means faster.
    #   Second number: bigger means slower.
    window.tracer(1, 1)

    for _ in range(iterations):
        cool_turtle.right(angle)
        cool_turtle.draw_square(size)

    # Reset the animation to its original speed.
    window.tracer(tracer_n, tracer_d)

    window.close_on_mouse_click()

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()

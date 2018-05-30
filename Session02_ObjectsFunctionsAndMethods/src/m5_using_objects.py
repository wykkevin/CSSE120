"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Yuankai Wang.  September 2016.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    two_circles()
    circle_and_rectangle()
    lines()


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------
    window1 = rg.RoseWindow(800, 800, 'two circles')
    O1 = rg.Point(123, 456)
    O2 = rg.Point(234, 567)
    R1 = 40
    R2 = 69
    circle1 = rg.Circle(O1, R1)
    circle2 = rg.Circle(O2, R2)
    circle1.fill_color = 'magenta2'
    circle2.fill_color = 'maroon'
    circle1.attach_to(window1)
    circle2.attach_to(window1)
    window1.render()
    window1.close_on_mouse_click()


def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # ------------------------------------------------------------------
    # DONE: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------
    window2 = rg.RoseWindow(700, 700, 'yuan&juxing')

    center = rg.Point(300, 63)
    xcenter = center.x
    ycenter = center.y
    radius = 50
    circle = rg.Circle(center, radius)
    circle.fill_color = 'blue'
    circle.attach_to(window2)

    point1 = rg.Point(400, 300)
    point2 = rg.Point(200, 600)
    rectangle = rg.Rectangle(point1, point2)
    rectangle.fill_color = 'PeachPuff1'
    rectangle.attach_to(window2)
    centerofrec = rg.Point(((point1.x + point2.x) / 2), ((point1.y + point2.y) / 2))
    centerofrecx = centerofrec.x
    centerofrecy = centerofrec.y

    window2.render()
    window2.close_on_mouse_click()

    print (circle.outline_thickness)
    print (circle.fill_color)
    print (center)
    print (xcenter)
    print (ycenter)
    print (rectangle.outline_thickness)
    print (rectangle.fill_color)
    print (centerofrec)
    print (centerofrecx)
    print (centerofrecy)


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # DONE: 4. Implement and test this function.
    window3 = rg.RoseWindow(900, 900, 'lines')
    line1 = rg.Line(rg.Point(1, 899), rg.Point(800, 30))
    line2 = rg.Line(rg.Point(300, 400), rg.Point(500, 100))
    line1.thickness = 30

    line1.attach_to(window3)
    line2.attach_to(window3)

    window3.render()
    window3.close_on_mouse_click()

    cline1 = rg.Point(((1 + 800) / 2), ((899 + 30) / 2))
    cline2 = rg.Point(((300 + 500) / 2), ((400 + 100) / 2))
    print (cline1)
    print (cline1.x)
    print (cline1.y)
    print (cline2)
    print (cline2.x)
    print (cline2.y)

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()

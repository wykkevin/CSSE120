"""
PRACTICE Test 3.

This problem provides practice at:
  ***  READING FROM THE CONSOLE  ***

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Yuankai Wang.  October 2016.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

########################################################################
# Students:
#
# These problems have DIFFICULTY and TIME ratings:
#  DIFFICULTY rating:  1 to 10, where:
#     1 is very easy
#     3 is an "easy" Test 2 question.
#     5 is a "typical" Test 2 question.
#     7 is a "hard" Test 2 question.
#    10 is an EXTREMELY hard problem (too hard for a Test 2 question)
#
#  TIME ratings: A ROUGH estimate of the number of minutes that we
#     would expect a well-prepared student to take on the problem.
#
#  IMPORTANT: For ALL the problems in this module,
#    if you reach the time estimate and are NOT close to a solution,
#    STOP working on that problem and ASK YOUR INSTRUCTOR FOR HELP
#    on it, in class or via Piazza.
########################################################################


def main():
    """ Calls the   TEST   functions in this module. """
    test_console_IO()


def test_console_IO():
    """ Tests the    console_IO    function. """
    # ------------------------------------------------------------------
    # We supplied tests for this function.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   console_IO   function:')
    print('--------------------------------------------------')

    console_IO()


def console_IO():
    """
    Prompts the user for and inputs:
      -- A positive floating point number
      -- A positive integer
      -- A string
    in that order (via three separate inputs).
    Then prints, in this order, all on separate lines:
      -- The square root of the floating point number,
         repeated the input integer number of times
      -- The string, repeated the input integer number of times.
    No input validation is required.  Nothing else should be printed.

    Here is a sample run, where the user input is to the right
    of the colons:
         Enter a positive floating point number: 1.44
         Enter a positive integer: 4
         Enter a string: Peace & Love.
         1.2
         1.2
         1.2
         1.2
         Peace & Love.
         Peace & Love.
         Peace & Love.
         Peace & Love.
    """
    # ------------------------------------------------------------------
    # DONE: 2. Implement and test this function.
    #     The testing code is already written for you (above).
    # ------------------------------------------------------------------
    # ------------------------------------------------------------------
    # DIFFICULTY AND TIME RATINGS (see top of this file for explanation)
    #    DIFFICULTY:      3
    #    TIME ESTIMATE:   5 minutes.
    # ------------------------------------------------------------------

    a = float(input('Enter a positive float:'))
    b = int(input('Enter a positive integer:'))
    c = input(str('Enter a string:'))
    for _ in range (b):
        print(a ** 0.5)
    for _ in range (b):
        print(c)


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()

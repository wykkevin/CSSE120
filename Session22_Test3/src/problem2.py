"""
Test 3, problem 2.

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Yuankai Wang.  October 2016.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    test_quarter_gpa()
    test_total_gpa()
    test_highest_gpa()
    test_higher_gpa()
    test_how_many_to_pass()

class Gradebook(object):
    """
    A Gradebook holds different grades in a list organized by quarter.
    Grades are expressed on a 4 point scale, so A=4, B=3, C=2, D=1, and
    F=0.
    """
    def __init__(self, student_name):
        """
        What comes in: A string representing the name of the student
            whose grades will be in the gradebook
        What goes out: Nothing
        Side Effects: 
            --sets the variable self.contents to an empty list
            --sets the variable self.name to the given student_name
        """
        self.contents = []
        self.name = student_name

    def __repr__(self):
        """
        What comes in: Nothing
        What goes out: A string with the student's name and total gpa
        Side Effects: None
        """
        return self.name + " with GPA: " + str(self.total_gpa())


    def add(self, grades):
        """
        What comes in: A list representing a quarter to add to the
                contents of this Gradebook
        What goes out: Nothing
        Side Effects: The quarter is added to the contents of this
                Gradebook
        """
        self.contents.append(grades)

    def remove(self, quarter):
        """
        What comes in: An integer representing the quarter to be removed
        What goes out: Nothing
        Side Effects: The given quarter in the contents is removed
        """
        self.contents = self.contents[:quarter] + self.contents[quarter + 1:]

    def quarter_gpa(self, quarter):
        """
        What comes in: A quarter to calculate the GPA of. You can assume
            it is a valid number
        What goes out: The GPA of the given quarter
        Side Effects: None
        Examples: This calculates the GPA of the given quarter. You can
            assume that all classes were the same number of credit hours,
            and therefore the GPA is simply the average of the grades in
            that quarter. If there are no classes in the quarter, return
            0.
            
            So, if our Gradebook book1 contained [[4,3,4,4],[4,4,2,3],[3,2,0,4,1]],
                book1.quarter_gpa(0)    would return    3.75
                book1.quarter_gpa(1)    would return    3.25
                book1.quarter_gpa(2)    would return    2.0
        """
        # --------------------------------------------------------------
        # DONE: 2. Implement and test this function.
        #     See the testing code (below) for more examples.
        #
        # IMPLEMENTATION RESTRICTION:
        #   ** You may NOT use anything but addition (+) and division (/)
        #      do calculate the average.
        #      In particular, you may NOT use:
        #        -- the SUM operator
        #              (example:  [9, 1, 2, 3].sum() returns 15)
        #        -- anything from the math library
        # --------------------------------------------------------------

        sumquartergpa = 0
        for k in range (len(self.contents[quarter])):
            sumquartergpa = sumquartergpa + self.contents[quarter][k]
        avgquartergpa = sumquartergpa / len(self.contents[quarter])
        return avgquartergpa


    def total_gpa(self):
        """
        What comes in: Nothing
        What goes out: The GPA of the Gradebook
        Side Effects: None
        Examples: This calculates the GPA over all quarters. You can
            assume that all classes were the same number of credit hours,
            and therefore the GPA is simply the average of the grades in
            that quarter. IF THERE ARE NO GRADES IN THE GRADEBOOK it should
            return 0.
            
            So, if our Gradebook book1 contained [[4,3,4,4],[4,4,2,3],[3,2,0,4,1]],
                book1.total_gpa()    would return    a number close to 2.92
        """
        # --------------------------------------------------------------
        # DONE: 3. Implement and test this function.
        #     See the testing code (below) for more examples.
        #
        # IMPLEMENTATION RESTRICTION:
        #   ** You may NOT use anything but addition (+) and division (/)
        #      do calculate the average.
        #      In particular, you may NOT use:
        #        -- the SUM operator
        #              (example:  [9, 1, 2, 3].sum() returns 15)
        #        -- anything from the math library
        # --------------------------------------------------------------

        sumtotalgpa = 0
        avgtotalgpa = 0
        numofgpa = 0
        for k in range (len(self.contents)):
            for i in range (len(self.contents[k])):
                sumtotalgpa = sumtotalgpa + self.contents[k][i]
                numofgpa = numofgpa + 1
        if len(self.contents) != 0:
            avgtotalgpa = sumtotalgpa / numofgpa
        return avgtotalgpa

    def highest_gpa(self):
        """
        What comes in: Nothing
        What goes out: The quarter with the highest quarter GPA in the Gradebook
        Side Effects: None
        Examples: This returns the quarter with the highest GPA out of all of the
            quarters. Can assume that we have at least one quarter of data.
            
            So, if our Gradebook book1 contained [[4,3,4,4],[4,4,2,3],[3,2,0,4,1]],
                book1.highest_gpa()    would return    [4,3,4,4]
                as 3.75 is the highest gpa of all of the quarters.
        """
        # --------------------------------------------------------------
        # DONE: 4. Implement and test this function.
        #     See the testing code (below) for more examples.
        #
        # IMPORTANT: You must call the relevant functions in the class
        # for full credit.
        # --------------------------------------------------------------

        highquarter = 0
        for k in range (len(self.contents)):
            if self.quarter_gpa(k) > self.quarter_gpa(highquarter):
                highquarter = k
        return self.contents[highquarter]


    def higher_gpa(self, other_gradebook):
        """
        What comes in: Another Gradebook
        What goes out: True if this Gradebook has the same or higher total gpa,
                        False otherwise.
        Side Effects: None
        Examples: We have two Gradebooks:
                book1 contains [[4,3,4,4],[4,4,2,3],[3,2,0,4,1]],
                book2 contains [[4,3,4,4],[0,0,0,0],[3,2,0,4,1]]
                book1.higher_gpa(book2)     would return    True
                book2.higher_gpa(book1)     would return    False
                
                We have two Gradebooks:
                book1 contains [[4,3,4,4],[4,4,2,3],[3,2,0,4,1]],
                book2 contains [[4,3,4,4],[4,4,2,3],[3,2,0,4,1]]
                book1.higher_gpa(book2)     would return    True
                book2.higher_gpa(book1)     would return    True
        """
        # --------------------------------------------------------------
        # DONE: 5. Implement and test this function.
        #     See the testing code (below) for more examples.
        #
        # IMPORTANT: You must call the relevant functions in the class
        # for full credit.
        # --------------------------------------------------------------

        if self.total_gpa() >= other_gradebook.total_gpa():
            return True
        else:
            return False

    def how_many_to_pass(self, grade, threshold):
        """
        What comes in: 
            --grade: A number representing a grade on a 4 point scale
            --threshold: A number representing a threshold to pass
            Assume grade is higher than the threshold.      
        What goes out: The number of classes this student would need to get
            the given grade in in order for their total gpa to be greater
            than the threshold
        Side Effects: None
        Examples: We have a Gradebook book1 that contains [[0,0,2,1],[3,4,4,2]
                book1.total_gpa()                 returns    2
                book1.how_many_to_pass(3,2.5)     returns    8
                book1.how_many_to_pass(4,2.5)     returns    3
                book1.how_many_to_pass(4,3.5)     returns    24
        """
        # --------------------------------------------------------------
        # DONE: 6. Implement and test this function.
        #     See the testing code (below) for more examples.
        # IMPORTANT: You must use a while loop to solve this problem.
        # --------------------------------------------------------------

        numberofclass = 0
        length = 0
        for k in range (len(self.contents)):
            length = length + len(self.contents[k])
        while True:
            newgpa = (self.total_gpa() * length + numberofclass * grade) / (length + numberofclass)
            if newgpa >= threshold:
                break
            numberofclass = numberofclass + 1
        return numberofclass

def test_quarter_gpa():
    """ Tests the    quarter_gpa    function. """
    # ------------------------------------------------------------------
    # We supplied tests for this function.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   quarter_gpa   function:')
    print('--------------------------------------------------')
    book1 = Gradebook("Bobby")
    book1.add([4, 3, 4, 4])
    book1.add([4, 4, 2, 3])
    book1.add([3, 2, 0, 4, 1])
    print("Expected: ", 3.75, "Actual: ", book1.quarter_gpa(0))
    print("Expected: ", 3.25, "Actual: ", book1.quarter_gpa(1))
    print("Expected: ", 2.0, "Actual: ", book1.quarter_gpa(2))
    book1.add([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
    print("Expected: ", .1, "Actual: ", book1.quarter_gpa(3))

def test_total_gpa():
    """ Tests the    total_gpa    function. """
    # ------------------------------------------------------------------
    # We supplied tests for this function.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   total_gpa   function:')
    print('--------------------------------------------------')
    book1 = Gradebook("Bobby")
    print("Expected roughly: ", 0, "Actual: ", book1.total_gpa())
    book1.add([4, 3, 4, 4])
    book1.add([4, 4, 2, 3])
    book1.add([3, 2, 0, 4, 1])
    print("Expected roughly: ", 2.92, "Actual: ", book1.total_gpa())
    book1.add([0, 0, 0, 0, 0, 0, 0, 0, 0])
    print("Expected roughly: ", 1.72, "Actual: ", book1.total_gpa())
    book1.add([4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4])
    print("Expected roughly: ", 2.86, "Actual: ", book1.total_gpa())
    book1.add([])
    print("Expected roughly: ", 2.86, "Actual: ", book1.total_gpa())

def test_highest_gpa():
    """ Tests the    highest_gpa    function. """
    # ------------------------------------------------------------------
    # We supplied tests for this function.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   highest_gpa   function:')
    print('--------------------------------------------------')
    book1 = Gradebook("Bobby")
    book1.add([4, 3, 4, 4])
    print("Expected: ", [4, 3, 4, 4], "Actual: ", book1.highest_gpa())
    book1.add([4, 3, 4, 4, 4, 3, 4, 4])
    print("Expected: ", [4, 3, 4, 4], "Actual: ", book1.highest_gpa())
    book1.add([4, 4, 2, 3])
    print("Expected: ", [4, 3, 4, 4], "Actual: ", book1.highest_gpa())
    book1.add([3, 2, 0, 4, 1])
    print("Expected: ", [4, 3, 4, 4], "Actual: ", book1.highest_gpa())
    book1.add([4, 4, 4, 4])
    print("Expected: ", [4, 4, 4, 4], "Actual: ", book1.highest_gpa())
    book1.add([3, 2, 0, 4, 1])
    print("Expected: ", [4, 4, 4, 4], "Actual: ", book1.highest_gpa())

def test_higher_gpa():
    """ Tests the    higher_gpa    function. """
    # ------------------------------------------------------------------
    # We supplied tests for this function.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   higher_gpa   function:')
    print('--------------------------------------------------')
    book1 = Gradebook("Bobby")
    book1.add([4, 3, 4, 4])
    book1.add([4, 4, 2, 3])
    book1.add([3, 2, 0, 4, 1])
    book2 = Gradebook("Sally")
    print("Expected: ", True, "Actual: ", book1.higher_gpa(book2))
    print("Expected: ", False, "Actual: ", book2.higher_gpa(book1))
    book2.add([4, 3, 4, 4])
    print("Expected: ", False, "Actual: ", book1.higher_gpa(book2))
    print("Expected: ", True, "Actual: ", book2.higher_gpa(book1))
    book2.add([4, 4, 2, 3])
    book2.add([3, 2, 0, 4, 1])
    print("Expected: ", True, "Actual: ", book1.higher_gpa(book2))
    print("Expected: ", True, "Actual: ", book2.higher_gpa(book1))

def test_how_many_to_pass():
    """ Tests the    how_many_to_pass    function. """
    # ------------------------------------------------------------------
    # We supplied tests for this function.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   how_many_to_pass   function:')
    print('--------------------------------------------------')
    book1 = Gradebook("Bobby")
    book1.add([0, 0, 2, 1])
    book1.add([3, 4, 4, 2])
    print("Expected: ", 8, "Actual: ", book1.how_many_to_pass(3, 2.5))
    print("Expected: ", 3, "Actual: ", book1.how_many_to_pass(4, 2.5))
    print("Expected: ", 24, "Actual: ", book1.how_many_to_pass(4, 3.5))
    print("Adding a failing quarter to the Gradebook")
    book1.add([0, 0, 0, 0])
    print("Expected: ", 28, "Actual: ", book1.how_many_to_pass(3, 2.5))
    print("Expected: ", 10, "Actual: ", book1.how_many_to_pass(4, 2.5))
    print("Expected: ", 52, "Actual: ", book1.how_many_to_pass(4, 3.5))

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()

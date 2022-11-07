import unittest
from Lab3dp import *
class Test(unittest.TestCase):
    def setUp(self):
        """Setting few methods for futher testing"""
        self.assignment2= {"title": "testing", "description" : "testing", "is_done": False, "mark": 0.0}
        self.student1=Student( 'Uaroslav Holovcko','Lviv','096833','Holovcko@gmail.com', 3,)
        self.enr = Enrollment()
        self.course1 = Algorithms('Algorithms', self.assignment2,  100)
        self.course2 = Math('Not math', self.assignment2,  100)
        self.prof1 = AlgorithmsProfessor(1, 'Han', 'Solo', 1000)
        self.prof2 = MathProfessor(1, 'Michael', 'Jackson', 2300)

    def test_1(self):
        """Creating algorithms course with choosen professor"""
        test1=self.prof1.create_course(self.course1)
        self.assertEqual(test1, 'Algorithms course created by Han Solo')


    def test_2(self):
        """Trying to create course with wrong title; expecting mistake"""
        test2=self.prof2.create_course(self.course2)
        self.assertEqual(test2, 'Not math is wrong course title')

    def test_3(self):
        """Enrolling choosen student; expectiong succes enrolling"""
        test3=self.enr.enroll(self.student1.student_number, self.course1.title, self.student1, self.course1)
        self.assertEqual(test3, 'Uaroslav Holovcko has been added to the course Algorithms')

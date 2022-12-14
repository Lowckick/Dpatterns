import unittest
import lab2dpab
from lab2dpab import *
class Test_ball(unittest.TestCase):
    def setUp(self):
        self.ball = Ball(50, 50, 5, 10, 30)
        self.container = Container(0, 0, 100, 100)
    def test1(self):
        self.ball.move()
        x = self.ball.x
        y = self.ball.y
        self.assertEqual(int(y), 38)
        self.assertEqual(int(x), 61)
    def test2(self):
        self.ball.reflectY()
        self.ball.reflectH()
        gd = self.ball.getDirection()
        self.assertEqual(gd, -2)
    def test3(self):
        self.ball.reflectH()
        gd = self.ball.getDirection()
        self.assertEqual(gd, 2)
    def test4(self):
        x = self.container.collides_with(self.ball)
        self.assertEqual(x, True)
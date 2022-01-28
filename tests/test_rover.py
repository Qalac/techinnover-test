import unittest
from Rover.rover import Rover

class TestRover(unittest.TestCase):

    def setUp(self):
        self.rover = Rover(1, 2, "N")

    def test_rover_creation(self):
        self.assertEqual(self.rover.x_pos, 1)
        self.assertEqual(self.rover.y_pos, 2)
        self.assertEqual(self.rover.dir, "N")

    def test_setLeft_function(self):
        self.rover.setLeft()
        self.assertEqual(self.rover.dir, "W")
        self.rover.setLeft()
        self.assertEqual(self.rover.dir, "S")
        self.rover.setLeft()
        self.assertEqual(self.rover.dir, "E")
        self.rover.setLeft()
        self.assertEqual(self.rover.dir, "N")


    def test_setRight_function(self):
        self.rover.setRight()
        self.assertEqual(self.rover.dir, "E")
        self.rover.setRight()
        self.assertEqual(self.rover.dir, "S")
        self.rover.setRight()
        self.assertEqual(self.rover.dir, "W")
        self.rover.setRight()
        self.assertEqual(self.rover.dir, "N")
        self.rover.setRight()
        self.assertNotEqual(self.rover.dir, "S")


    def test_moveForward_function(self):
        self.rover.moveForward()
        self.assertEqual(self.rover.y_pos, 3)
        self.rover.moveForward()
        self.assertEqual(self.rover.y_pos, 4)


if __name__ == "__main__":
    unittest.main()
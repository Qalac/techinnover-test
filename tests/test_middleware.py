import unittest
from middleware.middleware import *
from Rover.rover import Rover

class TestMiddleware(unittest.TestCase):

    def setUp(self):
        self.rover = Rover(1, 3, "N")

    def test_rover_is_not_within_perimeter(self):
        with self.assertRaises(Exception) as context:
            roverIsWithinPerimeter(7, 5, 5, 5, "N")

    def test_rover_is_within_perimeter(self):
        with self.assertRaises(Exception) as context:
            roverIsWithinPerimeter(5, 5, 5, 5, "N")

    def test_rover_x_is_not_within_perimeter(self):
        with self.assertRaises(Exception) as context:
            roverIsWithinPerimeter_x(7, 5, 5, 5, "N", self.rover.position)

    def test_rover_x_is_within_perimeter(self):
        with self.assertRaises(Exception) as context:
            roverIsWithinPerimeter_x(5, 5, 5, 5, "N", self.rover.position)

    def test_rover_x_is_landing_on_rover(self):
        with self.assertRaises(Exception) as context:
            roverIsWithinPerimeter_x(1, 5, 3, 5, "N", self.rover.position)

    def test_rover_x_is_not_landing_on_rover(self):
        with self.assertRaises(Exception) as context:
            roverIsWithinPerimeter_x(2, 5, 3, 5, "N", self.rover.position)

    def test_rover_is_making_invalid_movements(self):
        with self.assertRaises(Exception) as context:
            isValidMovement(0, 3, 5, 5, "W")

    def test_rover_is_making_valid_movements(self):
        with self.assertRaises(Exception) as context:
            isValidMovement(0, 3, 5, 5, "N")


    def test_rover_x_is_making_invalid_movement(self):
        with self.assertRaises(Exception) as context:
            isValidMovement_x(1, 2, 5, 5, "N", self.rover.position)

    def test_rover_x_is_making_valid_movement(self):
        with self.assertRaises(Exception) as context:
            isValidMovement_x(1, 2, 5, 5, "E", self.rover.position)


if __name__ == "__main__":
    unittest.main()
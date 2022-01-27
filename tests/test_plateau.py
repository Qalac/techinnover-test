import unittest
from Plateau.plateau import Plateau


# Tests that a plateau is successfully created

class TestPlateau(unittest.TestCase):

    def setUp(self):
        self.plateau = Plateau(5, 5)

    def test_plateau_creation(self):
        self.assertEqual(self.plateau.x, 5)
        self.assertEqual(self.plateau.y, 5)

if __name__ == "__main__":
    unittest.main()

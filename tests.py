import unittest
from box import box


class TestBox(unittest.TestCase):
    def setUp(self):
        self.data = [
            (10, 10),
            (16, 16),
            (0, 0),
            (1, 1),
            (-1, 14)
        ]

    def test_box_drawing(self):
        self.assertEqual(box(
            self.data[0][0], self.data[0][1]),
            ("Γ--------˥\n"
             "|        |\n"
             "|        |\n"
             "|        |\n"
             "|        |\n"
             "|        |\n"
             "|        |\n"
             "|        |\n"
             "|        |\n"
             "L________┘\n"))

    def test_box_drawing2(self):
        self.assertEqual(box(
            self.data[1][0], self.data[1][1]),
            ("Γ--------------˥\n"
             "|              |\n"
             "|              |\n"
             "|              |\n"
             "|              |\n"
             "|              |\n"
             "|              |\n"
             "|              |\n"
             "|              |\n"
             "|              |\n"
             "|              |\n"
             "|              |\n"
             "|              |\n"
             "|              |\n"
             "|              |\n"
             "L______________┘\n"))

    def test_zero_box(self):
        self.assertEqual(box(self.data[2][0], self.data[2][1]), None)

    def test_one_by_one(self):
        self.assertEqual(box(self.data[3][0], self.data[3][1]), None)

    def test_negative_input(self):
        self.assertEqual(box(self.data[4][0], self.data[4][1]), None)

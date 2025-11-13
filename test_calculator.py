# import unittest
# from calculator import Calculator

# class TestCalculator(unittest.TestCase):

#     def setUp(self):
#         self.calc = Calculator()

#     def test_add(self):
#         self.assertEqual(self.calc.add(1, 2), 3)
#         self.assertEqual(self.calc.add(-1, 5), 4)

#     def test_subtract(self):
#         # expected a - b
#         self.assertEqual(self.calc.subtract(5, 3), -2)
#         self.assertEqual(self.calc.subtract(3, 5), 2)
#     # Add the following test methods to the TestCalculator class:

# if __name__ == '__main__':
#     unittest.main()


import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 5), 4)

    def test_subtract(self):
        # expected a - b
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    # def test_divide(self):
    #     # integer division
    #     self.assertEqual(self.calc.divide(10, 2), 5)
    #     self.assertEqual(self.calc.divide(9, 2), 4)  # 9 // 2 == 4
    #     self.assertEqual(self.calc.divide(0, 3), 0)
    #     with self.assertRaises(ZeroDivisionError):
    #         self.calc.divide(5, 0)

    # def test_modulo(self):
    #     self.assertEqual(self.calc.modulo(10, 3), 1)
    #     self.assertEqual(self.calc.modulo(9, 3), 0)
    #     self.assertEqual(self.calc.modulo(2, 5), 2)

if __name__ == "__main__":
    unittest.main()

import math
import unittest

def convert_value(*args):
    results = []
    for x in args:
        try:
            if isinstance(x, str):
                raise ValueError("Invalid input")
            if x >= 0:
                y = math.sqrt(x**3)
            else:
                y = math.log(abs(x))
            results.append(y)
        except ValueError:
            results.append(None)
    return results
# Васькова Алина Николаевна , варинант 5, группа 44-22-114
class ConvertValueTestCase(unittest.TestCase):
    def test_positive_values(self):
        result = convert_value(2, 4, 6)
        expected = [math.sqrt(2**3), math.sqrt(4**3), math.sqrt(6**3)]
        self.assertEqual(result, expected)

    def test_negative_values(self):
        result = convert_value(-2, -4, -6)
        expected = [math.log(abs(-2)), math.log(abs(-4)), math.log(abs(-6))]
        self.assertEqual(result, expected)

    def test_mixed_values(self):
        result = convert_value(3, -5, 0)
        expected = [math.sqrt(3**3), math.log(abs(-5)), math.sqrt(0**3)]
        self.assertEqual(result, expected)

    def test_invalid_input(self):
        result = convert_value(10, 'xyz', 7)
        expected = [math.sqrt(10**3), None, math.sqrt(7**3)]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()

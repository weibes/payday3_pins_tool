import unittest
import sys
sys.path.append('../src')
from find_pins import find_4_digit_pins

class TestFindPins(unittest.TestCase):
    
    def test_four_nums_length(self):
        self.assertEqual(len(find_4_digit_pins([1,2,3,4])),24)
    
    def test_three_nums_length(self):
        self.assertEqual(len(find_4_digit_pins([1,2,3])), 72)
    
    def test_bad_item(self):
        with self.assertRaises(TypeError) as cm:
            find_4_digit_pins('asdf')
        ex = cm.exception
        self.assertEqual()
        self.assertEqual(str(ex), 'numbers must be a list of numbers')

    def test_list_too_long(self):
        with self.assertRaises(ValueError) as cm:
            find_4_digit_pins([-1, 3, 4, 5, 5])
        ex = cm.exception
        self.assertEqual(str(ex), 'cannot have more than 4 numbers in a 4 digit pin')

if __name__ == '__main__':
    unittest.main()
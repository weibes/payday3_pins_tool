import unittest
import sys
sys.path.append('../src')
from find_pins import find_4_digit_pins

class TestFindPins(unittest.TestCase):
    
    def test_four_nums_length(self):
        self.assertEqual(len(find_4_digit_pins([1,2,3,4])),24)
    
    def test_three_nums_length(self):
        self.assertEqual(len(find_4_digit_pins([1,2,3])), 36)
    
    def test_bad_item(self):
        with self.assertRaises(TypeError) as cm:
            find_4_digit_pins('asdf')
        ex = cm.exception
        self.assertEqual(str(ex), 'numbers must be a list of numbers')

    def test_list_too_long(self):
        with self.assertRaises(ValueError) as cm:
            find_4_digit_pins([-1, 3, 4, 5, 5])
        ex = cm.exception
        self.assertEqual(str(ex), 'cannot have more than 4 numbers in a 4 digit pin')

    def test_no_dupes_4_digits(self):
        el = find_4_digit_pins([1,2,3,4])
        dupe_list = []
        print('aeiou')
        print(el)
        for i in range(len(el)):
            item = el[i]
            print(item)
            if item not in dupe_list:
                dupe_list.append(item)
            self.assertEqual(len(dupe_list), len(el))

if __name__ == '__main__':
    unittest.main()
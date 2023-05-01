
assert sum([1, 2, 3]) == 6, "Should be 6"

assert sum([1, 1, 1]) == 6, "Should be 6"


# test.py
def add(a,b):
	return a + b

print(__name__)
if __name__ == "__main__":
	print(add(1,2))


# test2.py
#import test

#print(test.add(7,6))



def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")



# trying with a tuple
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"

if __name__ == "__main__":
    test_sum()
    test_sum_tuple()
    print("Everything passed")



import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()



import unittest


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

if __name__ == '__main__':
    unittest.main()



import unittest

def reverse(s):
    return s[::-1]

class TestReverse(unittest.TestCase):

    def test_reverse(self):
        self.assertEqual(reverse('hello'), 'olleh')
        self.assertEqual(reverse(''), '')
        #self.assertEqual(reverse(123), 321)
        self.assertEqual(reverse('12345'), '54321')

if __name__ == '__main__':
    unittest.main()



import unittest

def add(x, y):
    return x + y

class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 2), 4)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(10, -5), 5)

if __name__ == '__main__':
    unittest.main()



import unittest

def find_max(nums):
    return max(nums)

class TestFindMax(unittest.TestCase):

    def test_find_max(self):
        self.assertEqual(find_max([1, 2, 3]), 3)
        self.assertEqual(find_max([10, 2, 8]), 10)
        self.assertEqual(find_max([5]), 5)
        self.assertEqual(find_max([-1, -5, -10]), -1)

if __name__ == '__main__':
    unittest.main()



import unittest

def calculate(nums, op):
    if op == '+':
        return sum(nums)
    elif op == '*':
        result = 1
        for n in nums:
            result *= n
        return result
    else:
        raise ValueError('Invalid operator')

class TestCalculate(unittest.TestCase):

    def test_calculate_add(self):
        self.assertEqual(calculate([1, 2, 3], '+'), 6)
        self.assertEqual(calculate([-1, 2, -3], '+'), -2)

    def test_calculate_multiply(self):
        self.assertEqual(calculate([1, 2, 3], '*'), 6)
        self.assertEqual(calculate([1, -2, 3], '*'), -6)

    def test_calculate_invalid_operator(self):
        with self.assertRaises(ValueError):
            calculate([1, 2, 3], '-')
        with self.assertRaises(ValueError):
            calculate([1, 2, 3], 'invalid')

if __name__ == '__main__':
    unittest.main()



import unittest
import re

def email_validator(email):
    if len(email) > 7:
        if re.match(r'^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$', email) != None:
            return True
    return False

class TestEmailValidator(unittest.TestCase):

    def test_email_validator_valid(self):
        self.assertTrue(email_validator('test@example.com'))
        self.assertTrue(email_validator('test+123@example.com'))
        self.assertTrue(email_validator('test_123@example.co.uk'))

    def test_email_validator_invalid(self):
        self.assertFalse(email_validator('test'))
        self.assertFalse(email_validator('test@'))
        self.assertFalse(email_validator('test@example'))
        self.assertFalse(email_validator('test@example.'))

if __name__ == '__main__':
    unittest.main()

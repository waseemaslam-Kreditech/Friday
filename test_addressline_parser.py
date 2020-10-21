"""
Unit test module
"""
import unittest
from address_parser.addressline_parser import AddressParser


class TestStringMethods(unittest.TestCase):
    """
    Unit test class
    """
    def setUp(self):
        """create an instance of AddressParser class"""
        self.address_parser = AddressParser()

    def test_correct_parsing(self):
        """Test correct parsing of addresses samples"""
        result = self.address_parser.parse('15, M. A. Jinnah Road')
        self.assertTrue(result[0], '15')
        self.assertTrue(result[1], 'M. A. Jinnah Road')
        result2 = self.address_parser.parse('Nezábudková 3084/25')
        self.assertTrue(result2[0], '3084/25')
        self.assertTrue(result2[1], 'Nezábudková')
        result3 = self.address_parser.parse('Calle 39 No 1540')
        self.assertTrue(result3[0], 'No 1540')
        self.assertTrue(result3[1], 'Calle 39')

    def test_incorrect_parsing(self):
        """Test some failing parsing cases"""
        self.assertRaises(ValueError, self.address_parser.parse, 'Python programming language')
        self.assertRaises(AssertionError, self.address_parser.parse, 1)
        self.assertRaises(AssertionError, self.address_parser.parse, True)
        self.assertRaises(ValueError, self.address_parser.parse, '1')
        self.assertRaises(AssertionError, self.address_parser.parse, ['15, M. A. Jinnah Road'])

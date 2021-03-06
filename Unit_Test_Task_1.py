#Test case for string methods
import unittest
from String_Methods_Application import string_methods_application

class TestStringMethods(unittest.TestCase):

    #Unit Test of Task_1
    #Test passes when the first letter of the string is converted to capital letter.    
    def test_capitalize_string(self):
        output = string_methods_application.capitalize_string("software testing")
        self.assertEqual(output, "Software testing")

    #Test passes if it returns true when start value is a specified value   
    def test_startswith_string(self):
        output = string_methods_application.startswith_string("Software Testing.")
        self.assertTrue(output)

    #Unit Test of Task_2
    #Test passes when the old string is replaced with new string
    def test_replace_string(self):
        output = string_methods_application.replace_string("software testing")
        self.assertEqual(output, "unit testing")

    #Test passes if all the letters are in lowercase
    def test_islower_string(self):
        output = string_methods_application.islower_string("software testing")
        self.assertTrue(output)


    #Unit Test of Task_3
    #Test passes if it converts all the uppercase to lowercase
    def test_casefold_string(self):
        output = string_methods_application.casefold_string("SOFTWARE TESTING.")
        self.assertEqual(output, "software testing.")

    #Test passes if it returns true when the end value is a specified value
    def test_endswith_string(self):
        output = string_methods_application.endswith_string("Software Testing.")
        self.assertTrue(output, ".")

    


#Test case for string methods
import unittest
from String_Methods_Application import string_methods_application

class TestStringMethods(unittest.TestCase):

    #Integration Test of Task_1
    #Integrating islower and replace string methods
    def test_integration_Task_1(self):
        output = string_methods_application.startswith_string(string_methods_application.capitalize_string("software tesing."))
        self.assertTrue(output)
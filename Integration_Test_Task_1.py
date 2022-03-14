#Test case for string methods
import unittest
from String_Methods_Application import string_methods_application

class TestStringMethods(unittest.TestCase):

    #Integration Test of Task_1
    #Integrating islower and replace string methods
    def test_integration_Task_1(self):
        output = string_methods_application.startswith_string(string_methods_application.capitalize_string("software tesing."))
        self.assertTrue(output)

    #Integration Test of Task_2
    #integrating startswith and capitalize string methods
    def test_integration_Task_2(self):
        output = string_methods_application.islower_string(string_methods_application.replace_string("software testing"))
        self.assertTrue(output)

    #Integration Test of Task_3    
    #Integrating endswith and casefold string methods
    def test_integration_Task_3(self):
        output = string_methods_application.endswith_string(string_methods_application.casefold_string("SOFTWARE TESTING."))
        self.assertTrue(output, ".")

    #Integration Test of Task_4
    #Integrating count and title string methods
    def test_integration_Task_4(self):
        output = string_methods_application.count_string(string_methods_application.title_string("software tesing."))
        self.assertTrue(output, 1)


#string methods in python
class string_methods_application:

    #Task_1
    #Converts the first letter of the string to capital letter.
    def capitalize_string(my_string):
        return my_string.capitalize()

    #Returns true if the start value is a specified value    
    def startswith_string(my_string):
        return my_string.startswith("Software")

    #Task_2
    #Retruns true if all the letters are in lowercase
    def islower_string(my_string):
        return my_string.islower()

    #Replaces the old string with new string
    def replace_string(my_string):
        return my_string.replace("software", "unit")    

    #Task_3
    #Converts all the uppercase to lowercase
    def casefold_string(my_string):
        return my_string.casefold()

    #Returns true if the end value is a specified value
    def endswith_string(my_string):
        return my_string.endswith(".")
    
    #Task_4
    #Converts string into a title form
    def title_string(my_string):
        return my_string.title()   

    #Counts and returns the specific value in a given string
    def count_string(my_string):
        return my_string.count("Software")

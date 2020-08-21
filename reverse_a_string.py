import pytest

# function to reverse string without 'reverse' method
def reverse_string1(str):
    return_list = []
    str_list = list(str)
    for item in str_list:
        return_list.insert(0,item)
    return ''.join(return_list)  # Joins the contents of the array to an empty string

# function to reverse a string using the 'reverse' method
def reverse_string2(str):
    str_list = list(str)
    str_list.reverse()
    return ''.join(str_list)

# reverse a string ignoring spcial characters
def reverse_string3(str):
    spec_chars = ['!','@','#','$','%','&','^','*']
    temp = []
    str_list = list(str)                         # Coverts the string to a list
    for i, char in enumerate(str_list,start=0):
        if not char in spec_chars:               # Check to see if the char is 'sepcial'
            temp.insert(0,char)                  # inserts letter in temp array
            str_list[i] = ''                     # replaces the char with ''
    
    # Takes the temp list and replaces all ''s with the chars backwards.
    for char in temp:
        for x in range(0,len(str_list)):
            if not str_list[x]:
                str_list[x] = char
                break
    
    return ''.join(str_list)                    # returns the str_list joined into a string



# Tests for each of the functions

# Test for reverse_str1
def test_reverse_string1():
    assert reverse_string1('Brian') == 'nairB'

# Test for reverse_str2
def test_reverse_string2():
    assert reverse_string2('Brian') == 'nairB'

def test_reverse_string3():
    assert reverse_string3('#Bri$an&&') == '#nai$rB&&'


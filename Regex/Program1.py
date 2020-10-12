import re


# 1. Write a Python program to check that a string contains only a certain set of characters
# (in this case a-z, A-Z and 0-9).
def check_string(string):
    regex = re.compile(r'[^a-zA-Z0-9.]')
    string = regex.search(string)
    return not bool(string)

# print(check_string("ABCabc012"))
# print(check_string("@#$%^&*"))


# 2. Write a Python program that matches a string that has an a followed by zero or more b's.
def check_string1(string):
    regex = re.compile(r'[ab*?]')
    if regex.search(string):
        return "Match Found!"
    else:
        return "Match not Found!"
# print(check_string1("abc"))
# print(check_string1("c"))

#3. Write a Python program that matches a string that has an a followed by one or more b's.

def check_string2(string):
    regex ='ab+?'
    if re.search(regex,string):
        return "Found"
    else:
        return "Not Found"
# print(check_string2("abc"))
# print(check_string2("bc"))

#4. Write a Python program that matches a string that has an a followed by zero or one 'b'.
def check_string3(string):
    regex = 'ab?'
    if re.search(regex, string):
        return "Found"
    else:
        return "Not Found"
# print(check_string3("abc"))
# print(check_string3("bc"))

#5. Write a Python program that matches a string that has an a followed by three 'b'.
def check_string4(string):
    regex = 'ab{3}?'
    if re.search(regex,string):
        return "Found"
    else:
        return "Not Found"
# print(check_string4("abbbc"))
# print(check_string4("abbccc"))
# print(check_string4("abc"))

#6. Write a Python program that matches a string that has an a followed by two to three 'b'.
def check_string5(string):
    regex = 'ab{2,3}?'
    if re.search(regex, string):
        return "Found"
    else:
        return "Not Found"
# print(check_string5("abbbc"))
# print(check_string5("abbccc"))
# print(check_string5("abc"))

#7. Write a Python program to find sequences of lowercase letters joined with a underscore.
def check_string6(string):
    regex = '^[a-z]+_[a-z]+$'
    if re.search(regex, string):
        return "Found"
    else:
        return "Not Found"
# print(check_string6("abc_abc"))
# print(check_string6("a_c"))
# print(check_string6("12_ab"))

#8. Write a Python program to find the sequences of one upper case letter followed by lower case letters.
def check_string7(string):
    regex = '^[a-z]+[a-z]+$'
    if not re.search(regex, string):
        return "Found"
    else:
        return "Not Found"
print(check_string7("aabcbbbc"))
print(check_string7("aabAbbbc"))
print(check_string7("Aaab_abbbc"))

#9. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

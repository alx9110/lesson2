""" task 2 """

def string_comparsion(str1, str2):
    """ eq """
    if str1 == str2:
        return 1
    elif str1 != str2 and len(str1) > len(str2):
        return 2
    elif str1 != str2 and str2 == 'learn':
        return 3
    return None

str1 = input('Input, first string: ')
str2 = input('Input, second string: ')
print(string_comparsion(str1, str2))

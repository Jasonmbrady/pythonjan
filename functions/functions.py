from gettext import NullTranslations


# def subtract_nums(a, b = 10):
#     print(type(a))
#     print(a-b)
#     return True

# x = subtract_nums(5, b = 7) 

# print(x)

my_string = "Hello"
def add_to_str(str, added_str):
    str += added_str
    return str

new_string = add_to_str(my_string, ", World!")
print(new_string)
print(my_string)
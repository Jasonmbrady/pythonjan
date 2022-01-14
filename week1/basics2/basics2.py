def countdown(num):
    num_list = []
    for x in range(num, -1, -1):
        num_list.append(x)
    return num_list

print(countdown(5))

def print_and_return(two_num_list):
    print(two_num_list[0])
    return two_num_list[1]

print_and_return([1,2])

def first_plus_length(num_list):
    return num_list[0] +  len(num_list)

# Takes in a list of int. returns a new list of int
# check old list [1]. compare each value to it. 
# new list contains only those > old list [1]
# if len(old list) < 2, return False

def vals_greater_than_second(num_list):
    if len(num_list) < 2:
        return False
    else:
        second_num = num_list[1]
        new_list = []
        for num in num_list:
            if num > second_num:
                new_list.append(num)
        return new_list

print(vals_greater_than_second([9, 3, 4, 6, 2, 1, 8]))
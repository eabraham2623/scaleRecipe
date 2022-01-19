import math

input_string = input('Enter recipe measurements: ')
print("\n")
user_list = input_string.split()

input_percent = input('Enter percent: ')
factor_number = int(input_percent)

# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = int(user_list[i])

# convert each item to int type
for i in range(len(user_list)):
    # convert each item to int type
    user_list[i] = user_list[i] * (factor_number/100)
    user_list[i] = math.ceil(user_list[i])


print('Scaled Recipe: ', user_list)


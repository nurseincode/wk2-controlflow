is_raining = False

# if is_raining:
#     print("Carry an umbrella")
# else:
#     print('No need for an umbrella')
# print('The end!')

# Ternary expression -> Short way to write an if-else statement above

# print('I need and umbrella') if is_raining else print('No need for an umbrella')
print('I need and umbrella' if is_raining else 'No need for an umbrella') # Same


# --> Else if

# 90 – 100 ->HD
# 80 – 89 ->D
# 70 – 79 ->C
# 60 – 69 ->P
# Below 60 ->F 

# marks = int(input('Enter your marks (0-100):'))
# if marks >= 90:
#     print('HD')
# elif marks >= 80:
#     print('D')
# elif marks >= 70:
#     print('C')
# elif marks >= 60:
#     print('P')
# else:
#     print('F')

# age = 10

# if age >= 18:
#     print('You are an adult')
# elif age >= 13:
#     print('You are a teenager')
# else:
#     print('You are a child')

# day_of_week = 10

# # if day_of_week == 1:
# #     print('Monday')
# # elif day_of_week == 2:
# #     print('Tuesday')

# # match day_of_week: # Alternative construct, more clear
# #     case 1:
# #         print('Monday')
# #     case 2:
# #         print('Tuesday')
# #     case 3: 
# #         print('Wednesday')
# #     case 4:
# #         print('Thursday')
# #     case 5:
# #         print('Friday')
# #     case _: # Default case
# #         print('That is not a weekday!')

# # 1-5: Weekday
# # 6, 7: Weekend
# # Anything else: Error message
# match day_of_week:
#     case 1 | 2 | 3 | 4 | 5: # multiple cases with OR operator
#         print('Weekday')
#     case 6 | 7:
#         print('Weekend')
#     case _:
#         print('Error: Not a valid day number!')
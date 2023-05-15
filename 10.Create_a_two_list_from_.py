# Exercise 10: Create a new list from a two list using the following condition

# Create a new list from a two list using the following condition

# Given a two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

# Show Hint
# Create an empty list named result_list
# Iterate first list using a for loop
# In each iteration, check if the current number is odd number using num % 2 != 0 formula. If the current number is an odd number, add it to the result list
# Now, Iterate the first list using a loop.
# In each iteration, check if the current number is odd number using num % 2 == 0 formula. If the current number is an even number, add it to the result list
# print the result list

def merge_list(list1, list2):
    result_list = []

    # iterate first list
    for num in list1:
        # check if current number is odd
        if num % 2 != 0:
            # add odd number to result list
            result_list.append(num)

    # iterate second list
    for num in list2:
        # check if current number is even
        if num % 2 == 0:
            # add even number to result list
            result_list.append(num)
    return result_list


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("result list:", merge_list(list1, list2))

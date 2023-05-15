# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

# Show Hint
# Create a variable called previous_num and assign it to 0
# Iterate the first 10 numbers one by one using for loop and range() function
# Next, display the current number (i), previous number, and the addition of both numbers in each iteration of the loop. At last, change the value previous number to current number ( previous_num = i).

print("Printing current and previous number and their sum in a range(10)")
previous_num = 0

# loop from 1 to 10
for i in range(1, 11):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
    # modify previous number
    # set it to the current number
    previous_num = i

    
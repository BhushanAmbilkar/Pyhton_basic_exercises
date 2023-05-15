# Exercise 9: Check Palindrome Number
# Write a program to check if the given number is a palindrome number.
#
# A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers

# Show Hint
# Reverse the given number and save it in a different variable
# Use the if condition to check if the original number and reverse number are the same. If yes, return True.

def palindrome(number):
    print("original number", number)
    original_num = number

    # reverse the given number
    reverse_num = 0
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        number = number // 10

    # check numbers
    if original_num == reverse_num:
        print("Given number palindrome")
    else:
        print("Given number is not palindrome")


palindrome(121)
palindrome(125)

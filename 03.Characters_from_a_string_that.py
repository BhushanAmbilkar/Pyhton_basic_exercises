# Exercise 3: Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.
#
# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
#
# Show Hint
# Use Python input() function to accept a string from a user.
# Calculate the length of string using the len() function
# Next, iterate each character of a string using for loop and range() function.
# Use start = 0, stop = len(s)-1, and step =2. the step is 2 because we want only even index numbers
# in each iteration of a loop, use s[i] to print character present at current even index number


# Solution 01:

# accept input string from a user
word = input('Enter word ')
print("Original String:", word)

# get the length of a string
size = len(word)

# iterate a each character of a string
# start: 0 to start with first character
# stop: size-1 because index starts with 0
# step: 2 to get the characters present at even index like 0, 2, 4
print("Printing only even index chars")
for i in range(0, size - 1, 2):
    print("index[", i, "]", word[i])


# Solution 2: Using list slicing

# accept input string from a user
word = input('Enter word ')
print("Original String:", word)

# using list slicing
# convert string to list
# pick only even index chars
x = list(word)
for i in x[0::2]:
    print(i)




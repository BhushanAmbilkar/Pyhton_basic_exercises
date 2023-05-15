# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

# Show Hint
# Create a function that will take two numbers as parameters
# Next, Inside a function, multiply two numbers and save their product in a product variable
# Next, use the if condition to check if the product >1000. If yes, return the product
# Otherwise, use the else block to calculate the sum of two numbers and return it.

def multiplication_or_sum(num1, num2):
    # calculate product of two number
    product = num1 * num2
    # check if product is less then 1000
    if product <= 1000:
        return product
    else:
        # product is greater than 1000 calculate sum
        return num1 + num2

# first condition
result = multiplication_or_sum(20, 30)
print("The result is", result)

# Second condition
result = multiplication_or_sum(40, 30)
print("The result is", result)



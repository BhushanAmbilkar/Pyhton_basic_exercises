# Exercise 13: Print multiplication table form 1 to 10

# Show Hint
# Create the outer for loop to iterate numbers from 1 to 10. So total number of iteration of the outer loop is 10.
# Create a inner loop to iterate 10 times.
# For each iteration of the outer loop, the inner loop will execute ten times.
# In the first iteration of the nested loop, the number is 1. In the next, it 2. and so on till 10.
# In each iteration of an inner loop, we calculated the multiplication of two numbers. (current outer number and curent inner number)

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print("\t\t")


# Multiplication table (from 1 to 10) in Python_________

# num = int(input("Display multiplication table of? "))
#
# # Iterate 10 times from i = 1 to 10
# for i in range(1, 11):
#    print(num, 'x', i, '=', num*i)

# Sum of natural numbers up to num

# num = int(input("Sum of Natural numbers: "))
#
# if num < 0:
#    print("Enter a positive number")
# else:
#    sum = 0
#    # use while loop to iterate until zero
#    while(num > 0):
#        sum += num
#        num -= 1
#    print("The sum is", sum)

# Display the powers of 2 using anonymous function

terms = int(input("Enter a Number: "))

result = list(map(lambda x: 2 ** x, range(terms)))

print("The total terms are:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])
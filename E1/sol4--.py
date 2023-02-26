# we have 4 number lets call them a,b,c,d by order
# we want to print two value as sperated by comma like True,False or False,True
# the first value is the result if a is less and equal to b
# the second value is the result if d is greater to c
# inputs can be any integer number or float number

a = float(input("Enter your first number: "))
b = float(input("Enter your second number: "))
c = float(input("Enter your third number: "))
d = float(input("Enter your fourth number: "))

print("The result is:", end =" ")
print( a <= b , d > c , sep = ",")

# Fix the code to working as we expect
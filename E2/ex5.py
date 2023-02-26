# write a code that get a number from user as a
# if the number is even print "even"
# if the number is odd print "odd"
# you should not use any if statement in this code
# only operators and string manipulation is allowed

a = int(input("Enter a number: "))

even_odd = "evenodd "
print(even_odd[a % 2 * 4 : a % 2 * 4 + 4])
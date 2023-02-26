# get a range from with two input that is start and end
# end will be included in the range
# then get three input and print for each of them after each input
# if the input is in the range print True else print False

start_val = float(input("Enter your range start value: "))
end_val = float(input("Enter your range end value: "))
a = float(input("Enter a number: "))
print(a >= start_val and a <= end_val)
b = float(input("Enter a number: "))
print(b <= end_val and b >= start_val)
c = float(input("Enter a number: "))
print(c <= end_val and c >= start_val)

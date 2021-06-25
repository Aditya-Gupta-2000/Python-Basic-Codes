# Python program to print positive Numbers in a List
# (1)
# list of numbers
list1 = [12, -7, 5, 64, -14]
num1 = 0

# using while loop
while(num1 < len(list1)):

	# checking condition
	if list1[num1] >= 0:
		print(list1[num1], end = " ")

	# increment num
	num1 += 1
print("  \n   ")
#(2)
list2 = [-12, -14, 95, 3]
num2 = 0

# using while loop
while(num2 < len(list2)):

	# checking condition
	if list2[num2] >= 0:
		print(list2[num2], end = " ")

	# increment num
	num2 += 1

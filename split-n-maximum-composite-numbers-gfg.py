# Python3 program to split a number into 
# maximum number of composite numbers.

# Function to calculate the maximum number 
# of composite numbers adding upto n
def count(n):
	if n < 4 :
		return -1;
	rem = n % 4

	if(rem == 0):
		return n // 4
	if rem == 1:
		if n < 9:
			return -1
		else:
			return (n - 9) // 4 + 1
	if rem == 2:
		if n < 6:
			return -1
		else:
			return (n - 6) // 4 + 1
	if rem == 3:
		if n < 15:
			return -1
		else:
			return (n - 15) // 4 + 2 #2 becz 15 can be further expressed as 6 + 9 to get the maximum value
		 	 	 	 



# Unindented outside the class, with body indented properly
if __name__ == "__main__":
    # Test inputs
    result = count(90)
    print("Result: for 90 -- ", result)
    print("Result: for  143 -- ", count(143))

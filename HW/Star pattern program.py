#Print star pattern program

num = int(input("Enter the number vof rows"))
for i in range(1,num+1):
	for j in range(1,i+1):
		print( "*",end = " ")
	print()
# Python Program - prints the pyramid pattern of alphabets:
#65 values is asci values for A
#val = 65
for i in range(0,5):
	val = 65
	for j in range(0, i+1):
		ch = chr(val)
		print(ch, end=" ")
		val = val + 1
	print()
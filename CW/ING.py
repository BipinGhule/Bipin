def verbing(input_str):
	if len (input_str)<3:
		return input_str
	elif input_str[-3:]=='ing':
		return input_str[:-3]+'ly'
	else:
		return input_str + 'ing'
def main():
	num =(input("Enter the string"))
	print(verbing(num))

if __name__=='__main__':
	main()

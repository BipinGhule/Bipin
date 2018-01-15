def verbing(input_str):
	if len (input_str)<3:
		return input_str
	elif input_str[-3:]=='ing':
		return input_str[:-3]+'ly'
	else 
		return input_str + 'ing'
		
		
def main():
	input_str=input("Enter string which is to be verbed")
	output_str=verbing (input_str)
	print ("ver of {} is {} .format (input_str,output_str))
if __name__=='__main__':
	main()
	
#ba**ble
	input_str[0]+ input_str[1:].replace(input_str[0],replace_char)
#Take a string from the user and store it in a variable.
#Initialize the character count variable to 0 and the word count variable to 1.
#Use a for loop to traverse through the characters in the string and increment the character count variable each time.
#Increment the word count variable only if a space is encountered.
#Print the total count of the characters and words in the string.
#Exit.


def main():
	sentence=input("Enter sentence:")
	char=0
	word=1
	for i in sentence:
		char=char+1
		if(i==' '):
				word=word+1
	print("Number of words in the sentence:")
	print(word)
	print("Number of characters in the sentence:")
	print(char)
if __name__=='__main__':
	main()

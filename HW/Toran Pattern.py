#def main():
for row in range(4):
	for col in range(7):
		if col==0 or col==6 or col==1 or col==5:
	#if col==0 or col==6 or (col==1 and row==0) or (col==2 and row==0) or (col==3 and row==0) or (col==4 and row==0) or (col==5 and row==0) or (col==6 and row==0):
			print ("*",end="")
		else:
			print (end=" ")
	print ()
#if __name__=='__main__':
#	main()	
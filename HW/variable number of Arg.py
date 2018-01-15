def variableofargumentsisdemo(*args):
	print (type(args))
	for x in args:
		print (x)
def main():
	variableofargumentsisdemo(1,2,3,45,"hi","bye")
	variableofargumentsisdemo(8,9,99,458,"yes","no")
if __name__=='__main__':
	main()
	
	
	
	
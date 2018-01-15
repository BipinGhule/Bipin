def VariableArgsDictionaryDemo(a,b,c,*args,**kwargs):
	print (a,b,c)
	print (type(args))
	print (type(kwargss))
	for x in args:
		print (x)
	for key,values in kwargs.items():
		print (key,values)
	
def main():
	VariableArgsDictionaryDemo(1,2,3,7,8,9,name="bipin",hobby="Taching")
	
if __name__=='__main__':
	main()
			
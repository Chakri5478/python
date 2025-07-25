n=int(input("Enter a number:"))
code=65
for i in range(1,n+1):
	
	for j in range(i):
		
		print(chr(code),end="")
		code+=1
	print("")

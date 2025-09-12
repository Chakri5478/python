#Factorial of a number using recursinons
def fact(n=0):
	if n==0:
		return 1
	else:
		return n*fact(n-1)
n=int(input("Enter a number:"))
print("Factorial of ",n," is:",fact(n))

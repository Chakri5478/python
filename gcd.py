#finding the gcd using recursions
def gcd_rec(a,b):
	if b==0:
		return a
	else:
		return gcd_rec(b,a%b)
a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
print("GCD of ",a,",",b,"is ",gcd_rec(a,b))
	

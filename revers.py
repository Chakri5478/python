n=int(input("Enter a number:"))
rev=0
while n!=0:
	g=n%10
	rev=rev*10+g
	n=n//10
print(rev)

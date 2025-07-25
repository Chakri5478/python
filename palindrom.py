n=int(input("Enter a number:"))
m=n
rev=0
while n!=0:
	g=n%10
	rev=rev*10+g
	n=n//10
if m==rev:
	print(m,"is a palindrom")
else:
	print(m,"is not a palindrom")

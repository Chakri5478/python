n=int(input("Enter a number:"))
sum=0
while n!=0:
	g=n%10
	sum=sum+g
	n=n//10
print(sum)

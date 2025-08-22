#To print even length words
c=input("Enter a string:")
a=c.split()
print(a)
for i in a:
	if len(i)%2==0 :
		print(i)

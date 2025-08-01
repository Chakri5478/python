#finding positions of min and max position in the list
l=[]
n=int(input("Enter the size"))
for i in range(n):
	ele=int(input())
	l.append(ele)
a=max(l)
b=min(l)
for i in range(n):
	if a==l[i]:
		c=i
	elif b==l[i]:
		d=i
print("maximum number is",a,"its position is",c)
print("minimum number is",b,"its position is",d)

#swaping first and last element
l=[]
n=int(input("Enter the size:"))
for i in range(n):
	ele=int(input())
	l.append(ele)
temp=l[n-1]
l[n-1]=l[0]
l[0]=temp
print(l)

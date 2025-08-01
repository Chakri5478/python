#even and odd seperation
#sum and avg of the list
l=[]
n=int(input("Enter the size"))
for i in range(n):
	ele=int(input())
	l.append(ele)
e=[]
o=[]
for i in range(n):
	if l[i]%2==0:
		e.append(l[i])
	else:
		o.append(l[i])
print("Even list:",e)
print("Odd list:",o)

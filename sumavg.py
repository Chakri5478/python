#sum and avg of the list
l=[]
n=int(input("Enter the size"))
for i in range(n):
	ele=int(input("Enter the data"))
	l.append(ele)
print("Sum of the list:",sum(l))
avg=sum(l)/2
print("Average of the list:",avg)

#reverse of the list
l=[]
n=int(input("Enter the size"))
for i in range(n):
	ele=int(input("Enter the data"))
	l.append(ele)
print("Listy is",l)
l.reverse()
print(l)

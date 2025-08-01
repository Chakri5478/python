#removing duplicate from the list
l=[]
n=int(input("Size:"))
for i in range(n):
	ele=int(input())
	l.append(ele)
found=False
for i in range(len(l)):
	for j in range(i+1,len(l)):
		if l[i]==l[j]:
			l.pop(i)
			found=True
			break
	if found:
		break
print(l)

#Reversing the list without slicing
a=[1,2,3,4,5]
def reverse(a):
	l=len(a)
	for i in range(l):
		print(a[l-i-1],end=" ")
reverse(a)

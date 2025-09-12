#Fabinokey series
def fabino(n=0):
	if n<=1:
		return n
	else:
		return fabino(n-1)+fabino(n-2)
n=int(input("Enter a number:"))
print("Fabino key series:")
for i in range(n):
	print(fabino(i),end="")

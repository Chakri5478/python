#reversing the string without slicing
s="Chakri"
a=s
s1=""
for i in s:
	s1=i+s1
if a==s1:
	print(a," is a palindrom")
else:
	print(a," is not a palindrom")

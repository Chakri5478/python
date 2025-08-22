#counting the number of vowels in the given string
c=input("Enter a string:")
v=['a','e','i','o','u','A','E','I','O','U']
count1=0
count2=0
for i in c:
	if i in v :
		count1+=1
	else:
		count2+=1
print("Number of vowels:",count1)
print("Number of consonents:",count2)

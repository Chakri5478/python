#Even or Odd using lambda function
n=int(input("Enter a number:"))
b=lambda n: "Even" if n%2==0 else "Odd"
print(b(n))

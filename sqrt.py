n= float(input("Enter a number:"))
guess=n/2
while(guess*guess>n):
    guess=guess - 0.00001
print("Square root:",guess)
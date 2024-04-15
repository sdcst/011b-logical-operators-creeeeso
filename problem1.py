#! python3
 
"""
Problem 1
Ask the user to enter a number.
The number is considered "frue" if it is
divisible by 6, but not divisible by 8.
State whether the number is "frue" 
(2 marks)

Inputs:
a number

Outputs:
xx is frue
xx is not frue

example:
Enter a number: 48
48 is not frue

Enter a number: 36
36 is frue

Enter a number: 16
16 is not frue
"""

n=int(input("Enter a number: "))

x= n%6
y= n%8
if x==0 and y !=0:
    print(f"{n} is frue")
else:
    print(f"{n} is not frue")

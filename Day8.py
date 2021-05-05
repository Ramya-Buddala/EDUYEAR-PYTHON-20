'''Q1. Take a number from user and check whether it is prime or not. Use parameters to send the number to function.
Eg. Enter a number 3
       3 is prime'''

num = int(input())
flag = False
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            flag = True
            break
if flag:
    print(num, "is not a prime number")
else:
    print(num, "is a prime number")

'''Q2. Write a function to print n factorial. Take n value as user input and pass as a parameter
Eg. Enter a number 5
      120'''
def factorial_num(n):
    count=1
    for i in range(1,n+1):
        count=count*i
    print("Factorial of {} is {}".format(n,count))
factorial_num(int(input("enter a number")))

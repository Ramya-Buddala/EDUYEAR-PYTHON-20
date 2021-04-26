#Create a list of n numbers
#Q1.Count even numbers and odd numbers in the list
ce,co=0,0
n=int(input())
l=list(map(int,input().strip().split()))[:n]
for i in range(len(l)):
    if l[i]%2==0:
        ce += 1
    else:
        co +=1
print("Count of even numbers in list is : {}\nCount of odd numbers in list is : {}".format(ce,co))


#Create a list of n numbers
#Q2.Tell max and min of the list ( without using any inbuilt function like max(),min())
n=int(input("Enter number of elements in the list : "))
l=list(map(int,input().strip().split()))[:n]
max=l[0]
min=l[0]
for i in range(len(l)):
    if(max<l[i]):
        max=l[i]
    if(min>l[i]):
        min=l[i]
print("Maximum element in the list is:{}\nMinimum element in the list is:{}".format(max,min))


#Create a list of n numbers
#Q3.Check whether the whole list is palindrome or not( eg. [1,2,1] gives yes for palindrome while [1,2,2] doesn't
n=int(input("Enter number of elements in the list : "))
l=list(map(int,input().strip().split()))[:n]
a=l[::-1]
if l==a:
    print("Yes the whole list is palindrome")
else:
    print("No the whole list is not palindrome")


#Create a list of n numbers
#Q4.Print the numbers which are palindrome inside the list
n=int(input("Enter the number of elements in the list:"))
l=list(map(int,input().strip().split()))[:n]
for i in range(len(l)):
    rev=0
    temp=l[i]
    while (temp>0):
        rem=temp%10;
        rev=(rev*10)+rem
        temp=temp//10
    if(rev==l[i]):
        print(rev)

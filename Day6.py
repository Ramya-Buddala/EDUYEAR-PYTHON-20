#1. Give all the index values of vowels.

#Eg. "abed" 
#>> 0 2
name=input("Enter the string:")
for i in range(len(name)):
    if(name[i]=='a' or name[i]=='e' or name[i]=='i' or name[i]=='o' or name[i]=='u'):
        print(i,end=" ")

#2.Reverse the words of a string
#Input... hello world happy birthday
#Output... birthday happy world hello
st = input("Enter the string:")
l=st.split()
r=l[::-1]
a=' '.join(r)
print(a)

#3. Remove duplicate elemnts without using set()
#Ex. [1,2,3,3,2,4]
#>> [1,2,3,4]
n=int(input("Enter elements of list:"))
l=list(map(int,input().strip().split()))[:n]
res=[]
for i in l:
    if i not in res:
        res.append(i)
print(res)


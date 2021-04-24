print("-----enter 'q' r 'Q' to stop the numbers to add --------")
sum=0
while 1:
    a=input()
    if(a=='q' or a=='Q'):
        break
    else:
        b=int(a)
        sum=sum+b
print(sum)

'''n = int(input())
m = int(input())
for i in range(n,m+1):
    if i%5 == 0 or i%7 == 0 :
        print(i)
'''
n = int(input())
m = int(input())
i = n
while(i<=m):
    if i%5 == 0 or i%7 == 0:
        print(i)
    i += 1

'''Q1.Print following a pattern without using any loop. (Hint use recursive functions)
Examples : 
Input: n = 16
Output: 16, 11, 6, 1, -4, 1, 6, 11, 16
Input: n = 10
Output: 10, 5, 0, 5, 10'''

def my_func(a, b):
	print(a, end= ' ')
	if a <= 0:
		return 
	my_func(a-b, b)
	print(a, end= ' ')

a,b=map(int,input().split())
my_func(a,b)
print()

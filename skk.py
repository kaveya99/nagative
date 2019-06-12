value1=int(input())
value2=[int(i) for i in input().split()]
result=0
for i in range(value1):
	for j in range(i):
		if value2[j]<value2[i]:
			result+=value2[j]
print(result)
© 2019 GitHub, Inc.

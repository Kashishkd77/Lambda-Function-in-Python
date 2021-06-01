#illustration of map function using lambda function
#double the number list assigned
num=[1,78,23,11,7,0,-1,67]
print(list (map (lambda n : n*2 , num) ) )

f=map(lambda n:n*2,num)
for i in f:
    print(i)

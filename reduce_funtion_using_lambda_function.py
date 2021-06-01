#illustration of reduce function using lambda function
#print the largest in the list and sum of elements of list
import functools

li_st=[23,45,2,12,78,8]
print(functools.reduce(lambda a,b :a if a>b else b,li_st))
print(functools.reduce(lambda a,b :a+b,li_st))
#print(list(map(lambda a,b :a+b,li_st))) -->> creates error as it cannot take two values from list as input

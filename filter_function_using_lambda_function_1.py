#illustration of filter function using lambda function

letter=['w','e','o','a','m','a','r','x']

#to print all the vowels in the given list
print(list(filter(lambda letter: letter in ['a','e','i','o','u'],letter)))
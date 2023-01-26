#How can you reverse a string in Python using slicing in just one line of code?

# x=input("enter your name : ")
# print(x[::-1])


#How can you sort a list of integers in descending order using the sorted() function and a lambda function in just one line of code?

# num = [1,2,3,5,3,2,1,5,4]
# num = sorted(num,key=lambda x:-x) #using lambda
# print(num)


#How can you remove duplicates from a list in Python using a list comprehension in just one line of code?

# num = [1,2,3,5,3,2,1,5,4]
# print(list(set(num)))

#How can you flatten a nested list in Python using a list comprehension in just one line of code?

# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# flatten = [j for i in nested_list for j in i]

# print(flatten)

#How can you find the most common element in a list in Python using the collections module in just one line of code?

# from collections import Counter
# num = [1,2,3,5,3,2,1,5,4,1,1,1]

# print(Counter(num).most_common(1))

#How can you check if a given number is a prime number in just one line of code?

# def is_prime(n):
#     return n > 1 and all(n % i for i in range(2, int(n ** 0.5) + 1))
  

# x=50
# print(is_prime(x))



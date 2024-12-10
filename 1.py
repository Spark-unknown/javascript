# # # #    practical 1  
# # #        #example of argument with return type

# # # # # def fun(a,f = "hello world"):
    
# # # # #     print("this is a function " + a )
    
# # # # #     print("this is a function " + f )
    
# # # # #     sum = a + f
    
# # # # #     return sum
   
# # # # # result  =  fun("3") 

# # # # # print("the value of result is " + result)
# # # #         #this is example of only argument

# # # # def fun(a = "this",f = "hello world"):
    
# # # #     print("this is a function " + a )
    
# # # #     print("this is a function " + f )
    
# # # # fun()    


# # # # # def fun():
# # # # #     print("this is an example of without arg and return type")
    
# # # # #     fun()
    
# # # # # def fun():
# # # # #      print("this is an example or without argument with return type")
# # # # #      a = int(input("enter your first value"))
# # # # #      b = int(input("enter your second value"))
# # # # #      sum = a + b
# # # # #      return sum
# # # # # res = fun()
# # # # # print("this is res " , res)   


# # # # Practical 2

# # # # Insertion
# # # array = [1, 2, 3, 4, 5]
# # # array.append(6)  
# # # array.insert(2, 99)  
# # # print("After insertion:", array)

# # # # Deletion
# # # array.pop(2)  
# # # array.remove(6)  
# # # print("After deletion:", array)

# # # # Arithmetic operations
# # # array = [1, 2, 3, 4, 5]
# # # sum_array = sum(array)
# # # print("Sum of array:", sum_array)
# # # product = 1
# # # for num in array:
# # #     product *= num
# # # print("Product of array:", product)


# #           # practical 3

# # # import numpy as np

# # # # Vectors
# # # vector1 = np.array([1, 2, 3])
# # # vector2 = np.array([4, 5, 6])
# # # vector_add = vector1 + vector2
# # # vector_multiply = vector1 * vector2
# # # print("Vector Addition:", vector_add)
# # # print("Vector Multiplication:", vector_multiply)

# # # # Matrices
# # # matrix1 = np.array([[1, 2], [3, 4]])
# # # matrix2 = np.array([[5, 6], [7, 8]])
# # # matrix_add = matrix1 + matrix2
# # # matrix_multiply = np.dot(matrix1, matrix2)
# # # print("Matrix Addition:\n", matrix_add)
# # # print("Matrix Multiplication:\n", matrix_multiply)


# # # Length finding
# # string = "hello world"
# # print("Length of string:", len(string))

# # # Change specific character
# # string = "hello world"
# # new_string = string[:6] + 'W' + string[7:]
# # print("String after change:", new_string)

# # # Palindrome
# # def is_palindrome(s):
# #     return s == s[::-1]

# # print("Is 'racecar' a palindrome?", is_palindrome("racecar"))
# # print("Is 'hello' a palindrome?", is_palindrome("hello"))

# # # Concatenation
# # string1 = "hello"
# # string2 = "world"
# # concatenated_string = string1 + " " + string2
# # print("Concatenated string:", concatenated_string)


# def is_leap_year(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     else:
#         return False

# year = int(input("Enter a year: "))
# if is_leap_year(year):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")


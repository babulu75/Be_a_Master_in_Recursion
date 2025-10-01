#                                   ========Be a Master in Recursion========

#   what is recursion ?
#       Recursion is nothing but calling a fucntion itself or in simple terms a function calling itself
#   Note :
#       Every recursive function have two parts 
#           1. Base Case
#           2. Recursive Part
#       1. Base Case : It is nothing but a stopping condition like break for while loop but here we simply stop by return any value 
#       2. Recursive Part : This part is to calling the function until the base case is satisfied   (or)
#                           Simply breaking the problem into smaller parts until we reach required smaller part

#   *Note :
#       As python is top to bottom appraoch we should write function first before calling them 

#   Lets start with basic problems 

#   print 1 to n numbers using recursion 


def basic_recursion_1_to_n(n): # def is used to define the function in python
    if n==0:            # Base Case : that stops recursion                  
        return n        # here it return 1 back to the function here its end of recursive call
                           
    basic_recursion_1_to_n(n-1)    # Its a recursive case where function will call itself until the base condition satisfies

    print(n)                # Now after terminating the recursion the value will be started printing that from 1
                                # first it reaches n==1 then it start printing form 1,2,3,.. to n
                                # after successful printing the function will ends.....
    return
n =  int(input("Enter the n value : "))
basic_recursion_1_to_n(n)
#output 
#1 2 3 4 5 6 7 8 9 10 in vertical order 

# same code with slight difference in placing print command can print n to 1 numbers 

def basic_recursion_n_to_1(n):
    if n==0:
        return n        #same base case to end recursive calling
    

    print(n)            # printing the first before calling makes it reversing the order
    basic_recursion_n_to_1(n-1)
    return
n=10
basic_recursion_n_to_1(n)

#10 9 8 7 6 5 4 3 2 1 in vertical order
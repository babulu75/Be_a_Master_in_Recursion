#  sum of first n natural numbers using recursion

def sum_of_n_natural_numbers(n):

    if n==0:                # Base case to stop at 0 because natural numbers are starting from 0
        return 0            # here return type should be int beacuse  we directly adding it with previous number
    print(n)
    return n+sum_of_n_natural_numbers(n-1)    # recursive calling plus adding the number to previous one 
    
print(sum_of_n_natural_numbers(10))
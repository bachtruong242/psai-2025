#import numpy as np

#def mean(n)
    #return np.mean()

def get_median(numbers):
    numbers.sort()
    n = len(numbers)
    if n % 2 == 1:
        return numbers[n//2]
    if n % 2 == 0:
        m1 = n//2
        m2 = mid1 - 1
        return (numbers[m1] + numbers[m2]) / 2
    user_input = (int(input()))
    number_list = list(map(int, user_input.split()))
    
    median = get_median(number_list)
    print(median)
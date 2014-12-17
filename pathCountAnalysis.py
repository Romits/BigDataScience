import math
import sys
import numpy as np

"""
The number of path will be (m+n-2)choose(m-1)
"""
def countPath(inputArray):
    m,n = inputArray.shape
    f = math.factorial
    result = f(m+n-2)/(f(n-1) * f(m+n-2-(n-1)))
    return result

def main():
    inputArray = np.arange(100)
    inputArray = inputArray.reshape(10,10)
    result =  countPath(inputArray)
    print result 

if __name__=="__main__":
    main()

import numpy as np
import math

n=100
def catalan(n):
    if n == 0:
        return 1 
    else:
        return (4*n-2)/(n+1)*catalan(n-1)

print(catalan(100))
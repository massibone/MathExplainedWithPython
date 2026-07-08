import scipy
import math

def sinc(x):
    if x == 0:
        return 1
    else:
        return math.sin(x)/x


correction_factor = sinc(10)

print(correction_factor)

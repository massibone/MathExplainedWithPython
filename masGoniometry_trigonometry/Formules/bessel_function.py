'''
To use Bessel functions in Python, you need to import the "scipy" module.

Here is an example code to calculate the first-order Bessel function of the first kind:

'''
import scipy.special

x = 2.0
J = scipy.special.jn(1, x)

print("J(1, {})= {}".format(x, J))

'''
output:

J(1, 2.0)= 0.5767248077568734


'''

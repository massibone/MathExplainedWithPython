
import numpy
import matplotlib.pyplot as pyplot

x = numpy.arange(0, 1000, 0.01)
y = [10 / (500.53 - i) for i in x]
#pyplot.plot(x, y, 'b')
pyplot.axis([0, 1000, -10, 10])
threshold = 1000 # or a similarly appropriate threshold
y = numpy.ma.masked_less(y, -1*threshold) 
y = numpy.ma.masked_greater(y, threshold)

pyplot.plot(x, y, 'c')
pyplot.axis([0, 1000, -10, 10])
pyplot.show()

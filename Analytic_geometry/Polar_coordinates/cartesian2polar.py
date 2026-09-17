import math

i=7.0
q=8.0

print "Cartesian: (%.1f,%.1f)" %(i,q)
print "Polar: r = %.1f" %math.sqrt(math.pow(i,2) + math.pow(q,2)) + ", Theta = %.1f" %math.degrees(math.atan(q/i)) + " degrees"

def find_volume(area, h):
	
	# Formula to calculate
	
	Volume = (area * h)
	
	# Display volume
	print("Volume: ", end =" ")
	print(Volume)

# Function to find the
# surface area of octagonal prism
def find_Surface_area(area, a, h):
	
	# Formula to calculate Surface area
	Surface_area = (2 * area)+(8 * a * h)
	
	print("Surface area: ", end =" ")
	print(Surface_area)
	
# Driver Code
h = 1
a = 6
d = 2
area = 2 * a * d


find_Surface_area(area, a, h)

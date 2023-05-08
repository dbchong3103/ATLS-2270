'''
Name: Dahn Bi Chong
Problem: Blocked Billboard II (Rectangle Geometry)
Objective: Bessie doesn't like lawnmowers so now we have to cover that billboard. This could will take into account the cornerns of the billboard in order to determine a minimum size for a tarp to cover the unwanted lawnmower sign. It will compare the values of the corners of the billboards to ultimately determine the size of tarp needed.
'''

#Opens file, and this time also sets up a closing file, didn't make the close out file at the end so that we can use this variable throughout the problem for different billbaords in the elifs
fin, fout = open("billboard.in"), open("billboard.out", "w")

#Set up the coordiantes of the billboards! Note that the cow billboard can cover up some of the lawnmower billboard which changes how much tarp is needed!
x1, y1, x2, y2 = map(int, fin.readline().split())
a1, b1, a2, b2 = map(int, fin.readline().split())

#This section of great than and less than statements will determine if any of the corners are covered by the cow billboard already, Note that these don't actually ewual any numbers they are just comparing the x and y xoordinates from the cow and lawnmower billboards. Lawnmower coordinates are set with x and y whil ethe cow billboard is set with a and b for clarity. 
topLeft = a1 <= x1 and b2 >= y2
topRight = b2 >= y2 and a2 >= x2
bottomRight = a2 >= x2 and b1 <= y1
bottomLeft = b1 <= y1 and a1 <= x1

#Determines an addition of all of the conditions aboce
corner_num = sum([topLeft, topRight, bottomRight, bottomLeft])

#These if and elif statements essentially compare every top and bottom corner with another to determine which corners are covered using the great than or less than statements above. 

#This one concludes that the entire billboard is covered already and therefore we don't need a tarp, so the minimum is 0
if bottomLeft and topRight:
	fout.write(str(0))

#determines if the cow sign does anything to cover
elif corner_num in [0, 1]:
	fout.write(str(abs(x2 - x1) * abs(y2 - y1)))

#Determines if the right side of the lawnmower sign is covered 
elif bottomRight and topRight:
	fout.write(str(abs(y2 - y1) * abs(x2 - a2)))

#Determines if the Left side is covered
elif bottomLeft and topLeft:
	fout.write(str(abs(y2 - y1) * abs(x2 - a2)))

#determines if top is covered
elif topRight and topLeft:
	fout.write(str(abs(x2 - x1) * abs(b1 - y1)))
 
#Determines if bottom is covered
elif bottomRight and bottomLeft:
	fout.write(str(abs(x2 - x1) * abs(b1 - y1)))
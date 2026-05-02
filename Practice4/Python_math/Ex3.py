import math 

numofsides = int(input("Enter the number of sides:"))
length = int(input("Enter the value of the length of side:"))
area = (numofsides * length**2) / (4 * math.tan(math.pi / numofsides))
print("Area is:", round(area,2))
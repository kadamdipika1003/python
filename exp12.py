place1 = ("Pune", 18.5204, 73.8567)
place2 = ("Mumbai", 19.0760, 72.8777)
place3 = ("Delhi", 28.6139, 77.2090)

name1, latitude1, longitude1 = place1
name2, latitude2, longitude2 = place2
name3, latitude3, longitude3 = place3

print("Location 1")
print("Name:", name1)
print("Latitude:", latitude1)
print("Longitude:", longitude1)

print("\nLocation 2")
print("Name:", name2)
print("Latitude:", latitude2)
print("Longitude:", longitude2)

print("\nLocation 3")
print("Name:", name3)
print("Latitude:", latitude3)
print("Longitude:", longitude3)

# index() operation
print("\nIndex Operation")
print("Index of Pune:", place1.index("Pune"))
print("Index of 18.5204:", place1.index(18.5204))


# Slicing operation
print("\nSlicing Operation")
print("First two values of Pune:", place1[0:2])
print("Latitude and Longitude of Pune:", place1[1:3])

print("First two values of Mumbai:", place2[:2])
print("Latitude and Longitude of Delhi:", place3[1:])
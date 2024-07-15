list1 = input("Enter a number: ").split()
list2 = input("Enter second number: ").split()

setA = set(map(int, list1))
setB = set(map(int, list2))

intersection = setA.intersection(setB)
difference = setA.difference(setB)
union = setA.union(setB)

print("Intersection:", intersection)
print("Difference:", difference)
print("Union:", union)

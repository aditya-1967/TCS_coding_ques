#find the hypotenuse of a triangle
sides = [[6, 8], [3, 4], [5, 12]]
hypotenuse = []
for i in range(len(sides)):
    hypotenuse.append((sides[i][0]**2 + sides[i][1]**2)**0.5)
print(hypotenuse)

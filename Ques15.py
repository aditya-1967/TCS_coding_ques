#Check if given sides are sides of right-angled triangle or not.
sides = [[6, 8, 10], [3, 4, 5], [5, 12, 13], [3, 6, 8]]
hypotenuse = []
for i in range(len(sides)):
    hypotenuse.append((sides[i][0]**2 + sides[i][1]**2)**0.5 == sides[i][2])
print(hypotenuse)

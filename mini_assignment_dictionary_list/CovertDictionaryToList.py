d = {'HuEx': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
print("The original dictionary is : " + str(d))

res = []
for key, val in d.items():
    res.append([key] + val)

print("The converted list is : " + str(res))
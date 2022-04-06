list  = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = input()
    list.append(ele)
print(list )
#input_list = ["Alaska", "Alabama", "Arizona", "Arkansas", "Colorado", "Montana", "Nevada"]
print( sum(map(lambda x: x[0] == 'A', list)))
print( sum(map(lambda x: x.lower().count("a"), list))-sum(map(lambda x: x[0] == 'A',list)))
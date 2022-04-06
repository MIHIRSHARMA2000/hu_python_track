input_list  = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())

    input_list.append(ele)
print(input_list )

output_filter = list(filter(lambda x: True if x>0 else False, map(lambda x: x*-1, input_list)))
print(output_filter)
print()
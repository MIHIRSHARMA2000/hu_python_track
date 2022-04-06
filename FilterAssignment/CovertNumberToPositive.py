import functools

output_filter = list(filter(lambda n: n > 0, list(map(int, input("Enter list of numbers: ").split()))))
print(output_filter)
print()

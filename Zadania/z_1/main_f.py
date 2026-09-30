import module

f_max = module.make_extremum()
f_min = module.make_extremum("min")

data = [3, 1, 4, 1, 5, 9, 2, 6]

print("Максимум:", f_max(data))
print("Минимум:", f_min(data))
employees = [
    {"name": "Ajay", "age": 22, "salary": 25000},
    {"name": "Rahul", "age": 25, "salary": 40000},
    {"name": "Kiran", "age": 21, "salary": 30000}
]

def dynamic_sort(data, keys):
    return sorted(data, key=lambda emp: tuple(emp[k] for k in keys))


print("Salary Descending:")
for e in sorted(employees, key=lambda x: x["salary"], reverse=True):
    print(e)

print("\nAge then Salary:")
for e in sorted(employees, key=lambda x: (x["age"], x["salary"])):
    print(e)

print("\nDynamic Sort (salary, age):")
for e in dynamic_sort(employees, ["salary", "age"]):
    print(e)

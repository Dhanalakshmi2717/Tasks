from collections import defaultdict   

attendance = [
    ("Ajay", "2026-01-01", "Present"),
    ("Ajay", "2026-01-02", "Absent"),
    ("Rahul", "2026-01-01", "Present")
]

total_days = defaultdict(int)
present_days = defaultdict(int)

for name, date, status in attendance:
    total_days[name] += 1
    if status == "Present":
        present_days[name] += 1

print("Attendance Percentage:")
for student in total_days:
    percent = (present_days[student] / total_days[student]) * 100
    print(f"{student}: {percent:.2f}%")

print("\nBelow 75% Attendance:")
for student in total_days:
    percent = (present_days[student] / total_days[student]) * 100
    if percent < 75:
        print(student)

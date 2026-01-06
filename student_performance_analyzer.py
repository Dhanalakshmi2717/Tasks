def analyze_students(students):
    topper_name = ""
    topper_avg = 0

    print("Student Performance Analysis:")
    for name, marks in students:
        avg = sum(marks) / len(marks)

       
        if avg >= 85:
            status = "Distinction"
        elif avg >= 50:
            status = "Pass"
        else:
            status = "Fail"

        print(f"{name} -> Average: {round(avg,2)}, Status: {status}")

       
        if avg > topper_avg:
            topper_avg = avg
            topper_name = name

    print("\nTopper:", topper_name)



if __name__ == "__main__":
    students = [
        ("Ajay", [78, 85, 90]),
        ("Kumar", [65, 70, 60]),
        ("Rahul", [88, 92, 95])
    ]

    analyze_students(students)

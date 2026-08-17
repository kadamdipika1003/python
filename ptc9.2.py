
grades = []

n = int(input("Enter number of Students:"))

for i in range(n):
    grade = int(input(f"Enter grade{i+1}: "))
    grades.append(grade)
    
    print("\n******************")

print("Original grades:", grades)

index = int(input("Enter the index position to update: "))

new_grade = int(input("Enter the new grade: "))

if 0 <= index < len(grades):
    grades[index] = new_grade
    print("Corrected grades:", grades)
else:
    print("Invalid index position.")
name = input("Enter student name: ")

mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))

total = mark1 + mark2 + mark3
average = total / 3

print("\n--- SCORECARD ---")
print("Student:", name)
print("Total Marks:", total)
print("Average:", round(average, 2))

# Daily Class Schedule

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

hours = ["9-10", "10-11", "11-12", "12-1", "1-2"]

# Create 5 x 5 schedule
schedule = [
    ["Free", "Free", "Free", "Free", "Free"],
    ["Free", "Free", "Free", "Free", "Free"],
    ["Free", "Free", "Free", "Free", "Free"],
    ["Free", "Free", "Free", "Free", "Free"],
    ["Free", "Free", "Free", "Free", "Free"]
]

while True:

    print("\n1. View Schedule")
    print("2. Add/Overwrite Subject")
    print("3. Exit")

    choice = int(input("Enter choice: "))

    # View schedule
    if choice == 1:
        print("\nTime\t\tMonday\tTuesday\tWednesday\tThursday\tFriday")

        for i in range(5):
            print(hours[i], end="\t\t")

            for j in range(5):
                print(schedule[i][j], end="\t")

            print()

    # Add or overwrite subject
    elif choice == 2:

        print("\nDays:")
        for i in range(5):
            print(i + 1, days[i])

        day = int(input("Enter day number (1-5): "))

        print("\nTime Slots:")
        for i in range(5):
            print(i + 1, hours[i])

        time = int(input("Enter time slot (1-5): "))

        subject = input("Enter subject/topic: ")

        # Add or overwrite subject
        schedule[time - 1][day - 1] = subject

        print("Schedule updated successfully!")

    # Exit
    elif choice == 3:
        print("Program ended.")
        break

    else:
        print("Invalid choice!")


# Movie Theatre Booking Simulator

seats = [
    ["O", "O", "O"],
    ["O", "O", "O"],
    ["O", "O", "O"]
]

while True:
    print("\nMovie Theatre Seating Layout")
    print("   1  2  3")

    for i in range(3):
        print(i + 1, " ", "  ".join(seats[i]))

    row = int(input("\nEnter row (1-3), or 0 to exit: "))

    if row == 0:
        print("Thank you for using the booking system!")
        break

    column = int(input("Enter column (1-3): "))

    if row < 1 or row > 3 or column < 1 or column > 3:
        print("Invalid row or column. Please enter values from 1 to 3.")
        continue

    row_index = row - 1
    column_index = column - 1

    if seats[row_index][column_index] == "X":
        print("Sorry, that seat is already reserved.")
    else:
        seats[row_index][column_index] = "X"
        print(f"Seat ({row}, {column}) has been reserved successfully!")

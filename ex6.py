print("\n-----EXERCISE 1:RECEIPT NUMBER PATTERN----")
rows_pattern=int(input("Enter the number of rows for receipt pattern:"))

print("\n Generated pattern:")

for i in range(1, rows_pattern +1):

    for j in range(1, i+1):
        print(i,end=" ")

    print()


       
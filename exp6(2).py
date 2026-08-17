print("-----EXERCISE 2: INVOICE FRAM BORDER---")
frame_rows = int(input("Enter frame height(rows):"))
frame_cols = int(input("Enter frame width(colums):"))

for i in range(frame_rows):
    for j in range(frame_cols):
        if i==0 or i==frame_rows - 1 :
            print("*", end="")
        elif  j==0 or j==frame_cols - 1:
             print("*", end="")
        elif i==1 and j==12:
            print("RECEIPT",end="")
            break
        else:
            print(" ",end="")

    print()
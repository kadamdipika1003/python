user_paragraph = input("Enter the paragraph:")

words = user_paragraph.lower().split()

count = 0

for word in words:
    if word == "python":
        count += 1

print("The word python appears", count, "times.")
library={
    "12345":{
        "title": "Pride and Prejudice",
        "author": " Jane Austen",
        "year":1813,
        "availiblity": "True"
    
    },
    "67891": {
        "title": "The Great Gatsby",
                "author": "F. Scott Fitzgerald ",
                "year":1925,
                "availiblity": "False"

    }

}

running=True
while running:
    print("\n==dictionarries==")
    print("1.Display All Books")
    print("2.Add New Books")
    print("3.Update  Books")
    print("4.Exit")

    choice=(input("enter your choice(1 to 4) : "))

    if choice=="1":
        if not library:
            print("library is not found")
        else:
            print("======BOOKS IN LIBRRY======")   

            for isbn, info in library.items():
                print("\n isbn:", isbn)
                print("Title:", info["title"])
                print("Author:", info["author"])
                print("Year:", info["year"])
                
    elif choice == "2":
        isbn = input("Enter book ID: ")

        if isbn in library:
            print("isbn already exists!")
        else:
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            year = int(input("Enter publication year: "))
            availability = input("Is the book available? (True/False): ")

            if availability.lower() == "true":
                availability = True
            else:
                availability = False

            library[isbn] = {
                "title": title,
                "author": author,
                "year": year,
                "availability": availability
            }

            print("Book added successfully!")            


    elif choice == "3":
        isbn = input("Enter book isbn to update: ")

        if isbn not in library:
            print("Book not found!")
        else:
            print("\n1. Update Title")
            print("2. Update Author")
            print("3. Update Year")
            print("4. Update Availability")

            update_choice = input("Enter your choice: ")

            if update_choice == "1":
                library[isbn]["title"] = input("Enter new title: ")
                print("Title updated successfully!")

            elif update_choice == "2":
                library[isbn]["author"] = input("Enter new author: ")
                print("Author updated successfully!")

            elif update_choice == "3":
                library[isbn]["year"] = int(input("Enter new year: "))
                print("Year updated successfully!")

            elif update_choice == "4":
                value = input("Is the book available? (True/False): ")
                library[isbn]["availability"] = value.lower() == "true"
                print("Availability updated successfully!")

            else:
                print("Invalid update choice!")
                

    elif choice == "4":
        running = False
        print("Thank you! Program ended.")

    else:
        print("Invalid choice! Please enter 1 to 4.")
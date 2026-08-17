
print("***********Customer Feedback Formatter**********")


name = input("Enter customer name: ")
feedback = input("Enter customer feedback: ")
rating = int(input("Enter rating (1-5): "))

name = name.strip()
print("Name:",name)
feedback = feedback.strip()
print("Feedback:",feedback)

formatted_name = name.title()
print(formatted_name)

formatted_feedback = feedback.capitalize()
print(formatted_feedback)

upper_feedback = feedback.upper()
print(upper_feedback)

lower_feedback = feedback.lower()
print(upper_feedback)

words = feedback.split()
print("Words:", words)


replaced_feedback = feedback.replace(" ", "-")
print("Replaced Feedback:", replaced_feedback)

joined_feedback = " ".join(words)
print("Joined Feedback:", joined_feedback)


print("\n********* Professional Feedback**********")

print(f"Customer Name: {formatted_name}")
print(f"Feedback     : {formatted_feedback}")
print(f"Rating       : {rating}/5")
print(f"Thank you    , {formatted_name}, for your valuable feedback!")
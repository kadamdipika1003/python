text = input("Enter a paragraph: ")

word_count = 0
space_count = 0
character_count = 0
vowel_count = 0

vowels = "aeiouAEIOU"

for char in text:
    character_count += 1

    if char == " ":
        space_count += 1

    if char in vowels:
        vowel_count += 1

word_count = len(text.split())

print("\n--- Text Analyzer ---")

print("Number of words     :", word_count)
print("Number of spaces    :", space_count)
print("Number of characters:", character_count)
print("Number of vowels    :", vowel_count)
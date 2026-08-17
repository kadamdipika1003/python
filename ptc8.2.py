print("******TEXT MODERATE FILTER********")

feedback = "This is a badword and another badword."

target_words = ["badword", "stupid", "idiot"]

for word in target_words:
    feedback = feedback.replace(word, "****")

print(feedback)
import string

text = "I'm Komal from Favtutor, hello. How may I assist you??"
translate = str.maketrans("","",string.punctuation)
new_text = text.translate(translate)
print(new_text)
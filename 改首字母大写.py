text = "hello world"
words = text.strip().split()
new_words =[]
for word in words:
    word = word.capitalize()
    new_words.append(word)
new_text = " ".join(new_words) 
print(new_text)
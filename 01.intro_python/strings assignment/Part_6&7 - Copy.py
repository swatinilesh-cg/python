# --- Task 11: Length ---
word = "Hello"
sentence = "HelloWorld"
spaced_sentence = "Hello World"

print("Word length:", len(word))
print("Sentence length:", len(sentence))
print("Spaced sentence length:", len(spaced_sentence)) # Space counts as 1 character

# --- Task 12: Calculate last index ---
text = "Python Programming"
last_index = len(text) - 1
print("Last character using calculated index:", text[last_index])

# --- Task 13: Full Name ---
first_name = "John"
last_name = "Smith"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# --- Task 14: Sentence Creation ---
person_name = "Emma"
age = "25" # Keeping as string for concatenation
person_city = "London"
fav_lang = "Python"
print(person_name + " is " + age + " years old, lives in " + person_city + " and loves " + fav_lang + ".")

# --- Task 15: String and Integer ---
# TypeError: can only concatenate str (not "int") to str
# print("Age: " + 30) 
print("Age: " + str(30)) # Corrected version
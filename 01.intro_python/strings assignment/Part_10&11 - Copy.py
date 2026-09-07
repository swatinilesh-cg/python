# --- Task 20: Membership ---
phrase = "Python is a programming language"
print("'Python' in phrase?", "Python" in phrase)
print("'programming' in phrase?", "programming" in phrase)
print("'Java' in phrase?", "Java" in phrase)
print("'language' in phrase?", "language" in phrase)

# --- Task 21: find() ---
print("Find 'Python':", phrase.find("Python"))
print("Find 'programming':", phrase.find("programming"))
print("Find 'language':", phrase.find("language"))
print("Find 'Java':", phrase.find("Java")) # Returns -1 when not found

# --- Task 22: index() ---
print("Index 'Python':", phrase.index("Python"))
# print(phrase.index("Java")) # This will throw a ValueError because 'Java' is not found. find() is safer.

# --- Task 23: Count Characters ---
fruit = "banana"
print("Count 'a':", fruit.count("a"))
print("Count 'n':", fruit.count("n"))
print("Count 'b':", fruit.count("b"))

# --- Task 24: Starts and Ends ---
filename = "student_notes.pdf"
print("Starts with 'student':", filename.startswith("student"))
print("Ends with '.pdf':", filename.endswith(".pdf"))
print("Ends with '.txt':", filename.endswith(".txt"))

# --- Task 25 & 26 & 27: Replacing ---
text_replace = "I am learning Java"
print(text_replace.replace("Java", "Python"))

apple_text = "apple apple apple"
print("Replace all:", apple_text.replace("apple", "mango"))
print("Replace first:", apple_text.replace("apple", "mango", 1))

# --- Task 28: Check Immutability ---
text_imm = "Python"
text_imm.upper() 
print("Original string after upper():", text_imm) # Unchanged because strings are immutable
text_imm = text_imm.upper()
print("Stored string:", text_imm) # Changed because we reassigned the variable
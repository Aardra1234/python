course_description = """Welcome to the Complete Python Course! 
This hands-on program covers everything from basic syntax 
to advanced topics like object-oriented programming, data structures, 
and real-world project building."""

string_length = len(course_description)
print("The length of the string is: ", string_length)


print("The first character is: ",course_description[0])
print("The last character is: ",course_description[-1])

print("PREVIEW : ", course_description[:50])

print("Replace all occurrences of the word \"Python\" with \"PYTHON\": ", course_description.replace("Python", "PYTHON"))

print("Lowercase: ", course_description.lower())

print("Removing extra white spaces: ", course_description.strip())


clean_description = course_description.strip()
words_list = clean_description.split()
print("\nList of individual words:")
print(words_list)


if "course" in course_description.lower():
    print("\nMessage: The word 'course' was found in the paragraph!")

char_count = len(clean_description)
word_count = len(words_list)


final_message = "\nThe course description is {} characters long and has {} words.".format(char_count, word_count)
print(final_message)

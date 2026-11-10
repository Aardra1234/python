Python = {"Anu","Parvathy","Malu"}
Data_Science = {"Amal","Gayathri","Shilpa","Malu"}
print("Python: ",Python)
print("Data Science: ",Data_Science)

Python.add("Vimal")
print("Add a new student to Python: ",Python)

Data_Science.pop()
print("Remove one student from Data Science: ",Data_Science)

both = Python & Data_Science
print("Find and display the names of students who are enrolled in both courses: ",both)

print("Find students who are only in the Python course but not in Data Science: ",Python-Data_Science)

print("Display the combined list of all students in either course (no duplicates): ",Python | Data_Science)

course_dict = {"Python":len(Python),"Data_Science":len(Data_Science)}
print("Create a dictionary with course names as keys and number of students as values: ",course_dict)

for course, students in course_dict.items():
    print(f"Course: {course}, Students: {students}")
    

squares = {x: y * 2 for x, y in course_dict.items()} 
print("Using dictionary comprehension, create a new dictionary where course names are unchanged, but values are doubled: ",squares)

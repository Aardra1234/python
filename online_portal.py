Frontend = {"Anu","Parvathy","Malu"}
Backend = {"Amal","Gayathri","Shilpa","Malu"}
print("Frontend: ",Frontend)
print("Backend: ",Backend)

Backend.add("Vimal")
print("Add a new student to Backend: ",Backend)

Frontend.pop()
print("Remove one student from Frontend: ",Frontend)

both = Frontend | Backend
print("Find and display the names of students who are enrolled in both courses: ",both)

print("Find students who are only in the Backend course but not in Frontend: ",Backend-Frontend)

unique_students = len(both)
print(f"Total unique students: {unique_students}")

course_dict = {"Frontend":len(Frontend),"Backend":len(Backend)}
print("Create a dictionary with course names as keys and number of students as values: ",course_dict)

for course, students in course_dict.items():
    print(f"Course: {course}, Students: {students}")
    
updated_courses = {
    **{course: count for course, count in course_dict.items()},
    "Fullstack": sum(course_dict.values())
}

print(updated_courses)
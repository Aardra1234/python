Web_Dev = ["Anu","Parvathy","Akshaya"]
Data_Science =  ["James","Sneha","Gowri"]
Ui_Ux = ["Malu","Clara","Amal"]

all_participants=[Web_Dev,Data_Science,Ui_Ux]
print("Combine all three workshop lists into a single nested list : ",all_participants)

Web_Dev.append("Aiswarya")
print("A new participant joins the Web Development workshop: ",Web_Dev)

Data_Science.insert(2,"Anna")
print("Insert one more participant at the 2nd position in the Data Science list: ",Data_Science)

Ui_Ux.pop()
print("Remove the last participant from the UI/UX Design list: ",Ui_Ux)

Data_New = Data_Science.copy()
Data_Science.clear()
print("Copy the list of Data Science participants to a new list: ",Data_New)
print("clear the original Data_Science list: ",Data_Science)

Web_Dev_slice = Web_Dev[:2]
print("From the Web Development list, display only the first two participants: ",Web_Dev_slice)

name_lengths = [len(name) for name in Data_New]
print("Name Lengths in copied data science list:", name_lengths)

if "Asha" in all_participants:
    print("Asha is present")
else:
    print("Asha is not present")

first_member = (Web_Dev[0],Data_New[0],Ui_Ux[0])
print("A tuple that stores the name of the first participant from each workshop list: ",first_member)

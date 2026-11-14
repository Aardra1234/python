attendance = [18, 20, 19, 15, 21]
count = 0
total = 0
for x in attendance:
    if x>=20:
        print("Full")
        count+=1
    else:
        print('Not Full')
    total+=x
print("The number of days the class was full is: ",count)
print("Total attendance for all 5 days: ",total)

    
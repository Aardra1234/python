fruits = ["Apple","Mango","Grapes"]
vegetables = ["Tomato","Cucumber","Brinjal"]
beverages = ["Coffee","Lemonade","Lassi"] 

fruits.append("Kiwi")
print("Add a new item to the fruits list: ",fruits)

vegetables.insert(2,"Onion")
print("Insert a new item at the second position of the vegetables list: ",vegetables)

beverages.pop()
print("Remove the last item from the beverages list: ",beverages)

inventory = [fruits,vegetables,beverages]
print("Combine all three lists into a nested list called inventory: ",inventory)

fruits_new=fruits[:2]
print("Use slicing to print only the first two fruits: ",fruits_new)

vegetables_new = vegetables[-1]
print("Use negative indexing to access the last item from the vegetables list: ",vegetables_new)

fruits_len =[len(x) for x in fruits]
print("list of lengths of all items in the fruits list using list comprehension: ",fruits_len)

print("Check if Water is in the beverages list: ")
if "Water" in beverages:
    print("Water is in beverages")
else:
    print("Water is not in beverages")
    
tuple_first=(fruits[0],vegetables[0],beverages[0])
print("create a tuple of the first item from each section: ",tuple_first)
    




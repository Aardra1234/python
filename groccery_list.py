initial_list = ["milk", "bread", "eggs"]
def add_item(item):
    initial_list.append(item)
    print("Add an item 'Mango' to the grocery list: ",initial_list)
add_item("Mango")

def remove_last_item():
    initial_list.pop()
    print("removes the last item from the grocery list: ",initial_list)
remove_last_item()

display_item = lambda item: print("Item:", item)
for item in initial_list:
    display_item(item)

def count_characters(items):
    if not items:
        return 0
    return len(items[0]) + count_characters(items[1:])

print("\nTotal characters:", count_characters(initial_list))

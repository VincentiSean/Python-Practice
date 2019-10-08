#! python3
# todoList.py - This program is a simple To Do List in the command line. It reads a list
#   from a text file and lets you add, delete, and set a task as complete.


# Get text file containing todo list
todoFile = open('todo.txt')
todoItems = todoFile.readlines()

# Print todo list
print('------- To Do List -------')
for i in range(len(todoItems)):

    # Remove end line text from items
    if todoItems[i].endswith('\n'):
        todoItems[i] = todoItems[i].split('\n')[0]  

    print(str(i) + ': ' + todoItems[i])


# Ask user what they want to do (add, delete, complete)
# TODO: make this a while loop to keep adding/deleting/completing items
print()
print('To add an item: "add (item)"')
print('To delete an item: "del (item)"')
print('To complete an item: "comp (item)"')
print('To print the list again: "print"')

# Save todo list
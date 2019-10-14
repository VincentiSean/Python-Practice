#! python3
# todoList.py - This program is a simple To Do List in the command line. It reads a list
#   from a text file and lets you add, delete, and set a task as complete.


# This function gets the file containing the todo list and prints its contents.
def printList():

    # Get text file containing todo list
    todoFile = open('todo.txt')
    todoItems = todoFile.readlines()

    # Print todo list
    print()
    print('------- To Do List -------')
    for i in range(len(todoItems)):

        # Remove end line text from items
        if todoItems[i].endswith('\n'):
            todoItems[i] = todoItems[i].split('\n')[0]  

        print(str(i + 1) + ': ' + todoItems[i])

def removeExtraText(todoItems):
    for i in range(len(todoItems)):
        # Remove end line text from items
        if todoItems[i].endswith('\n'):
            todoItems[i] = todoItems[i].split('\n')[0]

        # Remove 'Completed ' from completed items
        if todoItems[i].startswith('Completed '):
            todoItems[i] = todoItems[i].split('Completed ')[1]  

    return todoItems

def readItemsFromFile():
    todoFile = open('todo.txt', 'r')        # Open the todo file
    todoItems = todoFile.readlines()   
    todoFile.close()

    return todoItems

# Write new list to file and close the file
def rewriteFile(todoItems):
    todoFile = open('todo.txt', 'w') 
    for item in todoItems:
        todoFile.write(item + '\n')

    todoFile.close()

#### End Functions ####
printList()

# Ask user what they want to do (add, delete, complete)
# TODO: make this a while loop to keep adding/deleting/completing items
userInput = ''
while (userInput != 'quit'):
    print()
    print('To add an item: "add (item)"')
    print('To delete an item: "del (item)"')
    print('To complete an item: "comp (item)"')
    print('To print the list again: "print"')
    print('To quit: "quit"')

    userInput = input()
    if (userInput.startswith('add ')):
        newItem = userInput.split('add ')[1]    # Get the item to add to the list
        todoFile = open('todo.txt', 'a+')       # Get the todo list file in append mode
        todoFile.write(newItem + '\n')          # Add the new item to the file with endline char
        todoFile.close()
    elif (userInput.startswith('del ')):
        itemToDel = userInput.split('del ')[1]  # Get the item to delete from the list
        
        # Get todo list w/no frills
        todoItems = readItemsFromFile()
        todoItems = removeExtraText(todoItems)

        # Verify item is in the list before deleting
        if (itemToDel in todoItems):
            todoItems.remove(itemToDel)
            print('Item removed')
        else:
            print('That was not in the todo list.')

        # Write new list to file and close the file
        rewriteFile(todoItems)

    elif (userInput.startswith('comp ')):
        itemToComplete = userInput.split('comp ')[1]    # Get the item to mark as completed
        
        # Get todo list w/no frills
        todoItems = readItemsFromFile()
        todoItems = removeExtraText(todoItems)

        # Go through all the items searching for the item to mark as 'completed'
        for i in range(len(todoItems)):
            if (itemToComplete == todoItems[i]):
                todoItems[i] = 'Completed ' + todoItems[i]
                print("Completed")

        # Write new list to file and close the file
        rewriteFile(todoItems)
        
    elif (userInput == 'print'):
        printList()
    elif (userInput == 'quit'):
        print('Goodbye!')
    else:
        print('Input was not understood.')
# Save todo list
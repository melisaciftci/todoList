while True:
    # Get user input and strip space chars from it
    user_action= input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action or 'new' in user_action:
        todo=user_action[4:] # todo after 'add'. (slicing)

        '''file = open('todos.txt', 'r')
        todos = file.readlines()
        file.close()'''

        with open('todos.txt', 'r') as file:  # : means indented
            todos = file.readlines()  # no need to close file.

        todos.append(todo + '\n')

        with open('todos.txt', 'w') as file:
            todos = file.writelines(todos)

    elif 'show' in user_action:

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        # new_todos = [item.strip('\n') for item in todos] -> list comprehension

        for index, item in enumerate(todos):
            item = item.strip('\n')
            item = item.title()
            row = f'{index + 1}-{item}'
            print(row)
    elif 'exit' in user_action:
        break
    elif 'edit' in user_action:
        number = int(user_action[5:])
        print(number)
        number = number - 1  # to solve the index issue.

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo: ")
        todos[number] = new_todo + '\n'

        with open('todos.txt', 'w') as file:
            todos = file.writelines(todos)

    elif 'complete' in user_action:
        number = int(user_action[9:])

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(number - 1)

        with open('todos.txt', 'w') as file:
            todos = file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list."
        print(message)

    else:
        print("Command is invalid!")

print('Bye!')
while True:
    # Get user input and strip space chars from it
    user_action= input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + '\n'

            '''file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()'''

            with open('todos.txt', 'r') as file: # : means indented
                todos = file.readlines() # no need to close file.

            todos.append(todo)

            with open('todos.txt', 'w') as file:
             todos = file.writelines(todos)

        case 'show':

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            # new_todos = [item.strip('\n') for item in todos] -> list comprehension

            for index, item in enumerate(todos):
                item = item.strip('\n')
                item = item.title()
                row = f'{index + 1}-{item}'
                print(row)
        case 'exit':
            break
        case 'edit':
            number = int(input("Number of to the todo to edit: "))
            number = number - 1 # to solve the index issue.

            with open('todos.txt', 'r') as file:
                todos=file.readlines()

            new_todo = input("Enter new todo: ").strip() + '\n' # newline character displays todos in some order. Must be used.
            todos[number] = new_todo + '\n'

            with open('todos.txt', 'w') as file:
                todos=file.writelines(todos)

        case 'complete':
            number = int(input("Number of to the todo to complete: "))

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(number - 1)

            with open('todos.txt', 'w') as file:
                todos=file.writelines(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)

        case _:
            print("You entered an unknown command!")
print('Bye!')
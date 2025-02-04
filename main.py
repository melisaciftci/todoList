while True:
    # Get user input and strip space chars from it
    user_action= input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + '\n'

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

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
            number = number - 1
            new_todo = input("Enter new todo: ")

            todos[number] = new_todo
        case 'complete':
            number = int(input("Number of to the todo to complete: "))
            todos.pop(number - 1)
        case _:
            print("You entered an unknown command!")
print('Bye!')
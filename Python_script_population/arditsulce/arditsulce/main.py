import builtins
import time
from functions import get_todos, write_todos # otherwise
#import functions
# and the calling takes place like todos = functions.get_todos() ---->>> modude when is imported

#output to .readlines is a list
#C:\Users\mrokas\Desktop\Python_script_population\arditsulce\arditsulce\
current_time = time.strftime("%b %d, %Y %H:%M:%S")
print(f"Today is {current_time} ")

while True:
    user_action = input('Type add,show,edit, complete or exit:')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = get_todos('todos.txt')
        todos.append(todo + '\n')
        write_todos(todos,'todos.txt'
                    )  # here we do not assign to a variable because the output of the function is None
    elif user_action.startswith('show'): # | is bitwise OR operator so this case can work with two input
         # we assign the content of readlines even if it is an empty text
        todos = get_todos('todos.txt')
        new_todos = [item.strip('\n') for item in todos] # exactly the same as the for loop above and there is no need for an empty list
        for index,item in enumerate(new_todos):
            row = f"{index + 1}. {item.capitalize()}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = get_todos('todos.txt')
            new_todo = input('Enter new todo:')
            todos[number] = new_todo + '\n'
            write_todos( todos,'todos.txt')
        except ValueError:
            print('Your command is not valid ,try again')
            continue # it will go to the beginning of the while loop. it will ignore everything and go back to the beginning
    elif user_action.startswith('complete'):
        try:
            number =int(user_action[9:])
            todos = get_todos('todos.txt')
            todo_to_remove = todos[number - 1].strip('\n') # to remove \n from the list for better printing
            todos.pop(number - 1)
            write_todos(todos,'todos.txt')
            print(f"Todo {todo_to_remove} is removed")
        except IndexError:
            print('try again, no item with that number:')
            continue
    elif 'exit' in user_action:
        break
    else:
        print('Not an option')



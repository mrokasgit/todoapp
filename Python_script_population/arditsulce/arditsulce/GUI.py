import functions
import FreeSimpleGUI as sg

label = sg.Text(" Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key = 'todo')

add_button = sg.Button('Add')


while True:

    window = sg.Window('My To-Do App',
                       layout =[[label], [input_box, add_button]],
                       font = ('Helvetica',10)) # inside the tile of the GUI, definining the window
    event , values = window.read() # to display the window
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n' #value[key]
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break
window.close() # to close the window


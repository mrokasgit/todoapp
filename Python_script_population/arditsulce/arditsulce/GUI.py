import functions
import FreeSimpleGUI as sg

label = sg.Text(" Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key = 'todo')

add_button = sg.Button('Add')

list_box = sg.Listbox(values=functions.get_todos(), key ='todos', enable_events =True, size=[45,10])
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Button('Exit')


layout = [[label], [input_box, add_button],[list_box,edit_button,complete_button],[exit_button]]
window = sg.Window('My To-Do App',
                       layout =layout,
                       font = ('Helvetica',10)) # inside the tile of the GUI, definining the window
while True:
    event , values = window.read() # to display the window
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n' #value[key]
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values = todos) # this will give us the list box.'todos' points to the list box and update it with the todos values
        case 'todos':
            window['todo'].update(value = values['todos'][0]) #--> values is a list and we want to extract the string. with [0] we take the string as first element
        case 'Complete':
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos) # here we update the listbox because it has key value 'todos'
            window['todo'].update(value = '') # here we update input "add" because we use value = 'todo'
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break
window.close() # to close the window


FILEPATH = 'todos.txt'

def get_todos(filepath = FILEPATH):
    with open(filepath, 'r') as file_local:# we read the lines of the file and assign to a variable (initially todos = [], but no need anymore because every time we
            # will update it with new content from the todos.txt
        todos_local = file_local.readlines() # we changed the name so we dont have universal(global) variable naming
    return todos_local

def write_todos(todos_arg, filepath =FILEPATH):
    with open(filepath, 'w') as file: #only with 'w' it will overwrite if i run it again. We write in the same file the content of todos list
        file.writelines(todos_arg)
## here there is no need to "return" anything. the function just makes an alternation of data

if __name__ == '__main__': ## this and below ,will run when i run the functions.py otherwise not
    print('hello')



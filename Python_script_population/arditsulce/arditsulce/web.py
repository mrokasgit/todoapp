import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] +'\n' ##session state is like dictionary opote einai sa na exoume dict['key']
    todos.append(todo)
    functions.write_todos(todos)


##gia na to  trexw paw sto terminal kai dinw command 'streamlit run onoma_efarmoghs.py' kai efoson anoixei de xreiazetai na to xanatrexw enimerwnetai sto browser
st.title("My Todo App")
st.subheader('This is my todo app')
## for simple write stuff
st.write('This app is to increase your productivity')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo) # here key is without "". connecting with variable??
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos) # write the updated todos to todos.txt
        del st.session_state[todo] # to remove also the session state dictionary entry
        st.rerun() # to rerun the script so all changes apply to the web app

st.text_input(label = "Enter a todo", placeholder='Add a new todo...',on_change=add_todo, key='new_todo') #on change to connect with function above, key like in the GUI
# to have visible the session_state dict item on the web app
#st.session_state # to have visible the session_state dict item on the web app
import functions
import FreeSimpleGUI as sg

label = sg.Text(" Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo")

add_button = sg.Button('Add')

window = sg.Window('My To-Do App', layout =[[label], [input_box, add_button]]) # inside the tile of the GUI, definining the window
window.read() # to display the window
window.close() # to close the window


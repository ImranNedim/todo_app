import streamlit as st
#st.set_page_config(layout="wide") #this function to make the web page wide
'''the stream little library to create web apps. Stream.
Leeds is a brand new library that is taking over and it's becoming really popular because it's easy
to create web apps.
'''
import functions

todos = functions.get_todos() #get todo list from fuctions file

def add_todo(): #this function to make user able to add a todo to todos list
    todo=st.session_state["new_todo"] + "\n" #here the word inside [] must be the same with the key in st.text_input
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App") # to see the link on the web write streamlit run web.py on terminal local and to stoap cntr + c
st.header("This is my app")
st.write("This app to increase your <b>prodectivty</b>",unsafe_allow_html=True) # to make blod font <b> the word you want to write</b>",unsafe_allow_html=True

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox: # this if statemnet is used to delete a todo from todos list by clicking checkbox
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo] #here todo match with key in st.checkbox ,,, if we do not write this row an embty checkbox will apear
        st.experimental_rerun() # if we dont use this function we will have to click the check boc twice in oredr to delete the todo
st.text_input(label="enter a todo",placeholder="enter text",
              on_change=add_todo,key='new_todo') #to add space to for writing text label is to add text above the text box place holder to add text inside the text box on change declears what changes will hapean after pressing enter
# st.session_state use this row and reload the web page to see the use of this function
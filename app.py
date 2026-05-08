import streamlit as st

st.title("To-Do List")

if "todos" not in st.session_state:
    st.session_state.todos = []

new_task = st.text_input("Enter task")

if st.button("Add Task"):
    if new_task:
        st.session_state.todos.append(new_task)

for i, task in enumerate(st.session_state.todos):
    st.checkbox(task, key=f"task_{i}")

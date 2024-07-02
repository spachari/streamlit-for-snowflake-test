import streamlit as st

st.title('About Session ...')

st.write(st.session_state)

# session_state is and everytime you do something to the input control, it's value will be recorded in 
# session_state

# {
# "my-button":true
# "my-toggle":false
# }

if st.button("Button", key= "my-button"):
    st.write("You clicked!")

if st.toggle("Toggle", key= "my-toggle"):
    st.write("You toggled!")

st.write(st.session_state)

# You pass a key and automatically the input control's state will be saved in the session state.

# toggle is a stateful state

# button does not save state
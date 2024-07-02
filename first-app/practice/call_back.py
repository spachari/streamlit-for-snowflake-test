import streamlit as st

def on_button_start(msg):
    st.write(f'{msg}, {st.session_state["names"]}')


st.session_state["names"] = "Srinivas"

st.button("Click me!", on_click=on_button_start, args=("Hi",))


# Callback

# callbacks are just, uh, custom, uh, event handlers. You remember an input control, you know, the so-called interactive widgets?

# Throw one single, uh, event that you can programmatically catch in Streamlit.

# And this is usually called the on_change. But for a button, this could be on_click.

# So the way you override, uh, what's happening on this on_click event, uh, is that it follows, uh,

# 1. when you create the button, you have to pass, uh, in the on_click uh, parameter

# the name of a separate Python functions, a function you define for this, button and in the args,

# or you can see you have kV args as well for variable arguments but in the args parameter uh you pass as a tuple different values for the function arguments.

# In this case, as you see here on screen at the bottom, uh, you pass in the wrong click and on button,

# click uh with the message value "Hi".

# Uh, the callback will execute at the beginning of the next page rerun before anything else from your, main level, 
# 
# from a Python file at the main level.

# So in this case, if you, click on a button, uh, the full page rerun is triggered and the function on_button_click is executed.

# First we in the first place with other callbacks.



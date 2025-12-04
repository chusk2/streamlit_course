import streamlit as st

st.write('### Callbacks and *session_state* values')

st.divider()

state = st.session_state
if 'counter' not in state:
    state.counter = 0

def increase_counter(step):
    state.counter += step
    st.write(f'Counter increased {step} unit(s)')
    st.write(f'Current value of counter is: {state.counter}')

def reset():
    state.counter = 0
    st.write('Counter value reset to zero!')

st.write(f'Current value of counter: {state.counter}')

col1, col2, col3 = st.columns([2,1,1])

with col1:
    step_value = st.slider('Step of increment', min_value = 1, max_value = 10, step = 1)

with col2:
    st.button('Increase counter', on_click = increase_counter, args = (step_value,))

with col3:
    st.button('Reset counter', on_click = reset)
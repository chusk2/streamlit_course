import streamlit as st

st.title('My first Streamlit App!')

st.subheader('Checkbox')

conditions_accepted = st.checkbox('I accept the conditions')

if conditions_accepted:
    st.success('✅ Conditions were accepted!')

st.subheader('Toggle')

admin_user = st.toggle("I'm an admin user")
if admin_user:
    st.markdown('User is ***admin***')
else:
    st.markdown('User is a regular user')

st.subheader('Warning, error and success')

if st.toggle('Show a warning...'):
    st.warning('Beware of the dog!')

if st.toggle('Show an error'):
    st.error('Ups! Something went wrong!')

if st.toggle('Sucess'):
    st.success("You've made it")


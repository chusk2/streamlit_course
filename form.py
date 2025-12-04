import streamlit as st

countries = [
    "Argentina",
    "Austria",
    "Bangladesh",
    "Belgium",
    "Brazil",
    "Canada",
    "Chile",
    "China",
    "Colombia",
    "Denmark",
    "Egypt",
    "Finland",
    "France",
    "Germany",
    "Greece",
    "India",
    "Indonesia",
    "Ireland",
    "Italy",
    "Japan",
    "Malaysia",
    "Mexico",
    "Netherlands",
    "Nigeria",
    "Norway",
    "Pakistan",
    "Peru",
    "Philippines",
    "Poland",
    "Portugal",
    "Russia",
    "Saudi Arabia",
    "South Africa",
    "South Korea",
    "Spain",
    "Sweden",
    "Switzerland",
    "Thailand",
    "Turkey",
    "United Arab Emirates",
    "United Kingdom",
    "United States",
]

with st.form('user_sign_in'):

    st.write("Please fill out the form below:")

    form_data = {
        'username': st.text_input('Enter your user name'),

        'email': st.text_input('Enter your email address'),

        'password': st.text_input('Create a password:', type='password'),

        'birth_date': st.date_input('Enter your birth date'),

        'gender': st.radio('Gender:', options=['Male', 'Female', 'Prefer not to say']),

        'country': st.selectbox('Country of origin', options=countries),

        'accept_terms': st.checkbox('Accept the terms')
    }

    submitted = st.form_submit_button("Sign In")

if submitted:
    if form_data['accept_terms']:
        st.write("Form submitted successfully!")
        st.write("Here is the data you entered:")
        st.json(form_data)
    else:
        st.warning('You have to accept the terms in order to create your account!')

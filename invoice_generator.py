import streamlit as st

state = st.session_state

st.title('Invoice generator')

with st.form(key = 'form'):

    form_data = {
        'client_name': st.text_input('Client name'),
        'client_tax_id': st.number_input('Client tax id', step=1),
        'client_address': st.text_input('Client address', max_chars=150),
        'invoice_date': st.date_input('Invoice date'),
        'concept': st.text_input('Invoice concept', max_chars=150),
        'quantity': st.number_input('Invoice quantity', min_value=0, step=1),
        'unit_price': st.number_input('Unit price', min_value=0),
        'vat_percentage': st.number_input('VAT %'),
        'discount': st.number_input('Discount %', min_value=0, max_value=100),
    }

    submitted = st.form_submit_button('Submit data')

if submitted:
    st.write(form_data)

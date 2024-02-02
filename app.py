import streamlit as st
from PedersonCommitment import generate_key,commitment,  check_point_on_curve

st.title("Pedersen Commitment")
st.subheader('Input Variable')
col1, col2 = st.columns([3,3])

with col1:
    m =  col1.text_input(" ", placeholder="Message (m) ")
    insert = col1.button("Commit")

with col2:
    r = col2.text_input("",placeholder="Randomness (r) ")

    col2.empty()





if insert:
    pedersonCommitment, x,y  = commitment(m,r)
    
    check =check_point_on_curve(pedersonCommitment)
    
   
    st.info(f"X : {x}  \n Y : {y}")
    st.info(f"Commitment Point is on Curve : {(check)}")
    

 

st.divider()


col3, col4 = st.columns(2)
with col3:
    col3.subheader('Generate random Key')

with col4:
    generate= col4.button("Generate")

if generate: 
    public_key=generate_key()
    st.info((bytes(public_key.to_string()).hex()))
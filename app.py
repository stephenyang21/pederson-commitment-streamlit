import streamlit as st
from PedersonCommitment import generate_key,commitment,  check_point_on_curve

st.title("Pedersen Commitment")
st.subheader('Input Variable')
col1, col2 = st.columns([3,3])

with col1:
    m =  col1.text_input("Value", placeholder="Hexadecimal Format")
    insert = col1.button("Commit")

with col2:
    r = col2.text_input("Randomness", placeholder="Hexadecimal Format")

    col2.empty()



if insert:
    pedersonCommitment, x,y  = commitment(m,r)
    check =check_point_on_curve(pedersonCommitment)
    
   
    st.info(f"X : {x}  \n Y : {y}")
    st.info(f"Commitment Point is on Curve : {(check)}")
    

 


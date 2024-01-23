import streamlit as st
from PedersonCommitment import PedersonCommitment

st.title("Pederson Commitment")

message = st.text_input("Message")
secret = st.text_input("Secret")
insert = st.button("Insert")

if insert:
    pedersonCommitment  = PedersonCommitment(security=int(secret),message=int(message))
    
    #SetUp
    pedersonCommitment.pedersen_setup()

    #Commitment
    c,r = pedersonCommitment.pederson_commitment()
    
    st.subheader("Commitment")
    st.markdown(c)

    
    open_message = pedersonCommitment.pedersen_opening(r)
    st.subheader("Open commitment")
    st.markdown(open_message)

    st.info(f"p : {pedersonCommitment.p}  \n q : {pedersonCommitment.q}  \n g : {pedersonCommitment.g}  \n h : {pedersonCommitment.h} ")
 







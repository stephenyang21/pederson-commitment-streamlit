import streamlit as st
from PedersonCommitment import PedersonCommitment

st.title("Pederson Commitment")


message = st.number_input(label="Message", min_value=1, max_value=9999999999999, placeholder="only integer", value=1)
secret = st.slider("Secret", 0, 100)
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
 







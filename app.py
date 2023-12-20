import atreamlit as st
import joblib

#load the joblib model
model_nb=joblib.load('spam_ham)

st.title('SPAMHAM Classifier')
ip=st.text_input('Enter your text:')

np=model_nb.predict([ip])
if st.button('predict'):
  st.title(op[0])

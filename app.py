import pickle
import streamlit as st
import numpy as np

st.title("Flower Classification App")

#file_name="lr_model.pkl"
with open("model.pkl", "rb") as f:
    lr_model=pickle.load(f)

    sl=st.slider("Insert a sepal length",0.0, 10.0)
    sw=st.slider("Insert a sepal width",0.0, 10.0)
    pl=st.slider("Insert a petal length",0.0, 10.0)
    pw=st.slider("Insert a petal width",0.0, 10.0)

    if st.button("Predict"):
        pred=lr_model.predict(np.array([[sl,sw,pl,pw]]))
        st.write("The flower is:",pred[0])
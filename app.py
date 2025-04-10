import streamlit as st # faz interface sem precisar de html - cria app web
import pandas as pd #
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")

modelo = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]

modelo.fit(x, y)

st.title("Prevendo o valor de uma pizza - com Machine learning")
st.divider()

diametro = st.number_input("Digite o tamamho do diametro em centimetros da pizza: ")

if diametro: 
    preco_previsto = modelo.predict([[diametro]])[0][0]

    st.write(f"O valor da pizza com diametro de {diametro:.2f} cm, é de R${preco_previsto:.2f}.")
    st.balloons()
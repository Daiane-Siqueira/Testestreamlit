import streamlit as st
st.write("Sou servidora pública")
st.title("Este é o título do app")
st.header("Este é o subtítulo")
st.subheader("Este é o terceiro subtítulo")
st.markdown("Este é texto")
st.caption("Esta é a a legenda")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

st.slider('Grau de satisfação', 0,100)


import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'nomeServidor': ['Adriana', 'Monica', 'Samara'],
    'salario': [1200,300,5000]
})

st.write("Criando uma tabela!")
st.write(df)
opcao = st.selectbox(
    'Qual servidor você gostaria de selecionar?',
    df['nomeServidor'])

st.write('Você selecionou: ', opcao)

dadosFiltrados = df[df['nomeServidor'] == opcao]
dadosFiltrados

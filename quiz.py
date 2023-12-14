import streamlit as st

st.title('Quiz da Elisa')

import streamlit as st

pontuacao = 0
contador_de_perguntas = 0

st.title('Bem-Vindo(a) ao Quiz da Elisa')
nome = st.text_input("Digite os sue nome:")
if len(nome) > 0:
    st.text(f'olá, {nome}. Vamos começar?')
    st.text('Qual a comida japonesa mais famosa no Brasil?')
    op1 = st.button('Sushi')
    op2 = st.button('Yakissoba')

    
    if op1 == True:
        st.text('Resposta certa')
        pontuacao += 1
        contador_de_perguntas += 1
    elif op2 == True:
        st.text('Resposta errada')
        contador_de_perguntas += 1

    if contador_de_perguntas == 1:
         st.text(f'Seu placar final foi: {pontuacao}')
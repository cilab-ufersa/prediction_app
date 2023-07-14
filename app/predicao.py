import streamlit as st

class Predicao:
    def __init__(self):
        st.set_page_config(
            initial_sidebar_state='collapsed',
            page_title="Hipotireoidismo",
            page_icon='app/icon/cilab.png',
            layout="wide",
            )
        self.page()
        
    def page(self):
        self.entradas()

    def entradas(self):
        idade = st.number_input("Idade",min_value=1, max_value=100, value=1, key="age", help="Idade do paciente")
        sexo = st.selectbox("Sexo",("M","F"), key="sex")

        if sexo == "F":
            gravidez = st.selectbox("já teve filhos?",("Não","Sim"), key="pregnancy")
        disturbio = st.selectbox("Possui algum distúrbio da tireoide?", ("Não", "Sim"), key="sick", help="Se o paciente possui algum distúrbio da tireoide já conhecido")
        tsh = st.number_input("TSH",min_value=0.0, max_value=600.0, value=0.0, key="tsh", help="TSH é a sigla para hormônio estimulante da tireoide, que é produzido pela glândula pituitária")
        t3 = st.number_input("T3",min_value=0.0, max_value=11.0, value=0.0, key="t3", help="T3 é a sigla para triiodotironina, que é um hormônio produzido pela glândula tireoide")
        t4 = st.number_input("T4",min_value=0.0, max_value=500.0, value=0.0, key="t4", help="T4 é a sigla para tiroxina, que é um hormônio produzido pela glândula tireoide")
        st.markdown('---')
    
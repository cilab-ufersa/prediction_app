import streamlit as st
from predicao import *

class Main():
    def __init__(self):
        st.set_page_config(
                    initial_sidebar_state='collapsed',
                    page_title="Hipotireoidismo",
                    page_icon='app/icon/cilab.png',
                    layout="wide",
                    )
        
        self.placeholder = st.empty()

        if "page" not in st.session_state:
            st.session_state.page = 0
            
        if st.session_state.page == 0:
            self.home()
        if st.session_state.page == 1:            
            Predicao
            st.button("Voltar",on_click=lambda:self.set_page(0))
    def set_page(self,numero):
        st.session_state.page = numero

    def home(self):
        st.markdown('<style>h1{font-size: 33px;}</style>', unsafe_allow_html=True)
        st.title("Classificação de doenças da tireoide com técnicas de aprendizado de máquina")
        st.markdown('---')
        st.image('app/icon/icon.png')
        st.write("O hipotireoidismo é uma condição em que a glândula tireoide não produz hormônio tireoidiano suficiente, o que pode resultar em uma diminuição do metabolismo e uma série de sintomas associados. A glândula tireoide está localizada na base do pescoço e é responsável por produzir hormônios que regulam o metabolismo do corpo.")

        # idade = st.number_input("Idade",min_value=1, max_value=100, value=1, key="age", help="Idade do paciente")
        # sexo = st.selectbox("Sexo",("M","F"), key="sex")

        # if sexo == "F":
        #   gravidez = st.selectbox("já teve filhos?",("Não","Sim"), key="pregnancy")
        # disturbio = st.selectbox("Possui algum distúrbio da tireoide?", ("Não", "Sim"), key="sick", help="Se o paciente possui algum distúrbio da tireoide já conhecido")
        # tsh = st.number_input("TSH",min_value=0.0, max_value=600.0, value=0.0, key="tsh", help="TSH é a sigla para hormônio estimulante da tireoide, que é produzido pela glândula pituitária")
        # t3 = st.number_input("T3",min_value=0.0, max_value=11.0, value=0.0, key="t3", help="T3 é a sigla para triiodotironina, que é um hormônio produzido pela glândula tireoide")
        # t4 = st.number_input("T4",min_value=0.0, max_value=500.0, value=0.0, key="t4", help="T4 é a sigla para tiroxina, que é um hormônio produzido pela glândula tireoide")
        # st.markdown('---')

        st.header("Realize o diagnóstico utilizando o modelo de inteligência artificial") 
        st.markdown('<style>div.row-widget.stButton > button {margin-left: 45%;}</style>', unsafe_allow_html=True)
        st.markdown('<style>div.row-widget.stButton > button {color: white; background-color: #1E90FF;}</style>', unsafe_allow_html=True)
        st.button("Realizar Diagnóstico",on_click=lambda:self.set_page(1))
        st.markdown('<style>h3{font-size: 15px;}</style>', unsafe_allow_html=True)
        st.subheader("Apoio")
        st.image('app/icon/Ufersa.png', caption='UFERSA', width=70)

if __name__ == '__main__':
    main = Main()
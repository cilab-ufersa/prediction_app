import streamlit as st
import pandas as pd

class Predicao:
    def __init__(self):
        self.page()
        
    def page(self):

        col1, col2, col3 = st.columns([2, 0.5, 2])

        with col1:
            self.entradas()

        with col2:
            pass

        with col3:
            st.header("Métricas do modelo")
            df = pd.read_csv("models/models.csv")
            col_1, col_2, col_3 = st.columns(3)
            col_1.metric("Acurácia", value=str(int(100*df['acuracia']))+"%", help="Acurácia do modelo: indica o quão precisa é a previsão de um modelo")
            col_2.metric("Precisão", value=str(int(100*df['precisao']))+"%", help="Precisão do modelo: indica a capacidade do modelo de prever corretamente os casos em que o paciente tem a doença")
            col_3.metric("Recall", value=str(int(100*df['recall']))+"%", help="Recall do modelo: indica quantos casos em que o paciente tem a doença o modelo conseguiu identificar no conjunto de dados")

            st.markdown('---')
            st.markdown('<style>p{ text-align: justify;, font-weight: bold;}</style>', unsafe_allow_html=True)
            st.warning("**ATENÇÃO**: Embora os resultados de testes e modelos sejam importantes, é fundamental lembrar que eles não devem ser usados como uma única fonte de informação ou como uma decisão definitiva. É essencial que um profissional de saúde utilize seu conhecimento clínico e julgamento para interpretar e avaliar adequadamente esses resultados, garantindo que os pacientes recebam o tratamento mais adequado e seguro.")
            

    def entradas(self):
        st.markdown('<style>h1{font-size: 30px;}</style>', unsafe_allow_html=True)
        st.header("Preencha os campos com os dados solicitados:")
        idade = st.number_input("Idade",min_value=1, max_value=100, value=1, key="age", help="Idade do paciente")
        sexo = st.selectbox("Sexo",("M","F"), key="sex")

        if sexo == "F":
            gravidez = st.selectbox("já teve filhos?",("Não","Sim"), key="pregnancy")
        disturbio = st.selectbox("Possui algum distúrbio da tireoide?", ("Não", "Sim"), key="sick", help="Se o paciente possui algum distúrbio da tireoide já conhecido")
        tsh = st.number_input("TSH *",min_value=0.0, max_value=600.0, value=0.0, key="tsh", help="TSH é a sigla para hormônio estimulante da tireoide, que é produzido pela glândula pituitária")
        t3 = st.number_input("T3 *",min_value=0.0, max_value=11.0, value=0.0, key="t3", help="T3 é a sigla para triiodotironina, que é um hormônio produzido pela glândula tireoide")
        t4 = st.number_input("T4 *",min_value=0.0, max_value=500.0, value=0.0, key="t4", help="T4 é a sigla para tiroxina, que é um hormônio produzido pela glândula tireoide")
        st.markdown('---')
        button_Verify = (tsh == 0) or (t3 == 0) or (t4 == 0)
        if button_Verify:
            st.error("Preencha os campos Obrigatórios! *")
        but1, but2, but3 = st.columns(3)
        with but1:
            st.button("Realizar predição",key="prediction", disabled = button_Verify)
        with but2:
            st.button("Limpar", on_click=lambda: self.limpar(), key="clear")
        with but3:
            pass
    
    def limpar(self):
        st.session_state.age = 1
        st.session_state.sex = "M"
        st.session_state.sick = "Não"
        st.session_state.tsh = 0.0
        st.session_state.t3 = 0.0
        st.session_state.t4 = 0.0

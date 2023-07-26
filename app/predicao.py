import streamlit as st

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
        tsh = st.number_input("TSH",min_value=0.0, max_value=600.0, value=0.0, key="tsh", help="TSH é a sigla para hormônio estimulante da tireoide, que é produzido pela glândula pituitária")
        t3 = st.number_input("T3",min_value=0.0, max_value=11.0, value=0.0, key="t3", help="T3 é a sigla para triiodotironina, que é um hormônio produzido pela glândula tireoide")
        t4 = st.number_input("T4",min_value=0.0, max_value=500.0, value=0.0, key="t4", help="T4 é a sigla para tiroxina, que é um hormônio produzido pela glândula tireoide")
        st.markdown('---')


        but1, but2, but3 = st.columns(3)
        with but1:
            st.button("Realizar predição",key="prediction")
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

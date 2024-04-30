import streamlit as st
import pandas as pd
from utils import get_user_data_hypothyroidism
from sklearn.preprocessing import StandardScaler
import joblib
import lime 
from lime.lime_tabular import LimeTabularExplainer
import streamlit.components.v1 as components

class hypothyroidism:
    def __init__(self, path):
        self.path = path
        self.page()
        
    def page(self):

        col1, col2, col3 = st.columns([2, 0.5, 2])

        with col1:
            self.entradas()

        with col2:
            pass

        with col3:
            st.header("Métricas do modelo")
            df = pd.read_csv("app/models_file/models.csv")
            col_1, col_2, col_3 = st.columns(3)
            col_1.metric("Acurácia", value=str(int(100*df['acuracia']))+"%", help="Acurácia do modelo: indica o quão precisa é a previsão de um modelo")
            col_2.metric("Precisão", value=str(int(100*df['precisao']))+"%", help="Precisão do modelo: indica a capacidade do modelo de prever corretamente os casos em que o paciente tem a doença")
            col_3.metric("Recall", value=str(int(100*df['recall']))+"%", help="Recall do modelo: indica quantos casos em que o paciente tem a doença o modelo conseguiu identificar no conjunto de dados")

            st.markdown('---')
            st.markdown('<style>p{ text-align: justify;, font-weight: bold;}</style>', unsafe_allow_html=True)
            st.warning("**ATENÇÃO**: Embora os resultados de testes e modelos sejam importantes, é fundamental lembrar que eles não devem ser usados como uma única fonte de informação ou como uma decisão definitiva. É essencial que um profissional de saúde utilize seu conhecimento clínico e julgamento para interpretar e avaliar adequadamente esses resultados, garantindo que os pacientes recebam o tratamento mais adequado e seguro.")
            
    def predicao(self, entradas_user):
        model = joblib.load(self.path)        
        scaler = StandardScaler()
        dados_s = scaler.fit_transform(entradas_user.reshape(10, -1))   
        entradas_user = dados_s.reshape(-1, 10)    
        retorno = model.predict(entradas_user)
        entradas_user = scaler.inverse_transform(entradas_user)
        # use lime for explainability
        explainer = LimeTabularExplainer(entradas_user, mode='classification', class_names=['Normal', 'Hypothyroidism'], 
                                         feature_names=["TT4", "TT4_measured", "T4U_measured", "T3_measured", "FTI", "T3", "TSH", "T4U", "pregnant", "I131"])
        
        predict_fn = lambda x: model.predict_proba(x)
        exp = explainer.explain_instance(entradas_user[0], predict_fn, num_features=10, top_labels=1)
        
        # show the results in the streamlit app 
        st.markdown('---')
        st.header("Explicabilidade do modelo")
        st.markdown("Aqui estão as características que mais influenciaram o modelo na decisão:")
        html = exp.as_html()
        html = html.replace("TT4", "T4 Total")
        html = html.replace("T4U", "T4 Livre")
        html = html.replace("pregnant", "Grávida")
        html = html.replace("I131", "Iodo-131")
        html = html.replace("TT4_measured", "Medido TT4")
        html = html.replace("T4U_measured", "Medido T4U")
        html = html.replace("T3_measured", "Medido T3")
        html = html.replace("Prediction", "Previsão")
        html = html.replace("Hypothyroidism", "Hiportireoidismo")
        html = html.replace("probability", "Probabilidade")
        components.html(html, height=500)
        st.markdown('---')
        
        if retorno == 0:
            st.success("Chances de ter hipotireoidismo: BAIXA")
        if retorno == 1:
            st.markdown("<span style='color:red'>Chances de ter hipotireoidismo: ALTA</span>", unsafe_allow_html=True)

    def entradas(self):
        st.markdown('<style>h1{font-size: 30px;}</style>', unsafe_allow_html=True)
        st.header("Preencha os campos com os dados solicitados:")
        gravidez = 0
        gravidezv = st.selectbox("Está grávida?",("Não","Sim"), key="pregnancy")
        if gravidezv == "Sim":
            gravidez = 1
        tsh = st.number_input("TSH *",min_value=0.0, max_value=600.0, value=0.0, key="tsh", help="TSH é a sigla para hormônio estimulante da tireoide, que é produzido pela glândula pituitária")
        t3 = st.number_input("T3 *",min_value=0.0, max_value=20.0, value=0.0, key="t3", help="T3 é a sigla para triiodotironina, que é um hormônio produzido pela glândula tireoide")
        tt4 = st.number_input("T4 Total *",min_value=0.0, max_value=500.0, value=0.0, key="tt4", help="TT4 é a sigla para tiroxina total, que é um hormônio produzido pela glândula tireoide")
        fti = st.number_input("FTI *",min_value=0.0, max_value=1000.0, value=0.0, key="fti", help="FTI é a sigla para índice de tiroxina livre, que é um hormônio produzido pela glândula tireoide")
        t4u = st.number_input("T4 Livre *",min_value=0.0, max_value=20.0, value=0.0, key="t4u", help="Tiroxina livre, que é um hormônio produzido pela glândula tireoide")
        i131 = 0
        i131v = st.selectbox("Já realizou tratamento com Iodo-131 ",("Não","Sim"), key = "i131", help="O tratamento com iodo-131 é um procedimento médico utilizado principalmente para tratar condições da tireoide")
        if i131v =="Sim":
            i131 = 1
        st.markdown('---')
        tt4_measured = 0
        t4u_measured = 0
        t3_measured = 0
        if tt4 != 0.0:
            tt4_measured = 1
        if t4u != 0.0:
            t4u_measured = 1
        if t3 != 0.0:    
            t3_measured = 1

        dados = get_user_data_hypothyroidism(tt4, tt4_measured, t4u_measured, t3_measured, fti, t3, tsh, t4u, gravidez, i131)
        #scaler = StandardScaler()
        #dados_s = scaler.fit_transform(dados.reshape(10, -1))   
        #self.entradas_user = dados_s.reshape(-1, 10)    
        self.entradas_user = dados
        button_Verify = (tsh == 0) or (t3 == 0) or (t4u == 0) or (tt4 == 0) or (fti == 0)
        
        if button_Verify:
            st.error("Preencha os campos Obrigatórios! *")
        but1, but2, but3 = st.columns(3)
        with but1:
            st.button("Realizar predição", on_click=lambda: self.predicao(self.entradas_user),key="prediction", disabled = button_Verify)
        with but2:
            st.button("Limpar", on_click=lambda: self.limpar(), key="clear")
        with but3:
            pass
    
    def limpar(self):
        st.session_state.tsh = 0.0
        st.session_state.t3 = 0.0
        st.session_state.t4 = 0.0
        st.session_state.tt4 = 0.0
        st.session_state.fti = 0.0
        st.session_state.t4u = 0.0

import streamlit as st
from euthyroidism import *
class Main():
    def __init__(self):
        st.set_page_config(
                    page_title="Hipotireoidismo",
                    initial_sidebar_state="collapsed",
                    page_icon='app/icon/cilab.png',
                    layout="wide",
                    )

        self.placeholder = st.empty()

        if "page" not in st.session_state:
            st.session_state.page = 0
            
        if st.session_state.page == 0:
            self.home()
        if st.session_state.page == 1:
            euthyroidism(path="Euthyroidism/models/StackingClassifier.sav")
            st.button("Voltar",on_click=lambda:self.set_page(0))
    
    def set_page(self,numero):
        st.session_state.page = numero

    def home(self):
        st.markdown('<style>h1{font-size: 33px;}</style>', unsafe_allow_html=True)
        st.title("Sistema de apoio ao diagnóstico: Síndrome do Eutireoideo doente")
        st.markdown('---')
        st.markdown('<style>h2{font-size: 20px;}</style>', unsafe_allow_html=True)
        st.header("Você sabe o que é a sindrome do Eutireoideo doente?")

        col1, col2 = st.columns(2)
        with col2:
            st.markdown('<style>p{text-align: justify;}</style>', unsafe_allow_html=True)
            st.markdown("""
            A síndrome do doente eutireoideo é uma condição médica que
            afeta a glândula tireoide e pode ser detectada por meio da
            interpretação de resultados de exames, como T4, TSH e T3. No entanto, a
            interpretação subjetiva desses resultados pode tornar o diagnóstico difícil
            para o profissional de saúde. Para ajudar nessa tarefa, um modelo de
            inteligência artificial foi desenvolvido para prever se o paciente tem
            ou não a síndrome com base em seus dados de exame. No entanto, é importante
            lembrar que a inteligência artificial pode apresentar falsos positivos e
            falsos negativos, portanto, seu resultado não deve ser considerado como
            absoluto e não deve substituir o julgamento clínico do profissional de saúde.
            É recomendado que o resultado da inteligência artificial seja interpretado
            com cautela e que o diagnóstico seja confirmado pelo profissional de saúde.
            """)
        with col1:
            st.image('app/icon/icon.png',width=400)
        st.markdown('---')

        st.header("Realize o diagnóstico utilizando o modelo de inteligência artificial") 
        st.button("Realizar Diagnóstico",on_click=lambda:self.set_page(1))  
        st.markdown('---')
        st.markdown('<style>h3{font-size: 15px;}</style>', unsafe_allow_html=True)
        st.subheader("Apoio")
        st.image('app/icon/Ufersa.png', caption='UFERSA', width=70)

if __name__ == '__main__':
    main = Main()
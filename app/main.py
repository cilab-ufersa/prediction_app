import streamlit as st
from hypothyroidism import *

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
            hypothyroidism(path="app/models_file/StackingModel.sav")
            st.button("Voltar",on_click=lambda:self.set_page(0))

    def set_page(self,numero):
        st.session_state.page = numero


    def home(self):
                

        st.markdown(
            """
            <style>
                .title {
                    font-size: 1.5rem;
                    font-weight: bold;
                    color: #333;
                    text-align: center;
                    margin-bottom: 1.5rem;
                }
                .header {
                    font-size: 2rem;
                    font-weight: bold;
                    color: #333;
                    margin-top: 2rem;
                    margin-bottom: 1rem;
                }
                .content {
                    font-size: 1.1rem;
                    color: #555;
                    margin-bottom: 1.5rem;
                }
                .sidebar-header {
                    font-size: 1.5rem;
                    font-weight: bold;
                    color: #333;
                    margin-bottom: 1rem;
                }
                .button {
                    background-color: #4CAF50;
                    color: white;
                    padding: 0.7rem 1.5rem;
                    font-size: 1rem;
                    border: none;
                    border-radius: 4px;
                    cursor: pointer;
                    transition: background-color 0.3s;
                }
                .button:hover {
                    background-color: #45a049;
                }
            </style>
            """,
            unsafe_allow_html=True
        )

        st.title("Detecção de Hipotireoidismo")
        st.markdown("---")

        st.header("Hipotireoidismo")

        col1, col2 = st.columns(2)

        with col1:
            st.image('app/icon/icon.png', width=400)

        with col2:
            st.markdown(
                """
                O hipotireoidismo é uma condição em que a glândula tireoide não produz hormônio tireoidiano suficiente, o que pode resultar em uma diminuição do metabolismo e uma série de sintomas associados. A glândula tireoide está localizada na base do pescoço e é responsável por produzir hormônios que regulam o metabolismo do corpo.
                """
            )

        st.header("Sobre diagnósticos")

        st.markdown(
            """
            O hipotireoidismo é uma disfunção que pode ser diagnosticada através de avaliação clínica, exames físicos para procurar sinais de hipotireoidismo, sintomas do paciente, e histórico médico. Outra maneira de diagnóstico é através de exames laboratoriais, com base em exames de sangue, observando-se os níveis hormonais do TSH, T4 e T3, auxiliados por um fluxograma.
            """
        )

        st.markdown(
            """
            A interpretação dos resultados pode tornar o diagnóstico desafiador para os profissionais de saúde. Com o objetivo de auxiliar nessa questão, um modelo de inteligência artificial foi treinado para prever o diagnóstico do paciente com base em seus níveis hormonais. No entanto, é importante lembrar que a inteligência artificial pode apresentar falsos positivos e falsos negativos; portanto, seu resultado não deve ser considerado absoluto e não deve substituir o julgamento clínico do profissional de saúde. É recomendado que o resultado da inteligência artificial seja interpretado com cautela e que o diagnóstico seja confirmado pelo profissional de saúde.
            """
        )

        st.header("Por que realizar um diagnóstico com inteligência artificial?")

        st.markdown(
            """
            **Precisão:** Modelos de machine learning podem ser treinados com grandes quantidades de dados e aprender padrões complexos que podem não ser prontamente identificados por humanos. Isso pode aumentar a precisão do diagnóstico, especialmente em casos difíceis.
            """
        )

        st.markdown(
            """
            **Detecção precoce:** Em alguns casos, os sintomas iniciais do hipotireoidismo podem ser sutis e difíceis de detectar. A análise precisa de uma inteligência artificial pode ser de grande ajuda em casos como este.
            """
        )

        st.markdown(
            """
            **Disponibilidade:** Um modelo de machine learning pode ser implementado em plataformas de saúde digital, tornando-o acessível para médicos e profissionais de saúde em diferentes locais. Isso é especialmente benéfico em áreas remotas ou com recursos limitados, onde a disponibilidade de especialistas pode ser escassa.
            """
        )

        st.sidebar.header("Realize o diagnóstico utilizando o modelo de inteligência artificial")
        st.sidebar.button("Realizar Diagnóstico", on_click=lambda:self.set_page(1))
        st.markdown("---")
        st.subheader("Apoio")
        st.image('app/icon/Ufersa.png', caption='UFERSA', width=70)

   

if __name__ == '__main__':
    main = Main()

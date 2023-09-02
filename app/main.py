import streamlit as st
from hypothyroidism import *
from euthyroidism import *

class Main():
    def __init__(self):
        st.set_page_config(
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
            euthyroidism(path="models/StackingClassifier.sav")
            st.button("Voltar",on_click=lambda:self.set_page(0))
        if st.session_state.page == 2:
            hypothyroidism()
            st.button("Voltar",on_click=lambda:self.set_page(0))

    def set_page(self,numero):
        st.session_state.page = numero

    def home(self):
        st.markdown('<style>h1{font-size: 33px;}</style>', unsafe_allow_html=True)
        st.title("Classificação de doenças da tireoide com técnicas de aprendizado de máquina")
        st.markdown('---')
        st.header("Hipotireoidismo")
        col1, col2 = st.columns(2)
        with col1:
            st.image('app/icon/icon.png',width=400)
        with col2:
            st.markdown("O hipotireoidismo é uma condição em que a glândula tireoide não produz hormônio tireoidiano suficiente, o que pode resultar em uma diminuição do metabolismo e uma série de sintomas associados. A glândula tireoide está localizada na base do pescoço e é responsável por produzir hormônios que regulam o metabolismo do corpo.")
            st.markdown("O hipotireoidismo primário é a forma mais comum dessa condição, resultando de uma falência da própria glândula tireoide em produzir hormônios suficientes. No entanto, existem outras causas, como o hipotireoidismo central, que ocorre devido a problemas no hipotálamo ou na hipófise, órgãos que desencadeiam a produção hormonal da tireoide. Nesse caso, a origem do distúrbio não está diretamente na glândula tireoide, mas em uma disfunção nos órgãos responsáveis por sua regulação.")
        
        st.header("Sobre diagnósticos")
        st.markdown("O hipotireoidismo é uma disfunção que pode ser diagnóstificada atravez de avaliação clínica, exames físico para procurar sinais de hipotireoidismo, sintomas do paciente, histórico médico. outra maneira de diagnóstico, exames laboratoriais, com base em exames de sangue, observando-se os níveis homonais do TSH, T4, e T3. Auxiliado por um fluxograma.")
        st.image("app/icon/fluxograma.png",width=900)
        st.markdown("A interpretação dos resultados pode tornar o diagnóstico desafiador para os profissionais de saúde. Com o objetivo de auxiliar nessa questão, um modelo de inteligência artificial foi treinado para prever o diagnóstico do paciente com base em seus níveis hormonais. No entanto, é importante lembrar que a inteligência artificial pode apresentar falsos positivos e falsos negativos; portanto, seu resultado não deve ser considerado absoluto e não deve substituir o julgamento clínico do profissional de saúde. É recomendado que o resultado da inteligência artificial seja interpretado com cautela e que o diagnóstico seja confirmado pelo profissional de saúde.")
        
        st.header("Por que realizar um diagnóstico utilizando inteligência artificial?")
        st.markdown("Precisão: Modelos de machine learning podem ser treinados com grandes quantidades de dados e aprender padrões complexos que podem não ser prontamente identificados por humanos. Isso pode aumentar a precisão do diagnóstico, especialmente em casos difíceis.")
        st.markdown("Detecção precoce: Em alguns casos, os sintomas iniciais do hipotireoidismo podem ser sutis e difíceis de detectar. o olhar preciso de uma inteligência artificial pode ser de grande ajuda em casos como este.")
        st.markdown("Disponibilidade: Um modelo de machine learning pode ser implementado em plataformas de saúde digital, tornando-o acessível para médicos e profissionais de saúde em diferentes locais. Isso é especialmente benéfico em áreas remotas ou com recursos limitados, onde a disponibilidade de especialistas pode ser escassa.")
  
        st.markdown('---')
        st.header("Realize o diagnóstico utilizando o modelo de inteligência artificial") 
        st.markdown('<style>div.row-widget.stButton > button {margin-left: 45%;}</style>', unsafe_allow_html=True)
        st.markdown('<style>div.row-widget.stButton > button {color: white; background-color: #1E90FF;}</style>', unsafe_allow_html=True)
        st.button("Realizar Diagnóstico Hipotireoidismo",on_click=lambda:self.set_page(2))
        st.button("Realizar Diagnóstico Eutireoidismo",on_click=lambda:self.set_page(1))
        st.markdown("---")
        st.markdown('<style>h3{font-size: 15px;}</style>', unsafe_allow_html=True)
        st.subheader("Apoio")
        st.image('app/icon/Ufersa.png', caption='UFERSA', width=70)


if __name__ == '__main__':
    main = Main()
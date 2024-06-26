import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler

@st.cache_data
def get_user_data(age, sex, sick, tsh, t3, tt4, t4u, fti):
    """
    Get user data from the form

    Args:
        age (int): age of the patient
        sex (int): sex of the patient 0 for F and 1 for M
        sick (int): sick of the patient 
        tsh (float): TSH of the patient
        t3 (float): T3 of the patient
        tt4 (float): TT4 of the patient
        t4u (float): T4U of the patient
        fti (float): FTI of the patient

    Returns:
        pd.DataFrame: user data
    
    """

    user_data = {"age": age,
                "sex": sex,
                "sick": sick,
                "TSH": tsh,
                "T3": t3,
                "TT4": tt4,
                "T4U": t4u,
                "FTI": fti
                }
    features = pd.DataFrame(user_data, index = [0])
    #print(features.values)
    return features.values

def get_user_data_hypothyroidism(tt4, tt4_measured, t4u_measured, t3_measured, fti, t3, tsh, t4u, gravidez, i131):
    dados = {"TT4": tt4,
               "TT4 measured": tt4_measured,
               "T4U measured": t4u_measured,
               "T3 measured": t3_measured,
               "FTI": fti,
               "T3": t3,
               "TSH": tsh,
               "T4U": t4u,
               "pregnant": gravidez,
               "I131 treatmet" :i131
               }
    features = pd.DataFrame(dados, index = [0])
    return features.values   


def sex_string2int(sex):
    """
        converting sex to int

        Args:
            sex (str): sex of the patient F and M

        returns 0 if patient is F or 1 if patient is M
    """     
    if sex == 'F':
        return int(0)
    else:
        return int(1)

def sick_string2int(sick):
    """
        converting sick to int

        Args:
            sick (str): if patiente have disorder

        returns 0 if patient have some disorder or 1 if patient dont have
    """
    if sick == 'Não':
        return int(0)
    else:
        return int(1)
    
def clear():
    st.cache_data.clear()
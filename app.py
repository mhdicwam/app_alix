# this file is responsible for creating the web page and communicating with streamlit
import sys
from streamlit import cli as stcli

import pandas as pd
import streamlit as st


# TODO : dynamisée le contenu des listes deroulantes par la suite ( recup directement de la bdd)
# dict variable
def main():
    list_marital = ['Seule', 'Veuf', 'Divorce', 'Conjoint pas autonome', 'Conjoint autonome', 'indifférent']
    list_sante = ['mémoire', 'santé', 'surendettement', 'maltraitance', 'internet', 'tuteur', 'rien', 'plus disponible',
                  'pas habitude papier', 'indifférent']
    list_aidant = ['famille proche', 'famille éloignée', 'autre', 'aucun', 'plus disponible', 'indifférent']
    list_patrimoine = ['Faible', 'moyen', 'important', 'gestion pat', 'indifférent']
    list_relation = ['bonnes relations', 'relation tendues', 'admin', 'budget', 'suivi med', 'aucun pb', 'gestion pat',
                     'indifférent']
    dict_marital = {
        "Seule": "A",
        "Veuf": "B",
        "Divorce": "C",
        "Conjoint pas autonome": "D",
        "Conjoint autonome": "E"
    }
    dict_sante = {
        "mémoire": "A",
        "santé": "B",
        "surendettement": "C",
        "maltraitance": "D",
        "internet": "E",
        "tuteur": "F",
        "rien": "G",
        "plus disponible": "H",
        "pas habitude papier": "I"
    }
    dict_aidant = {
        "famille proche": "A",
        "famille éloignée": "B",
        "autre": "C",
        "aucun": "E",
        "indifférent": "Z",
    }
    dict_patrimoine = {
        "famille proche": "A",
        "famille eloignee": "B",
        "autre": "C",
        "aucun": "D",
        "plus disponible": "E",
    }
    dict_relation = {
        "bonnes relations": "A",
        "relation tendues": "B",
        "admin": "C",
        "budget": "D",
        "suivi med": "E",
        "aucun pb": "F",
        "gestion pat": "G"
    }
    # title
    st.title(" this our POC ")

    # select box
    st.sidebar.title('Choose')
    list_contexte = st.sidebar.multiselect('Santé/contexte', list_sante)
    list_variable_situ_perso = st.sidebar.selectbox('Situation perso', list_marital)
    list_aidant = st.sidebar.selectbox('Famille', list_aidant)

    list_patrimoine = st.sidebar.selectbox('Patrimoine', list_patrimoine)
    list_relation = st.sidebar.multiselect('Qualité relation/pb gestion	', list_relation)

    # buttons
    st.button("Click to display the form")

    st.write("txt displayed here ")


if main == '__main__':
    main()

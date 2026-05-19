# Importation de la bibliothèque Streamlit
import streamlit as st

# Titre de l'application
st.title("Bienvenue sur le Calculateur d'IMC")

# Demande du poids en kilogrammes
weight = st.number_input("Entrez votre poids (en kg)", min_value=0.0)

# Choix du format de taille via un bouton radio
status = st.radio("Sélectionnez le format de votre taille :", ('cm', 'm', 'pieds'))

# Initialisation de la variable IMC
bmi = 0

# Si l'utilisateur choisit les centimètres
if status == 'cm':
    height = st.number_input("Entrez votre taille (en cm)", min_value=0.0)
    try:
        bmi = weight / ((height / 100) ** 2)
    except:
        st.warning("Veuillez entrer une taille valide.")

# Si l'utilisateur choisit les mètres
elif status == 'm':
    height = st.number_input("Entrez votre taille (en mètres)", min_value=0.0)
    try:
        bmi = weight / (height ** 2)
    except:
        st.warning("Veuillez entrer une taille valide.")

# Si l'utilisateur choisit les pieds
else:
    height = st.number_input("Entrez votre taille (en pieds)", min_value=0.0)
    try:
        height = height * 0.3048  # Conversion pieds -> mètres
        bmi = weight / (height ** 2)
    except:
        st.warning("Veuillez entrer une taille valide.")

# Affichage du résultat
if bmi:
    st.success(f"Votre IMC est : {bmi:.2f}")
    if bmi < 18.5:
        st.info("Vous êtes en insuffisance pondérale.")
    elif 18.5 <= bmi < 25:
        st.success("Vous avez un poids normal.")
    elif 25 <= bmi < 30:
        st.warning("Vous êtes en surpoids.")
    else:
        st.error("Vous êtes en obésité.")
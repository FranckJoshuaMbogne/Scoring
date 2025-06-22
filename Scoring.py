import streamlit as st

st.set_page_config(page_title="Simulateur de Scoring Crédit - Afrique", page_icon="💳")

st.title("💳 Simulateur de Scoring Crédit Alternatif (Afrique)")
st.markdown("""
Ce simulateur estime votre **score de crédit** basé sur des données alternatives adaptées au contexte africain (Mobile Money, loyer, crédibilité sociale, factures...).
Ce score est indicatif et ne remplace pas une analyse bancaire formelle.
""")

with st.form("formulaire"):
    revenus = st.number_input("Revenu mensuel estimé (FCFA)", 0, 2_000_000, 100_000, step=5000)
    montant_mm = st.number_input("Montant Mobile Money reçu ce mois-ci (FCFA)", 0, 1_000_000, 0, step=5000)
    nb_transactions = st.slider("Nombre moyen de transactions Mobile Money / semaine", 0, 20, 3)
    paiement_loyer = st.selectbox("Paiement régulier du loyer ?", ["Oui", "Non"])
    credibilite_sociale = st.selectbox("Réputation/Crédibilité sociale (références, microcrédits informels)", ["Élevée", "Moyenne", "Faible"])
    paiement_factures = st.slider("Nombre de mois consécutifs avec factures payées à temps", 0, 12, 6)
    anciennete_mm = st.slider("Ancienneté sur Mobile Money (en années)", 0, 10, 2)
    possession_actifs = st.selectbox("Possession d'actifs (téléphone, moto, terrain)", ["Oui", "Non"])
    participation_tontine = st.selectbox("Participation à des groupes d’épargne (tontines)", ["Oui", "Non"])
    submitted = st.form_submit_button("Calculer mon score")

if submitted:
    score = 0
    
    # Revenus mensuels (20 points max)
    if revenus >= 150_000:
        score += 20
    elif revenus >= 75_000:
        score += 10
    else:
        score += 5

    # Montant Mobile Money (15 points max)
    if montant_mm >= 50_000:
        score += 15
    elif montant_mm >= 20_000:
        score += 10
    else:
        score += 5

    # Transactions MM (10 points max)
    if nb_transactions >= 5:
        score += 10
    elif nb_transactions >= 3:
        score += 5

    # Paiement loyer (20 points max)
    if paiement_loyer == "Oui":
        score += 20

    # Crédibilité sociale (15 points max)
    if credibilite_sociale == "Élevée":
        score += 15
    elif credibilite_sociale == "Moyenne":
        score += 8
    else:
        score += 2

    # Paiement factures (10 points max)
    if paiement_factures >= 6:
        score += 10
    elif paiement_factures >= 3:
        score += 5

    # Ancienneté MM (5 points max)
    if anciennete_mm >= 5:
        score += 5
    elif anciennete_mm >= 2:
        score += 3

    # Possession d'actifs (3 points max)
    if possession_actifs == "Oui":
        score += 3

    # Participation tontine (2 points max)
    if participation_tontine == "Oui":
        score += 2

    st.success(f"🎯 Votre score est : {score}/100")

    if score >= 75:
        st.markdown("✅ **Niveau de confiance : Excellent (Profil A)**\nVous êtes éligible à un crédit important.")
    elif score >= 60:
        st.markdown("🟢 **Niveau de confiance : Bon (Profil B)**\nÉligible à un crédit modéré.")
    elif score >= 40:
        st.markdown("🟡 **Niveau de confiance : Moyen (Profil C)**\nÉligible à un petit crédit sous conditions.")
    else:
        st.markdown("🔴 **Niveau de confiance : Faible (Profil D)**\nDonnées insuffisantes pour accorder un crédit.")

    st.markdown("""
    **Conseil :** Pour améliorer votre score, augmentez vos revenus déclarés, la régularité de vos paiements de loyer et factures, et participez aux groupes d’épargne.
    """)

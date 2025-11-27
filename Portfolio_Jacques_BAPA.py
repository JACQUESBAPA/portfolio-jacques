import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
import os # Import nécessaire pour gérer les chemins de fichiers

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="Jacques BAPA | Ingénieur Financier & Développeur",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- STYLE CSS PERSONNALISÉ (Thème Blue FinTech) ---
st.markdown("""
<style>
    /* Titres principaux en Bleu Navy */
    h1, h2, h3 {
        color: #1e3a8a;
    }
    /* Style pour les onglets */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        border-radius: 4px 4px 0px 0px;
        font-weight: 600;
    }
    /* Personnalisation de la Sidebar */
    [data-testid="stSidebar"] {
        background-color: #f8fafc;
        border-right: 1px solid #e2e8f0;
    }
    /* Timeline style helper */
    .timeline-date {
        font-weight: bold;
        color: #1e3a8a;
    }
    .timeline-title {
        font-weight: bold;
        font-size: 1.1em;
    }
    .timeline-company {
        color: #64748b;
        font-style: italic;
    }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR : CONTACT & INFO ---
with st.sidebar:
    st.title("Jacques BAPA")
    st.markdown("**Ingénieur Financier & Développeur**")
    st.image("https://ui-avatars.com/api/?name=Jacques+Bapa&background=1e3a8a&color=fff&size=200", caption="Étudiant ESIGELEC")
    
    st.markdown("---")
    
    st.markdown("### 📞 Contact")
    st.markdown("📍 **Rouen, France**")
    st.markdown("📧 jacques.bapa@groupe-esigelec.org")
    st.markdown("📱 +33(0)7 80 25 50 14")
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/jacques-bapa-aa529a219/)")
    
    st.markdown("---")
    
    st.markdown("### 📥 Téléchargement")
    
    # CORRECTION ICI : Utilisation de __file__ pour éviter l'erreur FileNotFoundError
    # Cela permet d'ouvrir le script actuel quel que soit son nom.
    # Dans un cas réel, remplacez __file__ par le chemin vers votre PDF (ex: "CV_Jacques_BAPA.pdf")
    with open(__file__, "rb") as file: 
        st.download_button(
            label="📄 Télécharger mon CV",
            data=file, 
            file_name="CV_Jacques_BAPA.pdf",
            mime="application/pdf",
            disabled=False # Activé pour que vous puissiez tester le bouton
        )
    st.caption("*Le bouton télécharge ce fichier Python comme exemple en l'absence de PDF réel.*")

# --- SECTION HÉRO ---
col1, col2 = st.columns([2, 1])

with col1:
    st.title("L'Ingénieur au Carrefour de la Finance et de la Tech 🚀")
    st.markdown("""
    **Étudiant Ingénieur - Majeure Marchés Financiers (ESIGELEC)**
    
    Je ne suis pas seulement un financier qui utilise Excel, ni seulement un développeur qui code des sites web.
    Je suis le pont entre ces deux mondes. Je combine la **rigueur du calcul stochastique** avec l'**agilité du développement Full-Stack** pour créer des outils financiers performants et robustes.
    """)
    st.info("🎯 **Objectif :** Mettre à profit ma double compétence (Finance de Marché + Dev Python/Web) au sein d'une équipe de trading, de structuration ou de recherche quantitative.")

with col2:
    # Petit concept art en code (Plotly Indicator)
    fig_gauge = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = 100,
        title = {'text': "Motivation"},
        gauge = {'axis': {'range': [None, 100]}, 'bar': {'color': "#1e3a8a"}}
    ))
    fig_gauge.update_layout(height=250, margin=dict(l=20, r=20, t=50, b=20))
    st.plotly_chart(fig_gauge, use_container_width=True)

st.markdown("---")

# --- SECTION COMPÉTENCES (RADAR CHART) ---
st.header("🧬 Mon ADN Professionnel")

col_skills_text, col_skills_chart = st.columns([1, 1])

with col_skills_text:
    st.markdown("### Une Double Compétence Rare")
    st.write("Mon profil se distingue par l'équilibre.")
    
    st.markdown("""
    - **📊 Ingénierie Financière :** Gestion du Risque, Calcul Stochastique, Pricing d'Options/Obligations, VaR.
    - **💻 Tech & Dev :** Python (Data Science), VBA, Full-Stack (Laravel, React), SQL, API.
    - **🤝 Soft Skills :** Discipline (Tennis Compétition), Pédagogie (Professeur), Leadership.
    """)
    
    st.success("💡 **Pourquoi c'est important ?** Je peux comprendre les besoins complexes des traders ET implémenter les solutions techniques sans intermédiaire.")

with col_skills_chart:
    categories = ['Ingénierie Financière', 'Développement Web', 'Data Science/BI', 
                  'Gestion de Risque', 'Langues (Anglais/Français)', 'Soft Skills']
    values = [90, 85, 80, 88, 95, 90]

    fig = go.Figure(data=go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        name='Jacques BAPA',
        line=dict(color='#1e3a8a'),
        fillcolor='rgba(30, 58, 138, 0.2)'
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            )),
        showlegend=False,
        margin=dict(l=40, r=40, t=20, b=20),
        height=350
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# --- SECTION PROJETS (INTERACTIVE TABS) ---
st.header("🛠️ Projets Réalisés")
st.markdown("Explorez mes projets sous deux angles : **Business** (Finance) ou **Technique** (Code).")

# Projet 1
with st.container():
    st.subheader("1. Gestion de Portefeuilles Financiers")
    
    tab_fin, tab_tech = st.tabs(["💼 Vision Finance (Business)", "💻 Vision Tech (Code)"])
    
    with tab_fin:
        st.markdown("""
        *Focus : Asset Management & Performance*
        - **Suivi Multi-Actifs :** Gestion centralisée d'actions, obligations et fonds.
        - **Analyse de Performance :** Calculs de rendements historiques et volatilité.
        - **Allocation d'Actifs :** Outil visuel pour optimiser la diversification sectorielle et géographique.
        - **Aide à la décision :** Tableaux de bord pour le rééquilibrage stratégique.
        """)
        
    with tab_tech:
        st.markdown("""
        *Stack : Laravel (PHP), MySQL, JS*
        - **Architecture MVC :** Code modulaire et maintenable.
        - **Base de Données Relationnelle :** Schéma complexe pour gérer les historiques de prix et transactions.
        - **Data Visualization :** Intégration de librairies JS pour les graphiques dynamiques.
        - **Sécurité :** Gestion des authentifications et protection des données sensibles.
        """)

st.markdown("---")

# Projet 2
with st.container():
    st.subheader("2. Simulateur de Portefeuille Obligataire")
    
    tab_fin2, tab_tech2 = st.tabs(["📉 Vision Finance (Quant)", "🐍 Vision Tech (Algo)"])
    
    with tab_fin2:
        st.markdown("""
        *Focus : Fixed Income & Risk Management*
        - **Pricing :** Valorisation d'obligations et calcul du Yield to Maturity (YTM).
        - **Indicateurs de Risque :** Calcul automatisé de la **Duration**, Convexité et Sensibilité.
        - **Stress Tests :** Simulation de chocs de taux (+/- 100bps) et impact sur le P&L.
        - **Value-at-Risk (VaR) :** Estimation des pertes potentielles.
        """)
        
    with tab_tech2:
        st.markdown("""
        *Stack : Python, VBA, Web*
        - **Algorithmes Financiers :** Implémentation des formules de mathématiques financières (Cash Flows actualisés).
        - **Simulation :** Logique de calcul performante pour les scénarios de stress.
        - **Interactivité :** Interface permettant de modifier les paramètres de courbe de taux en temps réel.
        """)

st.markdown("---")

# --- SECTION PARCOURS (TIMELINE) ---
st.header("🎓 Parcours & Expériences")

def display_timeline_item(date, title, company, details, icon="🎓"):
    col_date, col_content = st.columns([1, 4])
    with col_date:
        st.markdown(f"<div style='text-align: right;'><span class='timeline-date'>{date}</span><br><span style='font-size: 2em;'>{icon}</span></div>", unsafe_allow_html=True)
    with col_content:
        st.markdown(f"<span class='timeline-title'>{title}</span>", unsafe_allow_html=True)
        st.markdown(f"<span class='timeline-company'>{company}</span>", unsafe_allow_html=True)
        st.markdown(details)

display_timeline_item(
    "2023 - 2026",
    "Diplôme d'Ingénieur en Ingénierie Financière",
    "ESIGELEC - Rouen, France",
    "**Majeure Marchés Financiers.**<br>Cours : Gestion du Risque, Calcul Stochastique, BI, IA, Blockchain."
)

st.divider()

display_timeline_item(
    "Juil - Oct 2025",
    "Stagiaire Développement Full-Stack",
    "Uk Software Company - Birmingham, UK",
    "Développement d'apps Web (Laravel/MySQL), conception d'API performantes et analyse concurrentielle (Tier 1 à Tier 3).",
    icon="💼"
)

st.divider()

display_timeline_item(
    "Mai - Août 2023",
    "Stagiaire Assistant Comptable",
    "Macoria PVC - Douala, Cameroun",
    "Tenue de la comptabilité, rapprochements bancaires et participation aux rituels **Agile/SCRUM**.",
    icon="💼"
)

st.divider()

display_timeline_item(
    "2020 - 2023",
    "Classe Prépa Ingénieur",
    "Prépavogt - Yaoundé, Cameroun",
    "Mathématiques, Statistiques, Physique, Sciences de l'Ingénieur.",
    icon="🎓"
)

# --- FOOTER ---
st.markdown("---")
st.markdown("<center>© 2025 Jacques BAPA - Réalisé avec Streamlit & Python 🐍</center>", unsafe_allow_html=True)
import streamlit as st
import plotly.graph_objects as go
import os

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(
    page_title="Jacques BAPA | Ingénieur Financier & Développeur",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- STYLE CSS PERSONNALISÉ ---
st.markdown("""
<style>
    h1, h2, h3 { color: #1e3a8a; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { height: 50px; white-space: pre-wrap; font-weight: 600; border-radius: 4px 4px 0px 0px; }
    .timeline-date { font-weight: bold; color: #1e3a8a; }
    .timeline-title { font-weight: bold; font-size: 1.1em; }
    .timeline-company { color: #64748b; font-style: italic; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR : CONTACT & INFO ---
with st.sidebar:
    st.title("Jacques BAPA")
    st.markdown("**Ingénieur Financier & Développeur**")
    
    # --- TA PHOTO DE PROFIL ---
    # Assure-toi que "JacquesBAPApdp.jpg" est bien sur GitHub
    profile_pic = "JacquesBAPApdp.jpg"
    
    if os.path.exists(profile_pic):
        st.image(profile_pic, width=200)
    else:
        # Image par défaut si ta photo ne s'affiche pas encore
        st.image("https://ui-avatars.com/api/?name=Jacques+Bapa&background=1e3a8a&color=fff&size=200")
    
    st.caption("Étudiant ESIGELEC")
    
    st.markdown("---")
    
    # --- CONTACT ---
    st.markdown("### 📞 Contact")
    st.markdown("📍 **Rouen, France**")
    st.markdown("📧 jacques.bapa@groupe-esigelec.org")
    st.markdown("📱 +33(0)7 80 25 50 14")
    
    # --- LINKEDIN PREMIUM ---
    st.markdown("""
    <a href="https://www.linkedin.com/in/jacques-bapa-aa529a219/" target="_blank" style="text-decoration: none; color: inherit;">
        <div style="display: flex; align-items: center; gap: 10px; padding: 5px 0;">
            <span style="font-size: 1.2em;">🔗</span>
            <div>
                <span style="font-weight: bold; color: #0077b5;">LinkedIn</span>
                <span style="background-color: #f8c77e; color: #783905; padding: 2px 6px; border-radius: 4px; font-size: 0.7em; font-weight: bold; margin-left: 5px;">PREMIUM</span>
                <br>
                <span style="font-size: 0.8em; color: #64748b;">🟢 Profil Ouvert (Message gratuit)</span>
            </div>
        </div>
    </a>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 📥 Téléchargement")
    
    # --- CV PDF ---
    pdf_file_path = "CV_Jacques_BAPA.pdf"
    
    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as file:
            st.download_button(
                label="📄 Télécharger mon CV",
                data=file,
                file_name="CV_Jacques_BAPA.pdf",
                mime="application/pdf"
            )
    else:
        st.warning("Le fichier CV n'est pas encore en ligne.")
        st.download_button("📄 CV Indisponible", data=b"", disabled=True)

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
    - **📊 Ingénierie Financière :** Gestion du Risque, Calcul Stochastique, Pricing, VaR.
    - **💻 Tech & Dev :** Python, VBA, Full-Stack (Laravel, React), SQL.
    - **🤝 Soft Skills :** Discipline (Tennis), Pédagogie, Leadership.
    """)

with col_skills_chart:
    categories = ['Ingénierie Fi.', 'Dev Web', 'Data Science', 'Risque', 'Anglais', 'Soft Skills']
    values = [90, 85, 80, 88, 95, 90]
    fig = go.Figure(data=go.Scatterpolar(
        r=values, theta=categories, fill='toself', name='Jacques BAPA',
        line=dict(color='#1e3a8a'), fillcolor='rgba(30, 58, 138, 0.2)'
    ))
    fig.update_layout(polar=dict(radialaxis=dict(visible=True, range=[0, 100])), showlegend=False, height=350, margin=dict(l=40, r=40, t=20, b=20))
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")

# --- SECTION PROJETS ---
st.header("🛠️ Projets Réalisés")
st.markdown("Explorez mes projets sous deux angles : **Business** (Finance) ou **Technique** (Code).")

with st.container():
    st.subheader("1. Gestion de Portefeuilles Financiers")
    tab_fin, tab_tech = st.tabs(["💼 Vision Finance", "💻 Vision Tech"])
    with tab_fin:
        st.markdown("""
        - **Suivi Multi-Actifs :** Gestion centralisée d'actions et fonds.
        - **Performance :** Calculs de rendements et volatilité.
        - **Allocation :** Optimisation sectorielle et géographique.
        """)
    with tab_tech:
        st.markdown("""
        - **Stack :** Laravel (PHP), MySQL, JS.
        - **Architecture MVC :** Code modulaire.
        - **Data Viz :** Graphiques dynamiques JS.
        """)

st.markdown("---")

with st.container():
    st.subheader("2. Simulateur Obligataire")
    tab_fin2, tab_tech2 = st.tabs(["📉 Vision Quant", "🐍 Vision Algo"])
    with tab_fin2:
        st.markdown("""
        - **Pricing :** Calcul du Yield to Maturity (YTM).
        - **Risque :** Duration, Convexité, Sensibilité.
        - **VaR :** Simulation de stress tests (+/- 100bps).
        """)
    with tab_tech2:
        st.markdown("""
        - **Stack :** Python, VBA, Streamlit.
        - **Algo :** Implémentation de cash flows actualisés.
        - **Simulation :** Calcul temps réel.
        """)

st.markdown("---")

# --- SECTION PARCOURS ---
st.header("🎓 Parcours & Expériences")

def display_timeline_item(date, title, company, details, icon="🎓"):
    col_date, col_content = st.columns([1, 4])
    with col_date:
        st.markdown(f"<div style='text-align: right;'><span class='timeline-date'>{date}</span><br><span style='font-size: 2em;'>{icon}</span></div>", unsafe_allow_html=True)
    with col_content:
        st.markdown(f"<span class='timeline-title'>{title}</span>", unsafe_allow_html=True)
        st.markdown(f"<span class='timeline-company'>{company}</span>", unsafe_allow_html=True)
        st.markdown(details)

display_timeline_item("2023 - 2026", "Diplôme d'Ingénieur Finance", "ESIGELEC - Rouen", "**Majeure Marchés Financiers.**<br>Gestion du Risque, Calcul Stochastique.")
st.divider()
display_timeline_item("Juil - Oct 2025", "Stagiaire Full-Stack", "Uk Software Company - UK", "Développement Web Laravel/MySQL, API.", icon="💼")
st.divider()
display_timeline_item("Mai - Août 2023", "Assistant Comptable", "Macoria PVC - Cameroun", "Comptabilité et méthode Agile/SCRUM.", icon="💼")
st.divider()
display_timeline_item("2020 - 2023", "Classe Prépa", "Prépavogt - Cameroun", "Maths, Physique, SI.", icon="🎓")

st.markdown("---")
st.markdown("<center>© 2025 Jacques BAPA - Portfolio Interactif</center>", unsafe_allow_html=True)

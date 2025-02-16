# Import de Streamlit
import streamlit as st

#Debut du Streamlit
st.set_page_config(page_title="Trafic vélo à Paris")
st.title("Trafic vélo à Paris :bicyclist:")


#Sidebar
#st.sidebar.title("Navigation")
pages=["Introduction", "Equipe", "Cadre du projet", "Nos axes d'analyse", "Clustering", "Conclusion", 'Tests']
page=st.sidebar.radio("Aller vers", pages)

#Page Introduction
if page=="Introduction":
    st.write("## Introduction")
    """Paris est une ville où la mobilité douce occupe une place centrale dans les politiques publiques. Elle est engagée dans une transformation urbaine accélérée, avec pour objectif de réduire la pollution et d’améliorer la qualité de vie de ses habitants.\n La capitale française, avec ses rues emblématiques investit massivement sur son ambition de devenir une référence mondiale en promouvant l’usage du vélo comme mode de transport quotidien. \n Le Plan Vélo, c’est 150 millions d’euros au budget 2015-2020 du département ainsi que 250 millions d’euros pour 2021-2026. Il prévoit sur cette seconde période, la création de 180 km de pistes cyclables supplémentaires, la sécurisation des intersections dangereuses et le développement d’infrastructures adaptées et illustre pleinement l’ambition de la ville.\n
Cependant, malgré ces investissements significatifs, des défis subsistent pour comprendre et optimiser les conditions favorisant l’utilisation du vélo dans la ville.\n
Ce projet d’étude a donc pour objectif d’avancer sur cette question cruciale : quels sont les facteurs déterminants qui encouragent ou freinent l’usage du vélo dans une ville comme Paris ?
En particulier, l’impact des facteurs suivants mérite d’être étudié :\n
Les caractéristiques socio-économiques des quartiers, telles que la densité de population et la présence d’entreprises, de commerces, \n
La présence de zones touristiques dans la ville,\n
L’accès aux infrastructures cyclables, telles que les pistes sécurisées ou les zones de stationnement pour vélos,\n
Les politiques publiques, comme les restrictions ou  incitations financières sur les véhicules motorisés,\n
etc...\n
En approfondissant ces aspects, nous espérons mettre en lumière des outils pouvant être travailler pour contribuer à l’atteinte des objectifs de la mairie de Paris et à l’amélioration des différents endroits cyclables de la ville.
"""

#Page Equipe
if page=='Equipe':
    st.write("## Equipe")
    st.write("Notre équipe, composée de quatre passionnés de données, habite en Ile-de-France et pour moitié directement dans Paris. Elle est donc directement concernée par la politique de la ville, dans le cadre de son lieu d’habitation et/ou dans ses déplacements personnels et professionnels.")

    row1 = st.columns(2)
    row2 = st.columns(2)

    row1[0].title(":lion_face:")
    row1[0].markdown("**Eloy**")
    row1[0].text("This is me and I am a student at Ecole Polytechnique")

    row1[1].title(":fox_face:")
    row1[1].markdown("**Erick**")
    row1[1].text("Psychologue social de formation. Avant dans les études de marché et je fais une reconversion en data analyst.")

    row2[0].title(":squid:")
    row2[0].markdown("**Philippe**")
    row2[0].text("This is me and I am a student at Ecole Polytechnique")

    row2[1].title(":parrot:")
    row2[1].markdown("**Delphine**")
    row2[1].text("This is me and I am a student at Ecole Polytechnique")

#Page Cadre du projet
if page=='Cadre du projet':
    """Le projet s’inscrit dans le cadre du cours de Data Science de l’Ecole Polytechnique, enseigné par le Professeur Alexandre GRAMFORT. Il a pour objectif de mettre en pratique les connaissances acquises pendant le cours, en appliquant les méthodes et outils de la Data Science à un problème concret.\n"""

if page=="Tests":
    def example():
        st.write("This is the main container")
        
        with bottom():
            st.write("This is the bottom container")
            st.text_input("This is a text input in the bottom container")
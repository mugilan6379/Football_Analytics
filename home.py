import streamlit as st
import pandas as pd
import altair as alt

import convertionRate
import goalsXG
import linearRegression

st.title('Striker Analysis')
main_file=pd.read_csv('StrikerAnalysis.csv')


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


local_css("styles.css")
def modify_file(main_file):
    main_file=main_file[(main_file['Year']>=2018)]
    #top 4 leagues only
    main_file=main_file[
        (main_file['League']=='La Liga') | 
        (main_file['League']=='Premier League') |
        (main_file['League']=='Bundesliga') |
        (main_file['League']=='Serie A')
    ]
    #player_goals = main_file.groupby('Player Names')['Goals'].sum().reset_index()
    main_file=main_file.drop(columns=['Year'])
    return main_file
   
main_file=modify_file(main_file)

tab1,tab2,tab3=st.tabs(['Convertion Rate of Strikers','Goals vs XG','Linear Regression'])

with tab1:
    convertionRate.convertionRateOfStriker(main_file)

with tab2:
    goalsXG.goalsVsXG(main_file)

with tab3:
    linearRegression.linRegression(main_file)


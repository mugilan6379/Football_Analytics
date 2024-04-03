import streamlit as st
import pandas as pd
import altair as alt

import convertionRate
import goalsXG

st.title('Striker Analysis')
main_file=pd.read_csv('StrikerAnalysis.csv')

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

convertionRate.convertionRateOfStriker(main_file)
goalsXG.goalsVsXG(main_file)
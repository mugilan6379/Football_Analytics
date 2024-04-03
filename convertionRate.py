import streamlit as st
import pandas as pd
import altair as alt
import ScatterPlot 

def convertionRateOfStriker(main_file):
    
    sub_file=main_file.loc[:,['Player Names','Goals','convertion rate of shots on target','convertion rate of total shots']]

    sum_of_goals_table=sub_file.groupby('Player Names')['Goals'].sum().sort_values(ascending=False)
    sum_of_goals_table=sum_of_goals_table.head(15)

    convertion_rate=pd.merge(
                        sub_file[['Player Names','convertion rate of shots on target','convertion rate of total shots']],
                        sum_of_goals_table,
                        on='Player Names',
                        how='inner'
                    ).sort_values(by='Goals',ascending=False)


    #convertion_rate=convertion_rate.groupby('Player Names')['convertion rate of shots on target'].sum().reset_index()
    convertion_rate=convertion_rate.groupby('Player Names').agg(
                                {'convertion rate of shots on target':'sum',
                                'convertion rate of total shots':'sum',
                                'Goals':'first'
                                }).reset_index().sort_values(by='Goals',ascending=False)

    st.write('Convertion Rate Table')
    st.write(convertion_rate)
    return st.altair_chart(ScatterPlot.scatter_plot(convertion_rate,'convertion rate of total shots','convertion rate of shots on target'),use_container_width=True)


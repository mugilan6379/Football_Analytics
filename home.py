import streamlit as st
import pandas as pd
import altair as alt

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
#main_file=main_file[main_file['Year']==2018]


def scatter_plot(file,x,y):
     return alt.Chart(file,title='Convertion rate').mark_circle().encode(
        x=x,
        y=y,
        tooltip=[x,y,'Player Names']
    ).interactive()
    
main_file=modify_file(main_file)

#st.altair_chart(scatter_plot(main_file,'convertion rate of shots on target','convertion rate of total shots'),use_container_width=True)
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
st.altair_chart(scatter_plot(convertion_rate,'convertion rate of total shots','convertion rate of shots on target'),use_container_width=True)

# convertion_rate=pd.merge(
#     convertion_rate,
#     sum_of_goals_table,
#     on='Player Names',
#     how='inner'
# ).sort_values(by='Goals',ascending=False)

#goal_filtered=goal_filtered.groupby(['Player Names','convertion rate of shots on target'])['Goals'].sum().sort_values(ascending=False)
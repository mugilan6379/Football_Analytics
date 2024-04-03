import altair as alt

def scatter_plot(file,x,y):
     return alt.Chart(file,title='Convertion rate').mark_circle().encode(
        x=x,
        y=y,
        tooltip=[x,y,'Player Names']
    ).interactive()
import plotly.express as px
import pandas as pd
import plotly.io as pio
pio.kaleido.scope.mathjax = None

def add_text(fig,strings):
    text = ''.join(strings)
    fig.add_annotation(dict(font=dict(color='grey',size=10),
        x=-.037,
        y=1.07,
        showarrow=False,
        align="left",
        text = text,
        textangle=0,
        xanchor='left',
        xref="paper",
        yref="paper"))


infile = '../tmp/temps_over_time.csv'
outfile = '../output/sortd-proportional_time.pdf'
title = "Proportional for kiln run"

df = pd.read_csv(infile)

#df['Date'] = pd.to_datetime(df['date'])

fig = px.scatter(df, x='Time', y='Proportional',  title=title, width=1000, height=600)
fig.update_layout(title_x=0.5)
fig.update_traces(marker_size=3)

fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=-.5,
    x=0
))
fig.update_layout(legend={'title_text':''})
#add_text(fig,subtext)

fig.write_image(outfile)


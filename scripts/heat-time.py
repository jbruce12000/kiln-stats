import plotly.express as px
import pandas as pd
import plotly.io as pio

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
outfile = '../output/sortc-heat_time.pdf'
title = "Elements on per Duty Cycle for run"

df = pd.read_csv(infile)

fig = px.scatter(df, x='Time', y='Heat', title=title, width=1000, height=600,trendline="lowess", trendline_options=dict(frac=0.1),trendline_color_override="red")
fig.update_layout(title_x=0.5)
fig.update_traces(marker_size=3)

fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=-.5,
    x=0
))
fig.update_layout(legend={'title_text':''})

fig.update_layout(
    xaxis = dict(
        tickmode = 'array',
        tickvals = [ x*3600 for x in range(48) ],
        ticktext = [ x for x in range(48) ]
    )
)

fig.write_image(outfile)


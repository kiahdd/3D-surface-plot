# %%
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import chart_studio
chart_studio.tools.set_credentials_file(username='kianahaddadi', api_key='GtvXc3WAHuTMEwz5FyyC')
import chart_studio.plotly as py
import plotly.graph_objects as go

# %%
df1 = pd.read_excel('data.xlsx', sheet_name='r600a')
df2 = pd.read_excel('data.xlsx', sheet_name='r600')
df3 = pd.read_excel('data.xlsx', sheet_name='r601a')
df4 = pd.read_excel('data.xlsx', sheet_name='r1234yf')
df5 = pd.read_excel('data.xlsx', sheet_name='r1234ze(E)')
df6 = pd.read_excel('data.xlsx', sheet_name='r245fa')


# %% plotly figures
x1 = df1.p_lp
y1 = df1.p_hp
z1 = df1[['p[19]', 'b_sys']].values.T
fluid1 = go.Figure(data=[go.Surface(z=z1, x=x1, y=y1)])
#
x2 = df2.p_lp
y2 = df2.p_hp
z2 = df2[['p[19]', 'b_sys']].values.T
#
x3 = df3.p_lp
y3 = df3.p_hp
z3 = df3[['p[21]', 'b_sys']].values.T
#
x4 = df4.p_lp
y4 = df4.p_hp
z4 = df4[['p[21]', 'b_sys']].values.T
#
x5 = df5.p_lp
y5 = df5.p_hp
z5 = df5[['p[21]', 'b_sys']].values.T
#
x6 = df6.p_lp
y6 = df6.p_hp
z6 = df6[['p[21]', 'b_sys']].values.T
#

fig = go.Figure(data=[
    go.Surface(z=z1, x=x1, y=y1, name = 'r600a'),
    go.Surface(z=z2, x=x2, y=y2, showscale=False, opacity=0.9,name="r600" ),
    go.Surface(z=z3, x=x3, y=y3, showscale=False, opacity=0.9, name= "r601a"),
    go.Surface(z=z4, x=x4, y=y4, showscale=False, opacity=0.9, name = "r1234yf"),
    go.Surface(z=z5, x=x5, y=y5, showscale=False, opacity=0.9, name="r1234ze(E)"),
    go.Surface(z=z6, x=x6, y=y6, showscale=False, opacity=0.9, name="r245fa")
])

fig.update_layout(
    title_text='b_sys & p[19]|p[21] VS. p_lp & p_hp',
    height=800,
    width=800
)
#%%
py.plot(fig,filename = 'Nassim', auto_open=True)

#%%

# %%

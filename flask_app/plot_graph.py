import pandas as pd
import numpy as np
import json
import plotly
import plotly.graph_objs as go
import plotly.express as px
import plotly.figure_factory as ff
import json
import os
import pycountry_convert as pc

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
DATA = pd.read_csv(os.path.join(THIS_FOLDER, 'static/data/summary.csv'))
DATA.rename(columns = {'total_confirmed':'총확진자', 'total_cases_per_1m_population':'백만명당 확진자',
                        'total_deaths':'총사망자', 'total_deaths_per_1m_population':'백만명당 사망자', 
                        'population':'인구'}, inplace=True)

def draw_treemap():
    # Numerical columns of DATA
    cols_dd = ['총확진자', '백만명당 확진자','총사망자', '백만명당 사망자','인구']
    # Define which trade will be visible:
    visible = np.array(cols_dd)

    # Define traces and buttons:
    traces = []
    buttons = []
    for value in cols_dd:
        traces.append(go.Treemap(labels = DATA["country"],
                                parents = ["country"]*len(DATA["country"]),
                                values = DATA[value] ))
                

        buttons.append(dict(label=value
                            , method='update'
                            , args=[{'visible':list(visible==value)}
                            , {'title':f"<b>{value}</b>"}]))

    updatemenus = [{'active':0
                    ,'buttons':buttons
                }]


    # Show figure
    fig = go.Figure(data=traces,
                    layout=dict(updatemenus=updatemenus))
    # This is in order to get the first title displayed correctly
    first_title = cols_dd[0]
    fig.update_layout(title=f"2020.01.20 ~ 2021.05.23 국가별 <b>{first_title}</b> 현황")

    treemapJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return treemapJSON
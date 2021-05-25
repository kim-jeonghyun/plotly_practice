from flask import Flask, render_template, request, jsonify
from plot_graph import *


app = Flask(__name__)


@app.route('/')
def index():
    treemapJSON  = draw_treemap()
    return render_template('index.html',plot={'treemap': treemapJSON})

'''
@app.route('/')
def eda():
    treemapJSON  = draw_treemap()
    corr_graphJSON = draw_corr()
    box_graphJSON = draw_boxplot()
    scatter_graphJSON = draw_scatter()
    return render_template('eda.html', plot={'mapgraph': map_graphJSON, 'corrgraph':corr_graphJSON, 'boxgraph':box_graphJSON, 'scatter' :scatter_graphJSON})    
''' 


if __name__ == '__main__':
    app.run(debug=True)

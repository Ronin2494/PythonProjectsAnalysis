#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 17:12:38 2023

@author: deepaksharma
"""

import numpy as np
import pandas as pd
import plotly.express as px
import pyqtgraph as pg
from PyQt5.QtWidgets import QApplication
from plotly.subplots import make_subplots
from plotly.graph_objs import *

# Read in the data
dff = pd.read_csv('/Users/deepaksharma/Desktop/Dataset/netflix_titles.csv')

# Group the data by rating and count the number of instances
z = dff.groupby(['rating']).size().reset_index(name='counts')

# Create the pie chart using Plotly Express
pieChart = px.pie(z, values='counts', names='rating', 
                  title='Distribution of Content Ratings on Netflix',
                  color_discrete_sequence=px.colors.qualitative.Set3)

# Convert the plotly figure to a PyQt5 widget
fig_widget = pg.plot(pieChart, remote=False, autoDownsample=True)

# Create the PyQt5 window and display the widget
app = QApplication([])
win = pg.GraphicsWindow()
layout = pg.LayoutWidget()
layout.addWidget(fig_widget, row=0, col=0)
win.setCentralWidget(layout)
win.show()
app.exec_()







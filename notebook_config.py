# Connection packages
import psycopg2
import os
import sys
# from helpers import db_conn
# from helpers import viz_template_professional

# Manipulations
import pandas as pd
import numpy as np
import re

# Plotting
import plotly_express as px
import plotly.graph_objects as go
import plotly.io as pio

import warnings

# Set Plotly styling for Jupyter notebooks
def apply_plotly_settings():
    pio.renderers.default = 'notebook'
    pio.templates.default = "plotly_white"

# Suppress all warnings
def suppress_warnings():
    warnings.filterwarnings('ignore')

def setup_notebook():
    apply_plotly_settings()
    suppress_warnings()
    pd.set_option('display.max_colwidth', None)

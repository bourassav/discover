# %% All my imports

import pandas as pd
from os import path
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import seaborn as sns
from scipy import stats
import numpy as np

# %% ANCHOR Sources files

src_facebook = path.abspath("../data/raw/FacebookNarcissism.dat")
src_anxiety = path.abspath("../data/raw/Exam Anxiety.dat")
src_festival = path.abspath("../data/raw/DownloadFestival.dat")
src_chick = path.abspath("../data/raw/ChickFlick.dat")


# %%  4.4.8 Putting it all together : a quick tutorial

# Importing the Facebook data
facebook_data = pd.read_csv(src_facebook, sep="\t")

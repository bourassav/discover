# %% All my imports

import pandas as pd
from os import path
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import seaborn as sns
from scipy import stats
import numpy as np
from plotnine import ggplot, aes, geom_line, geom_point

# %% ANCHOR Sources files

src_facebook = path.abspath("../data/raw/FacebookNarcissism.dat")
src_anxiety = path.abspath("../data/raw/Exam Anxiety.dat")
src_festival = path.abspath("../data/raw/DownloadFestival.dat")
src_chick = path.abspath("../data/raw/ChickFlick.dat")


# %%  4.4.8 Putting it all together : a quick tutorial

# Importing the Facebook data
facebook_data = pd.read_csv(src_facebook, sep="\t")

# Just creating the simple graph
# I didn't find the way to jitter the position of the points
fig = px.scatter(
    facebook_data,
    x=facebook_data['NPQC_R_Total'],
    y=facebook_data['Rating'],
    width=650,
    height=650,
    color=facebook_data['Rating_Type'],
    opacity=0.5)
fig.show()

# Lets try with plotnine
# And... It works great!
gg_facebook = ggplot(facebook_data, aes(x="NPQC_R_Total", y="Rating"))
gg_facebook + geom_point(aes(color="Rating_Type"), size=1, position="jitter")


# %% ANCHOR 4.5.1 Graphing relationships: the scatterplot

df_anxiety = pd.read_csv(src_anxiety, sep="\t")
df_anxiety.info()

# I've added labels to the graph, didn't know it was like that
fig = px.scatter(
    df_anxiety,
    x=df_anxiety['Anxiety'],
    y=df_anxiety['Exam'],
    width=650,
    height=650,
    labels={
        "Anxiety":"Exam Anxiety",
        "Exam": "Exam Performance %"
    })

fig.show()

# %% ANCHOR 4.5.2 Adding a funky line

(
    ggplot(
        df_anxiety,
        aes(
            "Anxiety",
            "Exam"
        )
    )
    + geom_point()
)

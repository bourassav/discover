# %% All my imports

import pandas as pd
from os import path
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go
import seaborn as sns
from scipy import stats
import numpy as np
from plotnine import ggplot, aes, geom_line, geom_point, labs, geom_smooth
from plotnine import geom_histogram, geom_boxplot

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
gg_facebook + geom_point(aes(shape="Rating_Type"), size=1, position="jitter")


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

# This is the ggplot version, love plotnine
scat_anxiety = ggplot(df_anxiety, aes("Anxiety", "Exam"))
scat_anxiety + geom_point() + labs(x="Exam Anxiety", y="Exam Performance %")

# %% ANCHOR 4.5.2 Adding a funky line
# From now on, I'm using plotnine

scat_anxiety + geom_point() + geom_smooth(
    method="lm",
    alpha=0.1,
    fill="#448aff",
    color="#448aff") + labs(
        x="Exam Anxiety",
        y="Exam Performance %")

# %% ANCHOR 4.5.3 Grouped scatterplot

scatter = ggplot(df_anxiety, aes(
    "Anxiety",
    "Exam",
    color="Gender"
))

# The order is important fort aesthetics in plotnine
scatter + geom_point() + geom_smooth(aes(fill="Gender"), method="lm")

# %% ANCHOR 4.5.3 Self-test
# Go back to the Facebook narcissism data from the earlier tutorial. Plot a
# graph that shows the pattern in the data using only a line. 

df_facebook = facebook_data


line = ggplot(df_facebook, aes(x="NPQC_R_Total", y="Rating"))
line + geom_smooth(method="lm")


# Plot different coloured lines for the different types of rating (cool,
# fashionable, attractive, glamorous).

# I could've had labs, but which one?
line + geom_smooth(aes(color="Rating_Type"), method="lm", se=False)
line + geom_smooth(
    aes(color="Rating_Type"),
    method="lm",
    se=False) + geom_point(
        aes(color="Rating_Type"),
        position="jitter")

# %% 4.6 Histograms : a good way to spot obvious problems

df_festival = pd.read_csv(src_festival, sep="\t")

# NOTE I haven't find a way to use ggplot opts

histogram = ggplot(df_festival, aes(x="day1"))
histogram + geom_histogram()

(histogram
 + geom_histogram(binwidth=0.4)
 + labs(
     x="Hygiene (Day 1 of Festival)",
     y="Frequency"))

# %% ANCHOR 4.1 Jane superbrain



# %% ANCHOR 4.7 Boxplots (box-whisker diagrams)

boxplot = ggplot(df_festival, aes("gender", "day1"))
boxplot + geom_boxplot() + labs(x="Gender", y="Hygiene (Day 1 of festival)")

# Self-test

df_festival_sorted = df_festival.sort_values(
    by="day1",
    ascending=False).iloc[1:, :]
boxplot = ggplot(df_festival_sorted, aes("gender", "day1"))
boxplot + geom_boxplot() + labs(x="Gender", y="Hygiene (Day 1 of festival)")

# %% ANCHOR 4.2 Janve superbrain

df_zscores = df_festival.copy()
df_zscores['day2'] = df_zscores['day2'].str.replace(' ', '')
df_zscores['day2'] = pd.to_numeric(df_zscores['day2'])
df_zscores['zscore'] = stats.zscore(df_zscores['day2'].dropna())
df_zscores.sort_values('zscore', ascending=False)

# %%

def get_zscore_proportions(serie):
    """From a serie of scores (numeric values), this function returns the
    proportion of zcores above 1.96, 2.58 and 3.29.

    Args:
        serie: pandas serie of numeric values
    """
    zscores = stats.zscore(serie)

    return zscores


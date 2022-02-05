# This file is to try out plotnine, since I know ggplot
# I did the exercices found on this page :
# https://realpython.com/ggplot-python/

# %% Import

from plotnine.data import economics, mpg, huron
from plotnine import ggplot, aes, geom_line, geom_point, geom_bar, stat_bin
from plotnine import geom_boxplot

# %% The dataframe used here

economics.info()

# %% First steps

(
    ggplot(economics)
    + aes(x="date", y="pop")
    + geom_line()
)

ggplot(mpg)

mpg.info()

ggplot(mpg) + aes(x="class", y="hwy")

ggplot(mpg) + aes(x="class", y="hwy") + geom_point()

ggplot(mpg) + aes(x="class") + geom_bar()

ggplot(huron) + aes(x="level") + stat_bin(bins=10) + geom_bar()

ggplot(huron) + aes(x="factor(decade)", y="level") + geom_boxplot()
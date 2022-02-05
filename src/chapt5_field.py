# %% ANCHOR Imports

import pandas as pd
import os
from scipy import stats

# %% ANCHOR Source files

src_rexam = "../data/raw/RExam.dat"

# %% ANCHOR The dataframes

df_rexam = pd.read_csv(src_rexam, sep="\t")

# %% ANCHOR Add a category
# Since I'm not using R, I figured that I should use categorial dtype
# to replace R factors.

df_rexam['uni_new'] = pd.Categorical.from_codes(
    df_rexam['uni'],
    ['Duncetown University',
    'Sussex University'])


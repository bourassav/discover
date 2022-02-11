#!/usr/bin/env python3
# NOTE How do you pass a serie from the command line... is it module's limit?
"""Get a serie of scores and returns proportions of zscores above 1.96, 2.58
and 3.29

Usage:

    python3 side4_field.py 
"""
# %% ANCHOR IMPORTS

import pandas as pd
from scipy.stats import zscores

# %% ANCHOR MAIN

def main(serie):
    get_zscore()


# %% IF NAME

if __name__ == '__main__':
    main(serie)
# %% Imports

from matplotlib.pyplot import draw
import pandas as pd
import numpy as np

# %% ANCHOR 12.1 Categorical data

values = pd.Series([
    'apple',
    'orange',
    'apple',
    'apple'
] * 2)

pd.unique(values)

pd.value_counts(values)

# %% ANCHOR Dimension tables
# In Pandas we talk about categories, not levels like in R

values = pd.Series([0, 1, 0, 0] * 2)
dim = pd.Series(['apple', 'orange'])

print(values,"\n",dim,"\n",dim.take(values))

# %% ANCHOR Categorical type in pandas

fruits = [
    'apple',
    'orange',
    'apple',
    'apple'
] * 2

N = len(fruits)

df = pd.DataFrame({
    'fruit': fruits,
    'basket_id': np.arange(N),
    'count': np.random.randint(3, 15, size=N),
    'weight': np.random.uniform(0, 4, size=N)
    },
    columns=[
        'basket_id',
        'fruit',
        'count',
        'weight'
    ])

print(df)

fruit_cat = df['fruit'].astype('category')

print(f"This is : \n{fruit_cat}")
c = fruit_cat.values
print(f"This is the values : \n {c}")
print(type(c))
print(c.codes)

my_categories = pd.Categorical(['foo', 'bar', 'baz', 'foo', 'bar'])

categories = ['foo', 'bar', 'baz']
codes = [0, 1, 2, 0, 0, 1]

my_cats_2 = pd.Categorical.from_codes(codes, categories)

ordered_cat_2 = pd.Categorical.from_codes(codes, categories, ordered=True)

# %% ANCHOR Computations with Categoricals

np.random.seed(12345)
draws = np.random.randn(1000)
print(draws[:5])
bins = pd.qcut(draws, 4, labels=["Q1", "Q2", "Q3", "Q4"])
print(f"Check out these bins: {bins}")

bins = pd.Series(bins, name='quartile')
results = (
    pd.Series(draws)).groupby(
        bins).agg([
            'count',
            'min',
            'max']).reset_index()

print(results)

# %% ANCHOR Better performance with categoricals

N = 10000000
draws = pd.Series(np.random.randn(N))

labels = pd.Series([
    'foo',
    'bar',
    'baz',
    'qux'] * (N//4))

categories = labels.astype('category')

print(labels.memory_usage())
print(categories.memory_usage())
%time _ = labels.astype('category')

# %% ANCHOR Categorical methods

s = pd.Series(['a', 'b', 'c', 'd'] * 2)
cat_s = s.astype('category')
print(cat_s)
print(cat_s.cat.codes)

actual_categories = ['a', 'b', 'c', 'd', 'e']
cat_s = cat_s.cat.set_categories(actual_categories)
print(cat_s)

print(cat_s.cat.codes)
print(cat_s.cat.categories)
print()
print(cat_s.value_counts())

cat_s3 = cat_s[cat_s.isin(['a', 'b'])]
cat_s3 = cat_s3.cat.remove_unused_categories()
print(cat_s3.value_counts())

# %% ANCHOR Creating dummy variables for modeling


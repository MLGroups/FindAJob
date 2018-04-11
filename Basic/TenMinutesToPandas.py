# -*- coding: utf-8 -*-
# @Time    : 18-3-30下午4:48
# @Author  : 石头人m
# @File    : TenMinutesToPandas.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1.Object Creation
# Series
s = pd.Series([1, 3, 5, np.nan, 6, 8])
# DataFrame
dates = pd.date_range('20180330', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20180330'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(['test', 'train', 'test', 'train']),
                    'F': 'foo'})

# 2.Viewing Data
print(df.head())
print(df.tail(3))
print(df.index)
print(df.columns)
print(df.values)
print(df.describe())
print(df.T)
print(df.sort_index(axis=1, ascending=False))
print(df.sort_values(by='B'))

# 3.Selection
# getting
print(df['A'])
print(df[0:3])
# selection by label
print(df.loc[dates[0]])
print(df.loc[:, ['A', 'B']])
print(df.loc['20180330':'20180402', ['A', 'B']])
print(df.loc['20180330', ['A', 'B']])
print(df.at[dates[0], 'A'])
# selection by position
print(df.iloc[3])
print(df.iloc[3:5, 0:2])
print(df.iloc[[1, 2, 4], [0, 2]])
print(df.iloc[:, 1:3])
print(df.iloc[1, 1])
print(df.iat[1, 1])
# boolean indexing
print(df[df.A > 0])
print(df[df > 0])
df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print(df2)
print(df2[df2['E'].isin(['two', 'four'])])
# setting
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
df['F'] = s1
df.at[dates[0], 'A'] = 0
df.iat[0, 1] = 0
df.loc[:, 'D'] = np.array([5] * len(df))
print(df)
df2 = df.copy()
df2[df2 > 0] = -df2

# 4.Missing Data
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1
print(df1)
print(df1.dropna(how='any'))
print(df1.fillna(value=5))
print(pd.isna(df1))

# 5.Operations
# stats
print(df.mean())
print(df.mean(1))
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
print(df.sub(s, axis='index'))
# apply
print(df)
print(df.apply(np.cumsum))  # 累计求和
print(df.apply(lambda x: x.max() - x.min()))
# histogramming
s = pd.Series(np.random.randint(0, 7, size=10))
print(s)
print(s.value_counts())
# string methods
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print(s.str.lower())

# 6.Merge
# concat
df = pd.DataFrame(np.random.randn(10, 4))
pieces = [df[:3], df[3:7], df[7:]]
print(pd.concat(pieces))
# join
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
print(left)
print(right)
print(pd.merge(left, right, on='key'))
# append
df = pd.DataFrame(np.random.randn(8, 4), columns=['A', 'B', 'C', 'D'])
s = df.iloc[3]
print(df.append(s, ignore_index=True))

# 7.Grouping
df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                         'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three',
                         'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})
print(df)
print(df.groupby('A').sum())
print(df.groupby(['A', 'B']).sum())

# 8.Reshaping
# stack
tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                     'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two',
                     'one', 'two', 'one', 'two']]))
print(tuples)
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
print(df)
df2 = df[:4]
print(df2)
stacked = df2.stack()
print(stacked)
print(stacked.unstack())
print(stacked.unstack(1))
print(stacked.unstack(0))
# pivot tables
df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
                   'B': ['A', 'B', 'C'] * 4,
                   'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D': np.random.randn(12),
                   'E': np.random.randn(12)})
print(df)
print(pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C']))

# 9.Time Series
rng = pd.date_range('1/1/2012', periods=100, freq='S')
print(rng)
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
print(ts)
print(ts.resample('5Min').sum())

rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
print(rng)
ts = pd.Series(np.random.randn(len(rng)), rng)
print(ts)
ts_utc = ts.tz_localize('UTC')
print(ts_utc)
print(ts_utc.tz_convert('US/Eastern'))

rng = pd.date_range('1/1/2012', periods=5, freq='M')
print(rng)
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts)
ps = ts.to_period()
print(ps)
print(ps.to_timestamp())

prng = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')
ts = pd.Series(np.random.randn(len(prng)), prng)
ts.index = (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9
print(ts.head())

# 10.Categoricals
df = pd.DataFrame({"id": [1, 2, 3, 4, 5, 6], "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']})
print(df)
df["grade"] = df["raw_grade"].astype("category")
print(df['grade'])
df["grade"].cat.categories = ["very good", "good", "very bad"]
df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
print(df['grade'])
print(df.sort_values(by="grade"))
print(df.groupby("grade").size())

# 11.Plotting
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
ts = ts.cumsum()
ts.plot()
plt.show()
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index,
                  columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
plt.figure()
df.plot()
plt.legend(loc='best')
plt.show()

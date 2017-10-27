import pandas as pd

s1 = pd.Series([1, 2], index=['a', 'b'])

print s1.loc['a']

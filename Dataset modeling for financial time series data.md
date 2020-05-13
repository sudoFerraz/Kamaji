
# Dataset modeling for Financial Time Series Data
This document aims to provide information on the research related to find the best format to represent financial time series data with certain data analysis for the usage of machine learning techniques

## On the data provided - Overview


```python
%matplotlib inline

import pandas as pd
import pandas_datareader as web
from IPython.core.display import display
import matplotlib.pylab as plt
from stockstats import StockDataFrame
import seaborn as sns
sns.set()

df = web.DataReader('BRL=X', 'yahoo')
data = pd.DataFrame(df)
data = StockDataFrame.retype(data)
display(data.head())
data.plot(figsize=(15,10))
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>adj close</th>
      <th>volume</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2010-01-04</th>
      <td>1.6930</td>
      <td>1.7412</td>
      <td>1.6723</td>
      <td>1.7190</td>
      <td>1.7190</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2010-01-05</th>
      <td>1.6713</td>
      <td>1.7370</td>
      <td>1.6713</td>
      <td>1.7370</td>
      <td>1.7370</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2010-01-06</th>
      <td>1.6798</td>
      <td>1.7359</td>
      <td>1.6798</td>
      <td>1.7315</td>
      <td>1.7315</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2010-01-07</th>
      <td>1.7242</td>
      <td>1.7472</td>
      <td>1.6805</td>
      <td>1.7389</td>
      <td>1.7389</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2010-01-08</th>
      <td>1.6954</td>
      <td>1.7492</td>
      <td>1.6954</td>
      <td>1.7320</td>
      <td>1.7320</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>





    <matplotlib.axes._subplots.AxesSubplot at 0x10f4d7310>




![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_2_2.png)


## On the indicators


```python
%matplotlib inline

import pandas as pd
import pandas_datareader as web
from IPython.core.display import display
import matplotlib.pylab as plt
from stockstats import StockDataFrame
import seaborn as sns
sns.set()

data = pd.read_csv('USDBRL/all_indicators.csv')
data = StockDataFrame.retype(data)
copy = data.copy()
display(data.tail())
```


<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>adj close</th>
      <th>volume</th>
      <th>close_20_sma</th>
      <th>close_20_mstd</th>
      <th>boll</th>
      <th>boll_ub</th>
      <th>...</th>
      <th>mdi_14</th>
      <th>mdi</th>
      <th>dx_14</th>
      <th>dx</th>
      <th>dx_6_ema</th>
      <th>adx</th>
      <th>adx_6_ema</th>
      <th>adxr</th>
      <th>trix</th>
      <th>trix_9_sma</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2018-01-22</th>
      <td>3.1912</td>
      <td>3.2063</td>
      <td>3.1828</td>
      <td>3.1947</td>
      <td>3.1947</td>
      <td>0.0</td>
      <td>3.25131</td>
      <td>0.045347</td>
      <td>3.25131</td>
      <td>3.342003</td>
      <td>...</td>
      <td>32.424464</td>
      <td>32.424464</td>
      <td>50.393826</td>
      <td>50.393826</td>
      <td>44.705562</td>
      <td>44.705562</td>
      <td>46.145262</td>
      <td>46.145262</td>
      <td>-0.104079</td>
      <td>-0.070007</td>
    </tr>
    <tr>
      <th>2018-01-23</th>
      <td>3.2007</td>
      <td>3.2364</td>
      <td>3.1986</td>
      <td>3.2007</td>
      <td>3.2007</td>
      <td>0.0</td>
      <td>3.24457</td>
      <td>0.042074</td>
      <td>3.24457</td>
      <td>3.328719</td>
      <td>...</td>
      <td>27.456171</td>
      <td>27.456171</td>
      <td>12.093108</td>
      <td>12.093108</td>
      <td>35.387718</td>
      <td>35.387718</td>
      <td>43.071678</td>
      <td>43.071678</td>
      <td>-0.108291</td>
      <td>-0.079818</td>
    </tr>
    <tr>
      <th>2018-01-24</th>
      <td>3.2337</td>
      <td>3.2382</td>
      <td>3.1757</td>
      <td>3.2355</td>
      <td>3.2355</td>
      <td>0.0</td>
      <td>3.24086</td>
      <td>0.039202</td>
      <td>3.24086</td>
      <td>3.319265</td>
      <td>...</td>
      <td>31.174430</td>
      <td>31.174430</td>
      <td>28.154808</td>
      <td>28.154808</td>
      <td>33.321172</td>
      <td>33.321172</td>
      <td>40.285819</td>
      <td>40.285819</td>
      <td>-0.107148</td>
      <td>-0.087835</td>
    </tr>
    <tr>
      <th>2018-01-25</th>
      <td>3.1451</td>
      <td>3.1484</td>
      <td>3.1215</td>
      <td>3.1451</td>
      <td>3.1451</td>
      <td>0.0</td>
      <td>3.23245</td>
      <td>0.040851</td>
      <td>3.23245</td>
      <td>3.314153</td>
      <td>...</td>
      <td>41.194580</td>
      <td>41.194580</td>
      <td>52.070509</td>
      <td>52.070509</td>
      <td>38.678126</td>
      <td>38.678126</td>
      <td>39.826478</td>
      <td>39.826478</td>
      <td>-0.112533</td>
      <td>-0.094800</td>
    </tr>
    <tr>
      <th>2018-01-26</th>
      <td>3.1454</td>
      <td>3.1543</td>
      <td>3.1312</td>
      <td>3.1469</td>
      <td>3.1469</td>
      <td>0.0</td>
      <td>3.22424</td>
      <td>0.040712</td>
      <td>3.22424</td>
      <td>3.305665</td>
      <td>...</td>
      <td>36.821796</td>
      <td>36.821796</td>
      <td>45.967524</td>
      <td>45.967524</td>
      <td>40.760811</td>
      <td>40.760811</td>
      <td>40.093430</td>
      <td>40.093430</td>
      <td>-0.120949</td>
      <td>-0.101018</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 69 columns</p>
</div>


## Handling missing data (Data Cleaning)


```python
#How much of the data is missing
counter_nan = data.isnull().sum().sort_values(ascending=False)
plt.figure(figsize=(15,10))
plt.scatter(counter_nan, counter_nan.values)
plt.show()
```


![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_6_0.png)



```python
#how many columns does not have a single nan
counter_without_nan = counter_nan[counter_nan==0]
print " [+] Number of columns that does not have a nan: " + str(len(counter_without_nan))
print " [+] Number of total columns: " + str(len(data.columns))
```

     [+] Number of columns that does not have a nan: 24
     [+] Number of total columns: 69


###### Much of the encountered NaN are caused from the indicators necessity for previous data


```python
display(data[counter_nan.keys()].head())
```


<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cci_20</th>
      <th>cci</th>
      <th>tr</th>
      <th>high_delta</th>
      <th>um</th>
      <th>low_delta</th>
      <th>dm</th>
      <th>close_-1_d</th>
      <th>cr-ma3</th>
      <th>close_-1_s</th>
      <th>...</th>
      <th>kdjk_9</th>
      <th>close_10_sma</th>
      <th>macds</th>
      <th>close_50_sma</th>
      <th>dma</th>
      <th>pdm</th>
      <th>pdm_14_ema</th>
      <th>pdm_14</th>
      <th>macdh</th>
      <th>macd</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2010-01-04</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>55.926463</td>
      <td>1.719000</td>
      <td>0.000000</td>
      <td>1.719000</td>
      <td>0.0</td>
      <td>0.0000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>2010-01-05</th>
      <td>66.666667</td>
      <td>66.666667</td>
      <td>0.0657</td>
      <td>-0.0042</td>
      <td>0.0000</td>
      <td>-0.0010</td>
      <td>0.001</td>
      <td>0.0180</td>
      <td>NaN</td>
      <td>1.7190</td>
      <td>...</td>
      <td>68.614781</td>
      <td>1.728000</td>
      <td>0.000224</td>
      <td>1.728000</td>
      <td>0.0</td>
      <td>0.0000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000359</td>
      <td>0.000404</td>
    </tr>
    <tr>
      <th>2010-01-06</th>
      <td>60.363636</td>
      <td>60.363636</td>
      <td>0.0572</td>
      <td>-0.0011</td>
      <td>0.0000</td>
      <td>0.0085</td>
      <td>0.000</td>
      <td>-0.0055</td>
      <td>NaN</td>
      <td>1.7370</td>
      <td>...</td>
      <td>74.450865</td>
      <td>1.729167</td>
      <td>0.000273</td>
      <td>1.729167</td>
      <td>0.0</td>
      <td>0.0000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000141</td>
      <td>0.000344</td>
    </tr>
    <tr>
      <th>2010-01-07</th>
      <td>133.333333</td>
      <td>133.333333</td>
      <td>0.0667</td>
      <td>0.0113</td>
      <td>0.0113</td>
      <td>0.0007</td>
      <td>0.000</td>
      <td>0.0074</td>
      <td>NaN</td>
      <td>1.7315</td>
      <td>...</td>
      <td>79.322096</td>
      <td>1.731600</td>
      <td>0.000376</td>
      <td>1.731600</td>
      <td>0.0</td>
      <td>0.0113</td>
      <td>0.003457</td>
      <td>0.003457</td>
      <td>0.000400</td>
      <td>0.000576</td>
    </tr>
    <tr>
      <th>2010-01-08</th>
      <td>106.533036</td>
      <td>106.533036</td>
      <td>0.0538</td>
      <td>0.0020</td>
      <td>0.0020</td>
      <td>0.0149</td>
      <td>0.000</td>
      <td>-0.0069</td>
      <td>NaN</td>
      <td>1.7389</td>
      <td>...</td>
      <td>78.854868</td>
      <td>1.731680</td>
      <td>0.000387</td>
      <td>1.731680</td>
      <td>0.0</td>
      <td>0.0020</td>
      <td>0.003077</td>
      <td>0.003077</td>
      <td>0.000055</td>
      <td>0.000415</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 69 columns</p>
</div>


###### Erasing equal or all zero columns


```python
from pandas.util.testing import assert_series_equal
import numpy as np

# Taking out columns that have all values as 0 or equal values
data = StockDataFrame.retype(data)
cols = data.select_dtypes([np.number]).columns
diff = data[cols].diff().sum()

data = data.drop(diff[diff==0].index, axis=1)
data = data.drop('adj close', 1)
display(data.tail())

```


<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>close_20_sma</th>
      <th>close_20_mstd</th>
      <th>boll</th>
      <th>boll_ub</th>
      <th>boll_lb</th>
      <th>close_-1_s</th>
      <th>...</th>
      <th>mdi_14</th>
      <th>mdi</th>
      <th>dx_14</th>
      <th>dx</th>
      <th>dx_6_ema</th>
      <th>adx</th>
      <th>adx_6_ema</th>
      <th>adxr</th>
      <th>trix</th>
      <th>trix_9_sma</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2018-01-22</th>
      <td>3.1912</td>
      <td>3.2063</td>
      <td>3.1828</td>
      <td>3.1947</td>
      <td>3.25131</td>
      <td>0.045347</td>
      <td>3.25131</td>
      <td>3.342003</td>
      <td>3.160617</td>
      <td>3.2051</td>
      <td>...</td>
      <td>32.424464</td>
      <td>32.424464</td>
      <td>50.393826</td>
      <td>50.393826</td>
      <td>44.705562</td>
      <td>44.705562</td>
      <td>46.145262</td>
      <td>46.145262</td>
      <td>-0.104079</td>
      <td>-0.070007</td>
    </tr>
    <tr>
      <th>2018-01-23</th>
      <td>3.2007</td>
      <td>3.2364</td>
      <td>3.1986</td>
      <td>3.2007</td>
      <td>3.24457</td>
      <td>0.042074</td>
      <td>3.24457</td>
      <td>3.328719</td>
      <td>3.160421</td>
      <td>3.1947</td>
      <td>...</td>
      <td>27.456171</td>
      <td>27.456171</td>
      <td>12.093108</td>
      <td>12.093108</td>
      <td>35.387718</td>
      <td>35.387718</td>
      <td>43.071678</td>
      <td>43.071678</td>
      <td>-0.108291</td>
      <td>-0.079818</td>
    </tr>
    <tr>
      <th>2018-01-24</th>
      <td>3.2337</td>
      <td>3.2382</td>
      <td>3.1757</td>
      <td>3.2355</td>
      <td>3.24086</td>
      <td>0.039202</td>
      <td>3.24086</td>
      <td>3.319265</td>
      <td>3.162455</td>
      <td>3.2007</td>
      <td>...</td>
      <td>31.174430</td>
      <td>31.174430</td>
      <td>28.154808</td>
      <td>28.154808</td>
      <td>33.321172</td>
      <td>33.321172</td>
      <td>40.285819</td>
      <td>40.285819</td>
      <td>-0.107148</td>
      <td>-0.087835</td>
    </tr>
    <tr>
      <th>2018-01-25</th>
      <td>3.1451</td>
      <td>3.1484</td>
      <td>3.1215</td>
      <td>3.1451</td>
      <td>3.23245</td>
      <td>0.040851</td>
      <td>3.23245</td>
      <td>3.314153</td>
      <td>3.150747</td>
      <td>3.2355</td>
      <td>...</td>
      <td>41.194580</td>
      <td>41.194580</td>
      <td>52.070509</td>
      <td>52.070509</td>
      <td>38.678126</td>
      <td>38.678126</td>
      <td>39.826478</td>
      <td>39.826478</td>
      <td>-0.112533</td>
      <td>-0.094800</td>
    </tr>
    <tr>
      <th>2018-01-26</th>
      <td>3.1454</td>
      <td>3.1543</td>
      <td>3.1312</td>
      <td>3.1469</td>
      <td>3.22424</td>
      <td>0.040712</td>
      <td>3.22424</td>
      <td>3.305665</td>
      <td>3.142815</td>
      <td>3.1451</td>
      <td>...</td>
      <td>36.821796</td>
      <td>36.821796</td>
      <td>45.967524</td>
      <td>45.967524</td>
      <td>40.760811</td>
      <td>40.760811</td>
      <td>40.093430</td>
      <td>40.093430</td>
      <td>-0.120949</td>
      <td>-0.101018</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 66 columns</p>
</div>


###### Slicing the index gives us a pretty simple solution with minimum data miss for the indicator necessity on previous data




```python
data = data[14:-14]
counter_nan = data.isnull().sum().sort_values(ascending=False)
display(data[counter_nan.keys()].head())
plt.figure(figsize=(15,10))
plt.scatter(counter_nan, counter_nan.values)
plt.show()
print " [+] Number of columns that does not have a nan: " + str(len(counter_nan))
print " [+] Number of total columns: " + str(len(data.columns))
```


<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>cci_20</th>
      <th>cci</th>
      <th>low_delta</th>
      <th>um</th>
      <th>high_delta</th>
      <th>tr</th>
      <th>close_-1_d</th>
      <th>dm</th>
      <th>wr_6</th>
      <th>open</th>
      <th>...</th>
      <th>mdm_14</th>
      <th>mdi_14</th>
      <th>trix</th>
      <th>kdjj</th>
      <th>kdjj_9</th>
      <th>kdjd</th>
      <th>kdjd_9</th>
      <th>kdjk</th>
      <th>kdjk_9</th>
      <th>trix_9_sma</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2010-01-22</th>
      <td>178.996300</td>
      <td>176.807799</td>
      <td>0.0130</td>
      <td>0.0269</td>
      <td>0.0269</td>
      <td>0.0776</td>
      <td>0.0180</td>
      <td>0.0000</td>
      <td>9.292763</td>
      <td>1.7525</td>
      <td>...</td>
      <td>0.001941</td>
      <td>3.085113</td>
      <td>0.143416</td>
      <td>97.528377</td>
      <td>97.528377</td>
      <td>92.856768</td>
      <td>92.856768</td>
      <td>94.413971</td>
      <td>94.413971</td>
      <td>0.083942</td>
    </tr>
    <tr>
      <th>2010-01-25</th>
      <td>128.966672</td>
      <td>124.296506</td>
      <td>0.0130</td>
      <td>0.0000</td>
      <td>-0.0088</td>
      <td>0.0558</td>
      <td>-0.0353</td>
      <td>0.0000</td>
      <td>38.800999</td>
      <td>1.8189</td>
      <td>...</td>
      <td>0.001653</td>
      <td>2.659399</td>
      <td>0.155344</td>
      <td>73.827148</td>
      <td>73.827148</td>
      <td>90.138251</td>
      <td>90.138251</td>
      <td>84.701217</td>
      <td>84.701217</td>
      <td>0.096051</td>
    </tr>
    <tr>
      <th>2010-01-26</th>
      <td>197.350586</td>
      <td>184.521032</td>
      <td>0.0474</td>
      <td>0.0247</td>
      <td>0.0247</td>
      <td>0.0625</td>
      <td>0.0501</td>
      <td>0.0000</td>
      <td>9.117647</td>
      <td>1.8136</td>
      <td>...</td>
      <td>0.001411</td>
      <td>2.269388</td>
      <td>0.172968</td>
      <td>82.362163</td>
      <td>82.362163</td>
      <td>89.027382</td>
      <td>89.027382</td>
      <td>86.805642</td>
      <td>86.805642</td>
      <td>0.110112</td>
    </tr>
    <tr>
      <th>2010-01-27</th>
      <td>170.239369</td>
      <td>148.954115</td>
      <td>-0.0269</td>
      <td>0.0203</td>
      <td>0.0203</td>
      <td>0.0803</td>
      <td>0.0160</td>
      <td>0.0269</td>
      <td>11.533149</td>
      <td>1.7860</td>
      <td>...</td>
      <td>0.005090</td>
      <td>7.953166</td>
      <td>0.195355</td>
      <td>85.874366</td>
      <td>85.874366</td>
      <td>88.576951</td>
      <td>88.576951</td>
      <td>87.676089</td>
      <td>87.676089</td>
      <td>0.125540</td>
    </tr>
    <tr>
      <th>2010-01-28</th>
      <td>166.319888</td>
      <td>142.587103</td>
      <td>0.0204</td>
      <td>0.0049</td>
      <td>0.0049</td>
      <td>0.0648</td>
      <td>0.0184</td>
      <td>0.0000</td>
      <td>2.429765</td>
      <td>1.8064</td>
      <td>...</td>
      <td>0.004363</td>
      <td>6.809581</td>
      <td>0.222101</td>
      <td>94.516229</td>
      <td>94.516229</td>
      <td>89.425419</td>
      <td>89.425419</td>
      <td>91.122356</td>
      <td>91.122356</td>
      <td>0.142624</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 66 columns</p>
</div>



![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_13_1.png)


     [+] Number of columns that does not have a nan: 66
     [+] Number of total columns: 66


###### After slicing we can backfill NaN values for holidays and exceptional days on the market


```python
#Back filling for holidays and exceptional days on the market
data = data.fillna(method='bfill')
data = data[1:-1]
counter_without_nan = data.isnull().sum().sort_values(ascending=False)
print " [+] Number of columns that does not have a nan: " + str(len(counter_without_nan))
print " [+] Number of total columns: " + str(len(data.columns))
```

     [+] Number of columns that does not have a nan: 66
     [+] Number of total columns: 66


## Data Exploring


```python
def plot_histogram(x):
    plt.figure(figsize=(15,10))
    plt.hist(x,  alpha=0.5)
    plt.title("Histogram of '{var_name}'".format(var_name=x.name))
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.show()
```


```python
plot_histogram(data['macdh'])
plot_histogram(data['cci'])
```


![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_18_0.png)



![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_18_1.png)


###### Exploring the distribution of percentage change in the close value


```python
import matplotlib.mlab as mlab

mu = data['close_-1_r'].mean()
sigma = data['close_-1_r'].std()
x = data['close_-1_r']
num_bins = 50
fig, ax = plt.subplots(figsize=(15,10))
n, bins, patches = ax.hist(x, num_bins, normed=1)
y = mlab.normpdf(bins, mu, sigma)
ax.plot(bins, y, '--')
ax.set_title('Histogram of 1-day Change $\mu=' + str(mu) + '$, $\sigma=' + str(sigma) + '$')
plt.show()
```


![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_20_0.png)


###### Making our first label of 1 day future forecast for feature exploration


```python
label_display = pd.DataFrame()
label_display['close'] = data['close']
label_display['from_yesterday_rate'] = data['close_-1_r']
y1 = data['close_-1_r'].shift(-1)
y1 = y1.apply(lambda x:1 if x>0.0000 else 0)
label_display['y'] = y1
label_display['c1'] = c1
display(label_display.head(7))

```

###### Exploring influence of feature on outcome target


```python
def plot_histogram_dv(x,y):
    plt.figure(figsize=(15,10))
    plt.hist(list(x[y==0]), alpha=0.5, label='Bear')
    plt.hist(list(x[y==1]), alpha=0.5, label='Bull')
    plt.title("Histogram of '{var_name}' by Forecast Target".format(var_name=x.name))
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.legend(loc='upper right')
    plt.show()
```


```python
plot_histogram_dv(data['macdh'], y1)
plot_histogram_dv(data['cci'], y1)
plot_histogram_dv(data['adx'], y1)
plot_histogram_dv(data['kdjk'], y1)
```


![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_25_0.png)



![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_25_1.png)



![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_25_2.png)



![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_25_3.png)


## Feature Engineering

###### Normalizing and Standardizing distributions
Different techniques to represent a price movement can be used to select the one with best results


```python
data.plot(x=data.index, y=['close_20_sma','adx', 'cci'], figsize=(15, 10))

```




    <matplotlib.axes._subplots.AxesSubplot at 0x1a17408850>




![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_28_1.png)


#### As shown above, different indicators have different metrics, so we need to normalize in various ways and search for the best results 

###### First let's explore the behavior of each target label


```python
#Labeling the different window frames
##Signaling the difference between a feature datapoint and the previous/next one
       
def labelwf(dataframe, wf):
    for i in wf:
        swf = str(i)
        dataframe['label' + swf] = \
        (dataframe['close'] - dataframe['close'].shift(i))/dataframe['close'].shift(i)
        dataframe['label' + swf] = dataframe['label' + swf].apply(lambda x:1 if x>0.0 else 0)
    return dataframe
    
#Negative for looking future datapoints
#Positive for looking backwards
window_frames = [-1, -2, -15, 1, 2, 15]
labeled_data = labelwf(data.copy(), window_frames)
index = list(range(len(data)))
index = index[-250:-15]
label1 = labeled_data['label-1'].values
label1 = label1[-250:-15]
label15 = labeled_data['label-15'].values
label15 = label15[-250:-15]
c1 = copy['close_1_r'].apply(lambda x:0 if x>0.000 else 1)
c15 = copy['close_15_r'].apply(lambda x:0 if x>0.000 else 1)
y_5 = copy['close_5_r'].apply(lambda x:0 if x>0.000 else 1)
y_10 = copy['close_10_r'].apply(lambda x:0 if x>0.000 else 1)
y_30 = copy['close_30_r'].applu(lambda x:0 if x>0.000 else 1)
index = list(range(len(c1)))
index = index[-250:-15]

fig, ax = plt.subplots(figsize=(15, 8), sharey=True)
ax.plot(index, c1[-250:-15], label='1d forward', color='r')
ax.scatter(index, c15[-250:-15], label='15d forward', color='g')
ax.legend()


labeled_data['index'] = list(range(len(data)))
data.plot(y='close', figsize=(15, 8))
for r in labeled_data.iterrows():
    if r[1]['label1'] == 1:
        plt.axvline(x=r[1]['index'], linewidth=0.3, alpha=0.3, color='g')
    else:
        plt.axvline(x=r[1]['index'], linewidth=0.3, alpha=0.3, color='r')
    
plt.show()

```


![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_31_0.png)



![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_31_1.png)


###### Percentage change of each indicator : (xn - xn-1)/xn-1 where n = [n, n+y, n+2y] and y = Time Frame Window selected


```python
#Normalizing the features datapoints 
#Accordingly to its window frame

#Each datapoint to the change percentage of timeframe
def percent_change(dataframe, wf):
    new = pd.DataFrame()
    swf = str(wf)
    for feature in dataframe:
        if 'label' in str(dataframe[feature].name):
            pass
        elif 'change_' in str(dataframe[feature].name):
            pass
        else:
            dataframe['change_' + str(dataframe[feature].name)] = \
            (dataframe[feature] - dataframe[feature].shift(wf))/dataframe[feature].shift(wf)
            new['change_' + str(dataframe[feature].name)] = \
            (dataframe[feature] - dataframe[feature].shift(wf))/dataframe[feature].shift(wf)
    return dataframe, new

raw_data = data.copy()
data, percent_change_data = percent_change(data, 1)
data = data.drop('change_pdm', 1)
data = data.drop('change_um', 1)
data = data.drop('change_dm', 1)
percent_change_data = percent_change_data.drop('change_pdm', 1)
percent_change_data = percent_change_data.drop('change_um', 1)
percent_change_data = percent_change_data.drop('change_dm', 1)
percent_change_data = percent_change_data.replace([np.inf, -np.inf], np.nan)
percent_change_data = percent_change_data.fillna(method='bfill')
data = data.replace([np.inf, -np.inf], np.nan)
data = data.fillna(method='bfill')
data.plot(x=data.index, y='change_close_20_sma', figsize=(15,10))
data.plot(x=data.index, y=['change_kdjk','change_adx', 'change_close_20_sma'], figsize=(15,10))
                          
display(data.tail())
display(percent_change_data.tail())
plot_histogram_dv(data['change_macdh'], y1)
plot_histogram_dv(data['change_macdh'], c15)
```


<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>close_20_sma</th>
      <th>close_20_mstd</th>
      <th>boll</th>
      <th>boll_ub</th>
      <th>boll_lb</th>
      <th>close_-1_s</th>
      <th>...</th>
      <th>change_mdi_14</th>
      <th>change_mdi</th>
      <th>change_dx_14</th>
      <th>change_dx</th>
      <th>change_dx_6_ema</th>
      <th>change_adx</th>
      <th>change_adx_6_ema</th>
      <th>change_adxr</th>
      <th>change_trix</th>
      <th>change_trix_9_sma</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2018-01-01</th>
      <td>3.3075</td>
      <td>3.3117</td>
      <td>3.3075</td>
      <td>3.3076</td>
      <td>3.296855</td>
      <td>0.029485</td>
      <td>3.296855</td>
      <td>3.355825</td>
      <td>3.237885</td>
      <td>3.3111</td>
      <td>...</td>
      <td>-0.073114</td>
      <td>-0.073114</td>
      <td>-6.225712e-16</td>
      <td>-6.225712e-16</td>
      <td>0.047143</td>
      <td>0.047143</td>
      <td>-0.009660</td>
      <td>-0.009660</td>
      <td>-0.034542</td>
      <td>0.016791</td>
    </tr>
    <tr>
      <th>2018-01-02</th>
      <td>3.3108</td>
      <td>3.3127</td>
      <td>3.2585</td>
      <td>3.3110</td>
      <td>3.300275</td>
      <td>0.026696</td>
      <td>3.300275</td>
      <td>3.353666</td>
      <td>3.246884</td>
      <td>3.3076</td>
      <td>...</td>
      <td>0.695512</td>
      <td>0.695512</td>
      <td>1.310292e+00</td>
      <td>1.310292e+00</td>
      <td>0.448662</td>
      <td>0.448662</td>
      <td>0.118096</td>
      <td>0.118096</td>
      <td>-0.044511</td>
      <td>0.007815</td>
    </tr>
    <tr>
      <th>2018-01-03</th>
      <td>3.2574</td>
      <td>3.2638</td>
      <td>3.2410</td>
      <td>3.2578</td>
      <td>3.301150</td>
      <td>0.024849</td>
      <td>3.301150</td>
      <td>3.350849</td>
      <td>3.251451</td>
      <td>3.3110</td>
      <td>...</td>
      <td>-0.015868</td>
      <td>-0.015868</td>
      <td>1.234280e-01</td>
      <td>1.234280e-01</td>
      <td>0.283790</td>
      <td>0.283790</td>
      <td>0.177938</td>
      <td>0.177938</td>
      <td>-0.126147</td>
      <td>-0.007375</td>
    </tr>
    <tr>
      <th>2018-01-04</th>
      <td>3.2356</td>
      <td>3.2410</td>
      <td>3.2214</td>
      <td>3.2355</td>
      <td>3.301210</td>
      <td>0.024680</td>
      <td>3.301210</td>
      <td>3.350571</td>
      <td>3.251849</td>
      <td>3.2578</td>
      <td>...</td>
      <td>0.066333</td>
      <td>0.066333</td>
      <td>1.039332e-01</td>
      <td>1.039332e-01</td>
      <td>0.204003</td>
      <td>0.204003</td>
      <td>0.188197</td>
      <td>0.188197</td>
      <td>-0.228872</td>
      <td>-0.030493</td>
    </tr>
    <tr>
      <th>2018-01-05</th>
      <td>3.2328</td>
      <td>3.2479</td>
      <td>3.2256</td>
      <td>3.2331</td>
      <td>3.298505</td>
      <td>0.028901</td>
      <td>3.298505</td>
      <td>3.356306</td>
      <td>3.240704</td>
      <td>3.2355</td>
      <td>...</td>
      <td>-0.105324</td>
      <td>-0.105324</td>
      <td>-1.462284e-01</td>
      <td>-1.462284e-01</td>
      <td>0.061550</td>
      <td>0.061550</td>
      <td>0.137684</td>
      <td>0.137684</td>
      <td>-0.352545</td>
      <td>-0.063682</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 129 columns</p>
</div>



<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>change_open</th>
      <th>change_high</th>
      <th>change_low</th>
      <th>change_close</th>
      <th>change_close_20_sma</th>
      <th>change_close_20_mstd</th>
      <th>change_boll</th>
      <th>change_boll_ub</th>
      <th>change_boll_lb</th>
      <th>change_close_-1_s</th>
      <th>...</th>
      <th>change_mdi_14</th>
      <th>change_mdi</th>
      <th>change_dx_14</th>
      <th>change_dx</th>
      <th>change_dx_6_ema</th>
      <th>change_adx</th>
      <th>change_adx_6_ema</th>
      <th>change_adxr</th>
      <th>change_trix</th>
      <th>change_trix_9_sma</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2018-01-01</th>
      <td>-0.001057</td>
      <td>-0.000151</td>
      <td>0.007770</td>
      <td>-0.001057</td>
      <td>0.000762</td>
      <td>-0.037582</td>
      <td>0.000762</td>
      <td>0.000062</td>
      <td>0.001489</td>
      <td>-0.000664</td>
      <td>...</td>
      <td>-0.073114</td>
      <td>-0.073114</td>
      <td>-6.225712e-16</td>
      <td>-6.225712e-16</td>
      <td>0.047143</td>
      <td>0.047143</td>
      <td>-0.009660</td>
      <td>-0.009660</td>
      <td>-0.034542</td>
      <td>0.016791</td>
    </tr>
    <tr>
      <th>2018-01-02</th>
      <td>0.000998</td>
      <td>0.000302</td>
      <td>-0.014815</td>
      <td>0.001028</td>
      <td>0.001037</td>
      <td>-0.094602</td>
      <td>0.001037</td>
      <td>-0.000643</td>
      <td>0.002779</td>
      <td>-0.001057</td>
      <td>...</td>
      <td>0.695512</td>
      <td>0.695512</td>
      <td>1.310292e+00</td>
      <td>1.310292e+00</td>
      <td>0.448662</td>
      <td>0.448662</td>
      <td>0.118096</td>
      <td>0.118096</td>
      <td>-0.044511</td>
      <td>0.007815</td>
    </tr>
    <tr>
      <th>2018-01-03</th>
      <td>-0.016129</td>
      <td>-0.014761</td>
      <td>-0.005371</td>
      <td>-0.016068</td>
      <td>0.000265</td>
      <td>-0.069161</td>
      <td>0.000265</td>
      <td>-0.000840</td>
      <td>0.001407</td>
      <td>0.001028</td>
      <td>...</td>
      <td>-0.015868</td>
      <td>-0.015868</td>
      <td>1.234280e-01</td>
      <td>1.234280e-01</td>
      <td>0.283790</td>
      <td>0.283790</td>
      <td>0.177938</td>
      <td>0.177938</td>
      <td>-0.126147</td>
      <td>-0.007375</td>
    </tr>
    <tr>
      <th>2018-01-04</th>
      <td>-0.006692</td>
      <td>-0.006986</td>
      <td>-0.006048</td>
      <td>-0.006845</td>
      <td>0.000018</td>
      <td>-0.006802</td>
      <td>0.000018</td>
      <td>-0.000083</td>
      <td>0.000122</td>
      <td>-0.016068</td>
      <td>...</td>
      <td>0.066333</td>
      <td>0.066333</td>
      <td>1.039332e-01</td>
      <td>1.039332e-01</td>
      <td>0.204003</td>
      <td>0.204003</td>
      <td>0.188197</td>
      <td>0.188197</td>
      <td>-0.228872</td>
      <td>-0.030493</td>
    </tr>
    <tr>
      <th>2018-01-05</th>
      <td>-0.000865</td>
      <td>0.002129</td>
      <td>0.001304</td>
      <td>-0.000742</td>
      <td>-0.000819</td>
      <td>0.170995</td>
      <td>-0.000819</td>
      <td>0.001712</td>
      <td>-0.003427</td>
      <td>-0.006845</td>
      <td>...</td>
      <td>-0.105324</td>
      <td>-0.105324</td>
      <td>-1.462284e-01</td>
      <td>-1.462284e-01</td>
      <td>0.061550</td>
      <td>0.061550</td>
      <td>0.137684</td>
      <td>0.137684</td>
      <td>-0.352545</td>
      <td>-0.063682</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 63 columns</p>
</div>



![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_33_2.png)



![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_33_3.png)



![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_33_4.png)


#### We see in the above picture that even with the percent change ratio we cant diferentiate on how much that change was significant by some orders of magnitude

###### Standardized change range : ((xn - xn-1)/xn-1) / (xMax - xMin)


```python
#How abnormal was the change compared to the feature range
def normalized_range(dataframe, wf):
    swf = str(wf)
    new = pd.DataFrame()
    for feature in dataframe:
        if 'label' in str(dataframe[feature].name):
            pass
        elif 'change_' in str(dataframe[feature].name):
            pass
        elif 'rchange_' in str(dataframe[feature].name):
            pass
        else:
            try:
                range = dataframe['change_' + str(dataframe[feature].name)].max() - \
                                              dataframe['change_' + str(dataframe[feature].name)].min()
                dataframe['rchange_' + str(dataframe[feature].name)] = \
                                              dataframe['change_' + str(dataframe[feature].name)] / range
                new['rchange_' + str(dataframe[feature].name)] = \
                                              dataframe['change_' + str(dataframe[feature].name)] / range
            except:
                pass
    return dataframe, new
                                              

change_data = data.copy()
data, normalized_range_data = normalized_range(data, 1)
data.plot(x=data.index, y=['rchange_close_20_sma','rchange_adx', 'rchange_close'], figsize=(15,10))
data = data.replace([np.inf, -np.inf], np.nan)
data = data.fillna(method='bfill')
normalized_range_data = normalized_range_data.replace([np.inf, -np.inf], np.nan)
normalized_range_data = normalized_range_data.fillna(method='bfill')


display(data.tail())
display(normalized_range_data.tail())
plot_histogram_dv(normalized_range_data['rchange_rsi_6'], y1)    
plot_histogram_dv(normalized_range_data['rchange_rsi_6'], c15) 
```


<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>close_20_sma</th>
      <th>close_20_mstd</th>
      <th>boll</th>
      <th>boll_ub</th>
      <th>boll_lb</th>
      <th>close_-1_s</th>
      <th>...</th>
      <th>rchange_mdi_14</th>
      <th>rchange_mdi</th>
      <th>rchange_dx_14</th>
      <th>rchange_dx</th>
      <th>rchange_dx_6_ema</th>
      <th>rchange_adx</th>
      <th>rchange_adx_6_ema</th>
      <th>rchange_adxr</th>
      <th>rchange_trix</th>
      <th>rchange_trix_9_sma</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2018-01-01</th>
      <td>3.3075</td>
      <td>3.3117</td>
      <td>3.3075</td>
      <td>3.3076</td>
      <td>3.296855</td>
      <td>0.029485</td>
      <td>3.296855</td>
      <td>3.355825</td>
      <td>3.237885</td>
      <td>3.3111</td>
      <td>...</td>
      <td>-0.010609</td>
      <td>-0.010609</td>
      <td>-2.072037e-19</td>
      <td>-2.072037e-19</td>
      <td>0.012496</td>
      <td>0.012496</td>
      <td>-0.015652</td>
      <td>-0.015652</td>
      <td>-0.000204</td>
      <td>0.000091</td>
    </tr>
    <tr>
      <th>2018-01-02</th>
      <td>3.3108</td>
      <td>3.3127</td>
      <td>3.2585</td>
      <td>3.3110</td>
      <td>3.300275</td>
      <td>0.026696</td>
      <td>3.300275</td>
      <td>3.353666</td>
      <td>3.246884</td>
      <td>3.3076</td>
      <td>...</td>
      <td>0.100917</td>
      <td>0.100917</td>
      <td>4.360903e-04</td>
      <td>4.360903e-04</td>
      <td>0.118926</td>
      <td>0.118926</td>
      <td>0.191346</td>
      <td>0.191346</td>
      <td>-0.000263</td>
      <td>0.000042</td>
    </tr>
    <tr>
      <th>2018-01-03</th>
      <td>3.2574</td>
      <td>3.2638</td>
      <td>3.2410</td>
      <td>3.2578</td>
      <td>3.301150</td>
      <td>0.024849</td>
      <td>3.301150</td>
      <td>3.350849</td>
      <td>3.251451</td>
      <td>3.3110</td>
      <td>...</td>
      <td>-0.002302</td>
      <td>-0.002302</td>
      <td>4.107921e-05</td>
      <td>4.107921e-05</td>
      <td>0.075224</td>
      <td>0.075224</td>
      <td>0.288305</td>
      <td>0.288305</td>
      <td>-0.000745</td>
      <td>-0.000040</td>
    </tr>
    <tr>
      <th>2018-01-04</th>
      <td>3.2356</td>
      <td>3.2410</td>
      <td>3.2214</td>
      <td>3.2355</td>
      <td>3.301210</td>
      <td>0.024680</td>
      <td>3.301210</td>
      <td>3.350571</td>
      <td>3.251849</td>
      <td>3.2578</td>
      <td>...</td>
      <td>0.009625</td>
      <td>0.009625</td>
      <td>3.459096e-05</td>
      <td>3.459096e-05</td>
      <td>0.054075</td>
      <td>0.054075</td>
      <td>0.304928</td>
      <td>0.304928</td>
      <td>-0.001352</td>
      <td>-0.000165</td>
    </tr>
    <tr>
      <th>2018-01-05</th>
      <td>3.2328</td>
      <td>3.2479</td>
      <td>3.2256</td>
      <td>3.2331</td>
      <td>3.298505</td>
      <td>0.028901</td>
      <td>3.298505</td>
      <td>3.356306</td>
      <td>3.240704</td>
      <td>3.2355</td>
      <td>...</td>
      <td>-0.015282</td>
      <td>-0.015282</td>
      <td>-4.866762e-05</td>
      <td>-4.866762e-05</td>
      <td>0.016315</td>
      <td>0.016315</td>
      <td>0.223084</td>
      <td>0.223084</td>
      <td>-0.002083</td>
      <td>-0.000345</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 192 columns</p>
</div>



<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>rchange_open</th>
      <th>rchange_high</th>
      <th>rchange_low</th>
      <th>rchange_close</th>
      <th>rchange_close_20_sma</th>
      <th>rchange_close_20_mstd</th>
      <th>rchange_boll</th>
      <th>rchange_boll_ub</th>
      <th>rchange_boll_lb</th>
      <th>rchange_close_-1_s</th>
      <th>...</th>
      <th>rchange_mdi_14</th>
      <th>rchange_mdi</th>
      <th>rchange_dx_14</th>
      <th>rchange_dx</th>
      <th>rchange_dx_6_ema</th>
      <th>rchange_adx</th>
      <th>rchange_adx_6_ema</th>
      <th>rchange_adxr</th>
      <th>rchange_trix</th>
      <th>rchange_trix_9_sma</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2018-01-01</th>
      <td>-0.006705</td>
      <td>-0.000915</td>
      <td>0.065792</td>
      <td>-0.007716</td>
      <td>0.055369</td>
      <td>-0.022755</td>
      <td>0.055369</td>
      <td>0.001321</td>
      <td>0.041792</td>
      <td>-0.004847</td>
      <td>...</td>
      <td>-0.010609</td>
      <td>-0.010609</td>
      <td>-2.072037e-19</td>
      <td>-2.072037e-19</td>
      <td>0.012496</td>
      <td>0.012496</td>
      <td>-0.015652</td>
      <td>-0.015652</td>
      <td>-0.000204</td>
      <td>0.000091</td>
    </tr>
    <tr>
      <th>2018-01-02</th>
      <td>0.006329</td>
      <td>0.001830</td>
      <td>-0.125450</td>
      <td>0.007503</td>
      <td>0.075386</td>
      <td>-0.057278</td>
      <td>0.075386</td>
      <td>-0.013763</td>
      <td>0.078024</td>
      <td>-0.007716</td>
      <td>...</td>
      <td>0.100917</td>
      <td>0.100917</td>
      <td>4.360903e-04</td>
      <td>4.360903e-04</td>
      <td>0.118926</td>
      <td>0.118926</td>
      <td>0.191346</td>
      <td>0.191346</td>
      <td>-0.000263</td>
      <td>0.000042</td>
    </tr>
    <tr>
      <th>2018-01-03</th>
      <td>-0.102309</td>
      <td>-0.089450</td>
      <td>-0.045477</td>
      <td>-0.117284</td>
      <td>0.019267</td>
      <td>-0.041874</td>
      <td>0.019267</td>
      <td>-0.017975</td>
      <td>0.039494</td>
      <td>0.007503</td>
      <td>...</td>
      <td>-0.002302</td>
      <td>-0.002302</td>
      <td>4.107921e-05</td>
      <td>4.107921e-05</td>
      <td>0.075224</td>
      <td>0.075224</td>
      <td>0.288305</td>
      <td>0.288305</td>
      <td>-0.000745</td>
      <td>-0.000040</td>
    </tr>
    <tr>
      <th>2018-01-04</th>
      <td>-0.042451</td>
      <td>-0.042332</td>
      <td>-0.051209</td>
      <td>-0.049965</td>
      <td>0.001321</td>
      <td>-0.004119</td>
      <td>0.001321</td>
      <td>-0.001775</td>
      <td>0.003437</td>
      <td>-0.117284</td>
      <td>...</td>
      <td>0.009625</td>
      <td>0.009625</td>
      <td>3.459096e-05</td>
      <td>3.459096e-05</td>
      <td>0.054075</td>
      <td>0.054075</td>
      <td>0.304928</td>
      <td>0.304928</td>
      <td>-0.001352</td>
      <td>-0.000165</td>
    </tr>
    <tr>
      <th>2018-01-05</th>
      <td>-0.005489</td>
      <td>0.012901</td>
      <td>0.011040</td>
      <td>-0.005414</td>
      <td>-0.059547</td>
      <td>0.103531</td>
      <td>-0.059547</td>
      <td>0.036623</td>
      <td>-0.096222</td>
      <td>-0.049965</td>
      <td>...</td>
      <td>-0.015282</td>
      <td>-0.015282</td>
      <td>-4.866762e-05</td>
      <td>-4.866762e-05</td>
      <td>0.016315</td>
      <td>0.016315</td>
      <td>0.223084</td>
      <td>0.223084</td>
      <td>-0.002083</td>
      <td>-0.000345</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 63 columns</p>
</div>



![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_36_2.png)



![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_36_3.png)



![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_36_4.png)


#### As we can see, the datapoints are now expressing in a much more intuiteve manner their movements with a same axis of change

###### Normalized change rate : ( ( (xn - xn-1)/xn-1 ) - (Σxi / n) ) / ( √( (Σxi - (Σxi / n)ˆ2 ) / n ) ) = (Change - Mean) / Standard Deviation


```python
#How abnormal was this change percentage ratio in comparison to the others
def normalized_change(dataframe, wf):
    swf = str(wf)
    new = pd.DataFrame()
    for feature in dataframe:
        if 'label' in str(dataframe[feature].name):
            pass
        elif 'change_' in str(dataframe[feature].name):
            pass
        elif 'rchange_' in str(dataframe[feature].name):
            pass
        elif 'nchange_' in str(dataframe[feature].name):
            pass
        else:
            try:
                std = dataframe['change_' + str(dataframe[feature].name)].std()
                mean = dataframe['change_' + str(dataframe[feature].name)].mean()
                dataframe['nchange_' + str(dataframe[feature].name)] = \
                (dataframe['change_' + str(dataframe[feature].name)] - mean)/std
                new['nchange_' + str(dataframe[feature].name)] = \
                (dataframe['change_' + str(dataframe[feature].name)] - mean)/std
            except:
                pass
            
    return dataframe, new

rchange_data = data.copy()
data, normalized_change_data = normalized_change(data, 1)
data = data.replace([np.inf, -np.inf], np.nan)
data = data.fillna(method='bfill')
normalized_change_data = normalized_change_data.replace([np.inf, -np.inf], np.nan)
normalized_change_data = normalized_change_data.fillna(method='bfill')
data.plot(x=data.index, y=['nchange_close_20_sma','nchange_adx', 'nchange_close'], figsize=(15, 10))
                          
display(data.tail())
display(normalized_change_data.tail())

plot_histogram_dv(normalized_change_data['nchange_rsi_6'], y1)    
plot_histogram_dv(normalized_change_data['nchange_rsi_6'], c15)    

```


<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>close_20_sma</th>
      <th>close_20_mstd</th>
      <th>boll</th>
      <th>boll_ub</th>
      <th>boll_lb</th>
      <th>close_-1_s</th>
      <th>...</th>
      <th>nchange_mdi_14</th>
      <th>nchange_mdi</th>
      <th>nchange_dx_14</th>
      <th>nchange_dx</th>
      <th>nchange_dx_6_ema</th>
      <th>nchange_adx</th>
      <th>nchange_adx_6_ema</th>
      <th>nchange_adxr</th>
      <th>nchange_trix</th>
      <th>nchange_trix_9_sma</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2018-01-01</th>
      <td>3.3075</td>
      <td>3.3117</td>
      <td>3.3075</td>
      <td>3.3076</td>
      <td>3.296855</td>
      <td>0.029485</td>
      <td>3.296855</td>
      <td>3.355825</td>
      <td>3.237885</td>
      <td>3.3111</td>
      <td>...</td>
      <td>-0.277020</td>
      <td>-0.277020</td>
      <td>-0.045644</td>
      <td>-0.045644</td>
      <td>0.134691</td>
      <td>0.134691</td>
      <td>-0.148862</td>
      <td>-0.148862</td>
      <td>0.007774</td>
      <td>0.020925</td>
    </tr>
    <tr>
      <th>2018-01-02</th>
      <td>3.3108</td>
      <td>3.3127</td>
      <td>3.2585</td>
      <td>3.3110</td>
      <td>3.300275</td>
      <td>0.026696</td>
      <td>3.300275</td>
      <td>3.353666</td>
      <td>3.246884</td>
      <td>3.3076</td>
      <td>...</td>
      <td>1.612389</td>
      <td>1.612389</td>
      <td>-0.026412</td>
      <td>-0.026412</td>
      <td>2.033934</td>
      <td>2.033934</td>
      <td>1.249729</td>
      <td>1.249729</td>
      <td>0.004729</td>
      <td>0.018454</td>
    </tr>
    <tr>
      <th>2018-01-03</th>
      <td>3.2574</td>
      <td>3.2638</td>
      <td>3.2410</td>
      <td>3.2578</td>
      <td>3.301150</td>
      <td>0.024849</td>
      <td>3.301150</td>
      <td>3.350849</td>
      <td>3.251451</td>
      <td>3.3110</td>
      <td>...</td>
      <td>-0.136300</td>
      <td>-0.136300</td>
      <td>-0.043832</td>
      <td>-0.043832</td>
      <td>1.254066</td>
      <td>1.254066</td>
      <td>1.904840</td>
      <td>1.904840</td>
      <td>-0.020209</td>
      <td>0.014271</td>
    </tr>
    <tr>
      <th>2018-01-04</th>
      <td>3.2356</td>
      <td>3.2410</td>
      <td>3.2214</td>
      <td>3.2355</td>
      <td>3.301210</td>
      <td>0.024680</td>
      <td>3.301210</td>
      <td>3.350571</td>
      <td>3.251849</td>
      <td>3.2578</td>
      <td>...</td>
      <td>0.065763</td>
      <td>0.065763</td>
      <td>-0.044118</td>
      <td>-0.044118</td>
      <td>0.876665</td>
      <td>0.876665</td>
      <td>2.017157</td>
      <td>2.017157</td>
      <td>-0.051589</td>
      <td>0.007907</td>
    </tr>
    <tr>
      <th>2018-01-05</th>
      <td>3.2328</td>
      <td>3.2479</td>
      <td>3.2256</td>
      <td>3.2331</td>
      <td>3.298505</td>
      <td>0.028901</td>
      <td>3.298505</td>
      <td>3.356306</td>
      <td>3.240704</td>
      <td>3.2355</td>
      <td>...</td>
      <td>-0.356199</td>
      <td>-0.356199</td>
      <td>-0.047790</td>
      <td>-0.047790</td>
      <td>0.202839</td>
      <td>0.202839</td>
      <td>1.464168</td>
      <td>1.464168</td>
      <td>-0.089369</td>
      <td>-0.001231</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 255 columns</p>
</div>



<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>nchange_open</th>
      <th>nchange_high</th>
      <th>nchange_low</th>
      <th>nchange_close</th>
      <th>nchange_close_20_sma</th>
      <th>nchange_close_20_mstd</th>
      <th>nchange_boll</th>
      <th>nchange_boll_ub</th>
      <th>nchange_boll_lb</th>
      <th>nchange_close_-1_s</th>
      <th>...</th>
      <th>nchange_mdi_14</th>
      <th>nchange_mdi</th>
      <th>nchange_dx_14</th>
      <th>nchange_dx</th>
      <th>nchange_dx_6_ema</th>
      <th>nchange_adx</th>
      <th>nchange_adx_6_ema</th>
      <th>nchange_adxr</th>
      <th>nchange_trix</th>
      <th>nchange_trix_9_sma</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2018-01-01</th>
      <td>-0.128347</td>
      <td>-0.050057</td>
      <td>0.821339</td>
      <td>-0.127259</td>
      <td>0.229905</td>
      <td>-0.441805</td>
      <td>0.229905</td>
      <td>-0.071889</td>
      <td>0.362274</td>
      <td>-0.089153</td>
      <td>...</td>
      <td>-0.277020</td>
      <td>-0.277020</td>
      <td>-0.045644</td>
      <td>-0.045644</td>
      <td>0.134691</td>
      <td>0.134691</td>
      <td>-0.148862</td>
      <td>-0.148862</td>
      <td>0.007774</td>
      <td>0.020925</td>
    </tr>
    <tr>
      <th>2018-01-02</th>
      <td>0.061175</td>
      <td>-0.003072</td>
      <td>-1.676715</td>
      <td>0.059701</td>
      <td>0.368936</td>
      <td>-1.041422</td>
      <td>0.368936</td>
      <td>-0.279976</td>
      <td>0.760588</td>
      <td>-0.124398</td>
      <td>...</td>
      <td>1.612389</td>
      <td>1.612389</td>
      <td>-0.026412</td>
      <td>-0.026412</td>
      <td>2.033934</td>
      <td>2.033934</td>
      <td>1.249729</td>
      <td>1.249729</td>
      <td>0.004729</td>
      <td>0.018454</td>
    </tr>
    <tr>
      <th>2018-01-03</th>
      <td>-1.518482</td>
      <td>-1.565728</td>
      <td>-0.632093</td>
      <td>-1.473256</td>
      <td>-0.020851</td>
      <td>-0.773884</td>
      <td>-0.020851</td>
      <td>-0.338086</td>
      <td>0.337015</td>
      <td>0.062559</td>
      <td>...</td>
      <td>-0.136300</td>
      <td>-0.136300</td>
      <td>-0.043832</td>
      <td>-0.043832</td>
      <td>1.254066</td>
      <td>1.254066</td>
      <td>1.904840</td>
      <td>1.904840</td>
      <td>-0.020209</td>
      <td>0.014271</td>
    </tr>
    <tr>
      <th>2018-01-04</th>
      <td>-0.648116</td>
      <td>-0.759089</td>
      <td>-0.706970</td>
      <td>-0.646273</td>
      <td>-0.145504</td>
      <td>-0.118126</td>
      <td>-0.145504</td>
      <td>-0.114609</td>
      <td>-0.059371</td>
      <td>-1.470369</td>
      <td>...</td>
      <td>0.065763</td>
      <td>0.065763</td>
      <td>-0.044118</td>
      <td>-0.044118</td>
      <td>0.876665</td>
      <td>0.876665</td>
      <td>2.017157</td>
      <td>2.017157</td>
      <td>-0.051589</td>
      <td>0.007907</td>
    </tr>
    <tr>
      <th>2018-01-05</th>
      <td>-0.110665</td>
      <td>0.186461</td>
      <td>0.106153</td>
      <td>-0.098988</td>
      <td>-0.568277</td>
      <td>1.751577</td>
      <td>-0.568277</td>
      <td>0.415113</td>
      <td>-1.154962</td>
      <td>-0.643402</td>
      <td>...</td>
      <td>-0.356199</td>
      <td>-0.356199</td>
      <td>-0.047790</td>
      <td>-0.047790</td>
      <td>0.202839</td>
      <td>0.202839</td>
      <td>1.464168</td>
      <td>1.464168</td>
      <td>-0.089369</td>
      <td>-0.001231</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 63 columns</p>
</div>



![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_39_2.png)



![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_39_3.png)



![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_39_4.png)


###### And now, we can evaluate the order of the anomaly of a certain datapoint without losing information on the feature

###### Normalizing the raw features instead of the change rate


```python
#How abnormal is the position that the datapoint is located at
#We substitute the original feature value for this one
def distance(dataframe):
    new = pd.DataFrame()
    for feature in dataframe:
        if 'label' in str(dataframe[feature].name):
            pass
        elif 'change_' in str(dataframe[feature].name):
            pass
        elif 'nchange_' in str(dataframe[feature].name):
            pass
        elif 'rchange_' in str(dataframe[feature].name):
            pass
        elif 'distance_' in str(dataframe[feature].name):
            pass
        else:
            std = dataframe[feature].std()
            mean = dataframe[feature].mean()
            dataframe['distance_' + str(dataframe[feature].name)] = (dataframe[feature] - mean)/std 
            new['distance_' + str(dataframe[feature].name)] = (dataframe[feature] - mean)/std 
    return dataframe, new

nchange = data.copy()
data, distance_data = distance(data)
data = data.replace([np.inf, -np.inf], np.nan)
data = data.fillna(method='bfill')
distance_data = distance_data.replace([np.inf, -np.inf], np.nan)
distance_data = distance_data.fillna(method='bfill')
data.plot(x=data.index, y=['distance_close_20_sma','distance_adx', 'close_20_sma'], figsize=(15,10))


display(data.tail())
display(distance_data.tail())

plot_histogram_dv(distance_data['distance_macdh'], y1)
plot_histogram_dv(data['macdh'], y1)    
plot_histogram_dv(distance_data['distance_macdh'], c15)
plot_histogram_dv(data['macdh'], c15)
```


<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>close_20_sma</th>
      <th>close_20_mstd</th>
      <th>boll</th>
      <th>boll_ub</th>
      <th>boll_lb</th>
      <th>close_-1_s</th>
      <th>...</th>
      <th>distance_mdi_14</th>
      <th>distance_mdi</th>
      <th>distance_dx_14</th>
      <th>distance_dx</th>
      <th>distance_dx_6_ema</th>
      <th>distance_adx</th>
      <th>distance_adx_6_ema</th>
      <th>distance_adxr</th>
      <th>distance_trix</th>
      <th>distance_trix_9_sma</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2018-01-01</th>
      <td>3.3075</td>
      <td>3.3117</td>
      <td>3.3075</td>
      <td>3.3076</td>
      <td>3.296855</td>
      <td>0.029485</td>
      <td>3.296855</td>
      <td>3.355825</td>
      <td>3.237885</td>
      <td>3.3111</td>
      <td>...</td>
      <td>0.488966</td>
      <td>0.488966</td>
      <td>-0.348806</td>
      <td>-0.348806</td>
      <td>-0.616822</td>
      <td>-0.616822</td>
      <td>-0.665492</td>
      <td>-0.665492</td>
      <td>0.338169</td>
      <td>0.335080</td>
    </tr>
    <tr>
      <th>2018-01-02</th>
      <td>3.3108</td>
      <td>3.3127</td>
      <td>3.2585</td>
      <td>3.3110</td>
      <td>3.300275</td>
      <td>0.026696</td>
      <td>3.300275</td>
      <td>3.353666</td>
      <td>3.246884</td>
      <td>3.3076</td>
      <td>...</td>
      <td>2.302947</td>
      <td>2.302947</td>
      <td>1.064375</td>
      <td>1.064375</td>
      <td>-0.031028</td>
      <td>-0.031028</td>
      <td>-0.485673</td>
      <td>-0.485673</td>
      <td>0.314458</td>
      <td>0.339260</td>
    </tr>
    <tr>
      <th>2018-01-03</th>
      <td>3.2574</td>
      <td>3.2638</td>
      <td>3.2410</td>
      <td>3.2578</td>
      <td>3.301150</td>
      <td>0.024849</td>
      <td>3.301150</td>
      <td>3.350849</td>
      <td>3.251451</td>
      <td>3.3110</td>
      <td>...</td>
      <td>2.232778</td>
      <td>2.232778</td>
      <td>1.371921</td>
      <td>1.371921</td>
      <td>0.505743</td>
      <td>0.505743</td>
      <td>-0.182739</td>
      <td>-0.182739</td>
      <td>0.250250</td>
      <td>0.335284</td>
    </tr>
    <tr>
      <th>2018-01-04</th>
      <td>3.2356</td>
      <td>3.2410</td>
      <td>3.2214</td>
      <td>3.2355</td>
      <td>3.301210</td>
      <td>0.024680</td>
      <td>3.301210</td>
      <td>3.350571</td>
      <td>3.251849</td>
      <td>3.2578</td>
      <td>...</td>
      <td>2.521454</td>
      <td>2.521454</td>
      <td>1.662856</td>
      <td>1.662856</td>
      <td>1.001106</td>
      <td>1.001106</td>
      <td>0.194673</td>
      <td>0.194673</td>
      <td>0.148451</td>
      <td>0.318967</td>
    </tr>
    <tr>
      <th>2018-01-05</th>
      <td>3.2328</td>
      <td>3.2479</td>
      <td>3.2256</td>
      <td>3.2331</td>
      <td>3.298505</td>
      <td>0.028901</td>
      <td>3.298505</td>
      <td>3.356306</td>
      <td>3.240704</td>
      <td>3.2355</td>
      <td>...</td>
      <td>2.032685</td>
      <td>2.032685</td>
      <td>1.210983</td>
      <td>1.210983</td>
      <td>1.181051</td>
      <td>1.181051</td>
      <td>0.522749</td>
      <td>0.522749</td>
      <td>0.027533</td>
      <td>0.285929</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 321 columns</p>
</div>



<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>distance_open</th>
      <th>distance_high</th>
      <th>distance_low</th>
      <th>distance_close</th>
      <th>distance_close_20_sma</th>
      <th>distance_close_20_mstd</th>
      <th>distance_boll</th>
      <th>distance_boll_ub</th>
      <th>distance_boll_lb</th>
      <th>distance_close_-1_s</th>
      <th>...</th>
      <th>distance_mdi_14</th>
      <th>distance_mdi</th>
      <th>distance_dx_14</th>
      <th>distance_dx</th>
      <th>distance_dx_6_ema</th>
      <th>distance_adx</th>
      <th>distance_adx_6_ema</th>
      <th>distance_adxr</th>
      <th>distance_trix</th>
      <th>distance_trix_9_sma</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2018-01-01</th>
      <td>1.129346</td>
      <td>1.105120</td>
      <td>1.161948</td>
      <td>1.130977</td>
      <td>1.128932</td>
      <td>-0.326446</td>
      <td>1.128932</td>
      <td>1.056927</td>
      <td>1.203622</td>
      <td>1.136831</td>
      <td>...</td>
      <td>0.488966</td>
      <td>0.488966</td>
      <td>-0.348806</td>
      <td>-0.348806</td>
      <td>-0.616822</td>
      <td>-0.616822</td>
      <td>-0.665492</td>
      <td>-0.665492</td>
      <td>0.338169</td>
      <td>0.335080</td>
    </tr>
    <tr>
      <th>2018-01-02</th>
      <td>1.133888</td>
      <td>1.106495</td>
      <td>1.093890</td>
      <td>1.135696</td>
      <td>1.133691</td>
      <td>-0.433323</td>
      <td>1.133691</td>
      <td>1.054054</td>
      <td>1.216700</td>
      <td>1.131972</td>
      <td>...</td>
      <td>2.302947</td>
      <td>2.302947</td>
      <td>1.064375</td>
      <td>1.064375</td>
      <td>-0.031028</td>
      <td>-0.031028</td>
      <td>-0.485673</td>
      <td>-0.485673</td>
      <td>0.314458</td>
      <td>0.339260</td>
    </tr>
    <tr>
      <th>2018-01-03</th>
      <td>1.060385</td>
      <td>1.039224</td>
      <td>1.069584</td>
      <td>1.061854</td>
      <td>1.134909</td>
      <td>-0.504066</td>
      <td>1.134909</td>
      <td>1.050304</td>
      <td>1.223338</td>
      <td>1.136692</td>
      <td>...</td>
      <td>2.232778</td>
      <td>2.232778</td>
      <td>1.371921</td>
      <td>1.371921</td>
      <td>0.505743</td>
      <td>0.505743</td>
      <td>-0.182739</td>
      <td>-0.182739</td>
      <td>0.250250</td>
      <td>0.335284</td>
    </tr>
    <tr>
      <th>2018-01-04</th>
      <td>1.030377</td>
      <td>1.007858</td>
      <td>1.042361</td>
      <td>1.030902</td>
      <td>1.134993</td>
      <td>-0.510543</td>
      <td>1.134993</td>
      <td>1.049934</td>
      <td>1.223916</td>
      <td>1.062847</td>
      <td>...</td>
      <td>2.521454</td>
      <td>2.521454</td>
      <td>1.662856</td>
      <td>1.662856</td>
      <td>1.001106</td>
      <td>1.001106</td>
      <td>0.194673</td>
      <td>0.194673</td>
      <td>0.148451</td>
      <td>0.318967</td>
    </tr>
    <tr>
      <th>2018-01-05</th>
      <td>1.026523</td>
      <td>1.017350</td>
      <td>1.048194</td>
      <td>1.027570</td>
      <td>1.131228</td>
      <td>-0.348840</td>
      <td>1.131228</td>
      <td>1.057567</td>
      <td>1.207719</td>
      <td>1.031893</td>
      <td>...</td>
      <td>2.032685</td>
      <td>2.032685</td>
      <td>1.210983</td>
      <td>1.210983</td>
      <td>1.181051</td>
      <td>1.181051</td>
      <td>0.522749</td>
      <td>0.522749</td>
      <td>0.027533</td>
      <td>0.285929</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 66 columns</p>
</div>



![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_42_2.png)



![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_42_3.png)



![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_42_4.png)



![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_42_5.png)



![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_42_6.png)


#### And evaluate the distance of the datapoint address in comparison to the others of its kind

###### Creating new features via interactions between them


```python
from itertools import combinations
from sklearn.preprocessing import PolynomialFeatures

def add_interactions(df):
    # Get feature names
    combos = list(combinations(list(df.columns), 2))
    colnames = list(df.columns) + ['_'.join(x) for x in combos]
    
    # Find interactions
    poly = PolynomialFeatures(interaction_only=True, include_bias=False)
    df = poly.fit_transform(df)
    df = pd.DataFrame(df)
    df.columns = colnames
    
    # Remove interaction terms with all 0 values            
    noint_indicies = [i for i, x in enumerate(list((df == 0).all())) if x]
    df = df.drop(df.columns[noint_indicies], axis=1)
    
    return df
```


```python
teste = add_interactions(data.copy())
print (teste.head(5))
```

         open    high     low   close  close_20_sma  close_20_mstd      boll  \
    0  1.8189  1.8213  1.7655  1.7835      1.758200       0.028923  1.758200   
    1  1.8136  1.8460  1.8129  1.8336      1.762635       0.033447  1.762635   
    2  1.7860  1.8663  1.7860  1.8496      1.767467       0.038380  1.767467   
    3  1.8064  1.8712  1.8064  1.8680      1.772758       0.043854  1.772758   
    4  1.8200  1.8729  1.8200  1.8729      1.777765       0.048201  1.777765   
    
        boll_ub   boll_lb  close_-1_s                ...                  \
    0  1.816046  1.700354      1.8188                ...                   
    1  1.829528  1.695742      1.7835                ...                   
    2  1.844227  1.690707      1.8336                ...                   
    3  1.860465  1.685051      1.8496                ...                   
    4  1.874167  1.681363      1.8680                ...                   
    
       distance_adx_distance_adx_6_ema  distance_adx_distance_adxr  \
    0                         2.155962                    2.155962   
    1                         3.204561                    3.204561   
    2                         2.238586                    2.238586   
    3                         1.551822                    1.551822   
    4                         1.090493                    1.090493   
    
       distance_adx_distance_trix  distance_adx_distance_trix_9_sma  \
    0                    1.237139                          0.663483   
    1                    1.774381                          1.013457   
    2                    1.445436                          0.852129   
    3                    1.260181                          0.754362   
    4                    1.133128                          0.694455   
    
       distance_adx_6_ema_distance_adxr  distance_adx_6_ema_distance_trix  \
    0                          1.881588                          1.079697   
    1                          2.633112                          1.457967   
    2                          2.594067                          1.674967   
    3                          2.216411                          1.799871   
    4                          1.767651                          1.836761   
    
       distance_adx_6_ema_distance_trix_9_sma  distance_adxr_distance_trix  \
    0                                0.579046                     1.079697   
    1                                0.832734                     1.457967   
    2                                0.987445                     1.674967   
    3                                1.077429                     1.799871   
    4                                1.125687                     1.836761   
    
       distance_adxr_distance_trix_9_sma  distance_trix_distance_trix_9_sma  
    0                           0.579046                           0.332270  
    1                           0.832734                           0.461089  
    2                           0.987445                           0.637585  
    3                           1.077429                           0.874942  
    4                           1.125687                           1.169698  
    
    [5 rows x 51681 columns]


## Feature Selection

###### The methods based on F-test estimate the degree of linear dependency between two random variables. On the other hand, mutual information methods can capture any kind of statistical dependency, but being nonparametric, they require more samples for accurate estimation.


```python
import numpy as np
from sklearn.feature_selection import f_classif, mutual_info_classif

y_15 = c15[15:-15]
y_1 = c1[15:-15]
y_5 = y_5[15:-15]
y_30 = y_30[15:-15]
mi = mutual_info_regression(distance_data, y_15, discrete_features='auto')
#print test.columns
mi /= np.max(mi)
result = distance_data.columns[mi > 0.1]
miresult = result
mi = mi[mi > 0.1]
print len(result)
display(result)
mi_df = pd.DataFrame(index=result, columns=['value'])
mi_df['value'] = mi
mi_df.plot(figsize=(15,10))
display(mi_df.head())
print mi_df

print "\n"

ftest, _ = f_regression(distance_data, y_15)
ftest /= np.max(ftest)
_[np.isnan(_)] = 0.0
f = _[~np.isnan(_)]
result = distance_data.columns[f > 0.1]
f = f[f > 0.1]
#print f.max()
#print result.max()
print len(result)
print result

f_df = pd.DataFrame(index=result, columns=['value'])
f_df['value'] = f
f_df.plot(figsize=(15,10))
display(f_df.head())
print f_df

equal = []

for i in miresult.values:
    if i in result.values:
        equal.append(i)
    
print "\n"
display(equal)


```

    29



    Index([u'distance_open', u'distance_high', u'distance_low', u'distance_close',
           u'distance_close_20_sma', u'distance_close_20_mstd', u'distance_boll',
           u'distance_boll_ub', u'distance_boll_lb', u'distance_close_-1_s',
           u'distance_close_26_ema', u'distance_macd', u'distance_middle',
           u'distance_cr-ma1', u'distance_cr-ma3', u'distance_open_2_sma',
           u'distance_middle_14_sma', u'distance_middle_20_sma', u'distance_atr',
           u'distance_close_10_sma', u'distance_close_50_sma', u'distance_dma',
           u'distance_atr_14', u'distance_dx_14', u'distance_dx',
           u'distance_dx_6_ema', u'distance_adx', u'distance_trix',
           u'distance_trix_9_sma'],
          dtype='object')



<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>distance_open</th>
      <td>0.440642</td>
    </tr>
    <tr>
      <th>distance_high</th>
      <td>0.443556</td>
    </tr>
    <tr>
      <th>distance_low</th>
      <td>0.505598</td>
    </tr>
    <tr>
      <th>distance_close</th>
      <td>0.468534</td>
    </tr>
    <tr>
      <th>distance_close_20_sma</th>
      <td>0.491667</td>
    </tr>
  </tbody>
</table>
</div>


                               value
    distance_open           0.440642
    distance_high           0.443556
    distance_low            0.505598
    distance_close          0.468534
    distance_close_20_sma   0.491667
    distance_close_20_mstd  0.217032
    distance_boll           0.494343
    distance_boll_ub        0.829823
    distance_boll_lb        0.555011
    distance_close_-1_s     0.442161
    distance_close_26_ema   0.729244
    distance_macd           0.168234
    distance_middle         0.637619
    distance_cr-ma1         0.207764
    distance_cr-ma3         0.198476
    distance_open_2_sma     0.450697
    distance_middle_14_sma  0.642620
    distance_middle_20_sma  0.506292
    distance_atr            0.241409
    distance_close_10_sma   0.624836
    distance_close_50_sma   1.000000
    distance_dma            0.172680
    distance_atr_14         0.246042
    distance_dx_14          0.185833
    distance_dx             0.173521
    distance_dx_6_ema       0.113376
    distance_adx            0.113376
    distance_trix           0.319277
    distance_trix_9_sma     0.260197
    
    
    24
    Index([u'distance_open', u'distance_high', u'distance_low', u'distance_close',
           u'distance_boll_lb', u'distance_close_-1_s', u'distance_close_-1_d',
           u'distance_close_-1_r', u'distance_middle', u'distance_cr-ma3',
           u'distance_rsv_9', u'distance_kdjk_9', u'distance_kdjk',
           u'distance_kdjj_9', u'distance_kdjj', u'distance_open_2_sma',
           u'distance_wr_10', u'distance_middle_14_sma', u'distance_close_10_sma',
           u'distance_pdm_14_ema', u'distance_pdm_14', u'distance_adx_6_ema',
           u'distance_adxr', u'distance_trix_9_sma'],
          dtype='object')



<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>value</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>distance_open</th>
      <td>0.191533</td>
    </tr>
    <tr>
      <th>distance_high</th>
      <td>0.181462</td>
    </tr>
    <tr>
      <th>distance_low</th>
      <td>0.210108</td>
    </tr>
    <tr>
      <th>distance_close</th>
      <td>0.138125</td>
    </tr>
    <tr>
      <th>distance_boll_lb</th>
      <td>0.141074</td>
    </tr>
  </tbody>
</table>
</div>


                               value
    distance_open           0.191533
    distance_high           0.181462
    distance_low            0.210108
    distance_close          0.138125
    distance_boll_lb        0.141074
    distance_close_-1_s     0.141206
    distance_close_-1_d     0.740016
    distance_close_-1_r     0.530851
    distance_middle         0.174595
    distance_cr-ma3         0.211435
    distance_rsv_9          0.249812
    distance_kdjk_9         0.276445
    distance_kdjk           0.276445
    distance_kdjj_9         0.714550
    distance_kdjj           0.714550
    distance_open_2_sma     0.184072
    distance_wr_10          0.488122
    distance_middle_14_sma  0.110842
    distance_close_10_sma   0.116276
    distance_pdm_14_ema     0.299721
    distance_pdm_14         0.299721
    distance_adx_6_ema      0.506360
    distance_adxr           0.506360
    distance_trix_9_sma     0.250674
    
    



    ['distance_open',
     'distance_high',
     'distance_low',
     'distance_close',
     'distance_boll_lb',
     'distance_close_-1_s',
     'distance_middle',
     'distance_cr-ma3',
     'distance_open_2_sma',
     'distance_middle_14_sma',
     'distance_close_10_sma',
     'distance_trix_9_sma']



![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_49_7.png)



![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_49_8.png)



```python
from sklearn.decomposition import PCA



pca = PCA(n_components=2)
data_pca = pd.DataFrame(pca.fit_transform(distance_data))
#display(data_pca.head())
data_pca.plot(figsize=(15,10))

datatest = pca.fit_transform(distance_data)
plt.figure(num=None, figsize=(18, 11), dpi=80, facecolor='w', edgecolor='k')
plt.scatter(datatest[:, 0], datatest[:, 1])
plt.show()
```


![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_50_0.png)



![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_50_1.png)


###### T - Distributed Stochastic Neighboor Embedding
Transforming the data into a Similarity Matrix for comparing the similarity of a certain datapoint with the rest


```python
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score

# t-distributed Stochastic Neighbor Embedding (t-SNE) visualization
from sklearn.manifold import TSNE
tsne = TSNE(n_components=2, random_state=0)
x_test_2d = tsne.fit_transform(distance_data)
#y_test = y_15

y_tsne = []
for key, i in np.ndenumerate(y_15):
    if i == 0:
        if y_1[key[0]] == 0:
            y_tsne.append(0)
        elif y_1[key[0]] == 1:
            y_tsne.append(1)
    if i == 1:
        if y_1[key[0]] == 0:
            y_tsne.append(2)
        elif y_1[key[0]] == 1:
            y_tsne.append(3)

y_test = np.array(y_tsne)
            

markers=('s', 'd', 'o', '^', 'v')
color_map = {0:'red', 1:'blue', 2:'lightgreen', 3:'purple'}
plt.figure(figsize=(15,10))
for idx, cl in enumerate(np.unique(y_test)):
    plt.scatter(x=x_test_2d[y_test==cl,0], y=x_test_2d[y_test==cl,1], c=color_map[idx], marker=markers[idx], label=cl, alpha=0.5)
plt.xlabel('X in t-SNE')
plt.ylabel('Y in t-SNE')
plt.legend(loc='upper left')
plt.title('t-SNE visualization of test data')
plt.show()


```


![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_52_0.png)


# Facebook Time series forecasting

###### Prophet library


```python
from fbprophet import Prophet
import numpy as np

test = data.copy()
test['ds'] = data.index
test['y'] = np.log(data['close'])
display(test.tail())
m = Prophet()
m.fit(test)
future = m.make_future_dataframe(periods=365)
forecast = m.predict(future)
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
m.plot(forecast)
m.plot_components(forecast)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>adj close</th>
      <th>volume</th>
      <th>ds</th>
      <th>y</th>
    </tr>
    <tr>
      <th>Date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2018-02-05</th>
      <td>3.2169</td>
      <td>3.2455</td>
      <td>3.2138</td>
      <td>3.2154</td>
      <td>3.2154</td>
      <td>0.0</td>
      <td>2018-02-05</td>
      <td>1.167952</td>
    </tr>
    <tr>
      <th>2018-02-06</th>
      <td>3.2611</td>
      <td>3.2759</td>
      <td>3.2175</td>
      <td>3.2611</td>
      <td>3.2611</td>
      <td>0.0</td>
      <td>2018-02-06</td>
      <td>1.182065</td>
    </tr>
    <tr>
      <th>2018-02-07</th>
      <td>3.2333</td>
      <td>3.2630</td>
      <td>3.2314</td>
      <td>3.2334</td>
      <td>3.2334</td>
      <td>0.0</td>
      <td>2018-02-07</td>
      <td>1.173534</td>
    </tr>
    <tr>
      <th>2018-02-08</th>
      <td>3.2696</td>
      <td>3.2926</td>
      <td>3.2562</td>
      <td>3.2699</td>
      <td>3.2699</td>
      <td>0.0</td>
      <td>2018-02-08</td>
      <td>1.184759</td>
    </tr>
    <tr>
      <th>2018-02-09</th>
      <td>3.2844</td>
      <td>3.3075</td>
      <td>3.2708</td>
      <td>3.2846</td>
      <td>3.2846</td>
      <td>0.0</td>
      <td>2018-02-09</td>
      <td>1.189245</td>
    </tr>
  </tbody>
</table>
</div>


    INFO:fbprophet.forecaster:Disabling daily seasonality. Run prophet with daily_seasonality=True to override this.
    /Library/Python/2.7/site-packages/pystan/misc.py:399: FutureWarning: Conversion of the second argument of issubdtype from `float` to `np.floating` is deprecated. In future, it will be treated as `np.float64 == np.dtype(float).type`.
      elif np.issubdtype(np.asarray(v).dtype, float):





![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_55_2.png)




![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_55_3.png)



![png](Dataset%20modeling%20for%20financial%20time%20series%20data_files/Dataset%20modeling%20for%20financial%20time%20series%20data_55_4.png)


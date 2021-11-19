from datetime import time
import matplotlib
import pandas as pd
from matplotlib import pyplot as plt
from pandas.core.frame import DataFrame
from pandas.core.indexes.base import InvalidIndexError
import seaborn as sns
import numpy as np

dt = pd.read_csv('case_time_series.csv',parse_dates=['Date'],index_col="Date")

print(dt.head(5))


dt.TC.plot()
dt.TR.plot()
dt.TD.plot()
plt.title('Covid Cases India')
plt.ylabel('Cases in Millions')
plt.legend()
plt.show()


dt.DC.plot()
dt.DR.plot()
dt.DD.plot()
plt.title('Daily cases India')
plt.ylabel('cases in lakhs')
plt.legend()
plt.show()  


sns.violinplot("TC",data=dt)
plt.show()


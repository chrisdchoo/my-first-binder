import numpy as np
import matplotlib as plt
import pandas as pd
data = pd.read_csv("DB2_data.csv")
plt.plot(data.month, data.avg_temp, data.revenue)

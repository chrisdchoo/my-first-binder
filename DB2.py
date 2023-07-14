import numpy as np
import matplotlib as plt
import pandas as pd
data = pd.read_csv("DB2_data.csv")
data.plot(x="month", y=["avg_temp", "revenue($)"],
        kind="line", figsize=(10, 10))
 

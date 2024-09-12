import pandas as pd
import numpy as np
import matplotlib.pyplot as  plt
weather_data=pd.read_csv('/content/3791007.csv', parse_dates=['DATE'])
weather_data['DATE'] = pd.to_datetime(weather_data['DATE'])
weather_data.set_index('DATE', inplace=True)

# Display the data
weather_data.head()







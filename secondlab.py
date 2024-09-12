import pandas as pd
import numpy as np
import matplotlib.pyplot as  plt
weather_data=pd.read_csv("C:/Users/basar/PycharmProjects/DeepFarmingAndAgriFoodsProject/3791007.csv", parse_dates=['DATE'])
weather_data['DATE'] = pd.to_datetime(weather_data['DATE'])
weather_data.set_index('DATE', inplace=True)

# Display the data
print(weather_data.head())

weather_data['Month'] = weather_data.index.month
monthly_avg = weather_data.groupby('Month')['TMAX'].mean()

# Plotting seasonality (average temperature by month)
plt.figure(figsize=(10,6))
monthly_avg.plot(kind='bar', color='skyblue')
plt.title('Average Max Temperature by Month')
plt.xlabel('Month')
plt.ylabel('Temperature (Celsius)')
plt.show()






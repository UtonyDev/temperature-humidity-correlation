import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

try:
  path = 'open-meteo-tempt-humid-jan-jul-2025.csv'
  met_df = pd.read_csv(path)
  #print("original df: ", met_df)

  daysTemptAvgs = []
  daysHumidAvgs = []
  daysDateTime = []

  for day in range(0, 4344, 24):
    hourTemptList = []
    hourHumidList = []
    date_to_list = (met_df.loc[day, 'datetime'])[0:10]
    list_to_date = ''.join(date_to_list)
    daysDateTime.append( list_to_date ) 

    for hour in range(day, 24 + day, 1):
      #print(f'{hour}:00: {met_df.loc[hour, 'temperature']}')
      hourTemptList.append( float(met_df.loc[hour, 'temperature']) )
      hourHumidList.append( int(met_df.loc[hour, 'r_humidity']) )
    
    hourTemptArr = np.array(hourTemptList)
    hourHumidArr = np.array(hourHumidList)
    #print(f"day {int((day / 24) + 1)} \n --**-- mean tempt.: {round(np.mean(hourTemptArr) * 10 ) / 10.0}, \n --**-- mean humid.: {round(np.mean(hourHumidArr) * 10 ) / 10.0}, \n --**-- Tempt. list: {hourTemptArr}, \n --**-- Humid. list: {hourHumidArr} ")
    daysTemptAvgs.append(round(np.mean(hourTemptArr) * 10 ) / 10.0)
    daysHumidAvgs.append(round(np.mean(hourHumidArr) * 10 ) / 10.0)

  #print(f'The mean temperature for all {len(daysTemptAvgs)} days: {daysTemptAvgs} \n The mean humidity for all {len(daysHumidAvgs)} days: {daysHumidAvgs}')
  #print(f'datetime: {daysDateTime}')

  # Construct the DataFrame table for the daily averages
  avg_daily_met_dict = {
    'temperature' : daysTemptAvgs,
    'r_humidity' : daysHumidAvgs
  }

  avg_daily_met_df = pd.DataFrame(avg_daily_met_dict, index = daysDateTime)
  print("The complete df table: \n", avg_daily_met_df)

  avg_daily_met_df.plot(kind='scatter', x='temperature', y='r_humidity', title='Average Daily Temperature vs. Humidity (Jan-Jul 2025)')
  plt.show()
  
  avg_daily_met_corr = avg_daily_met_df.corr()
  print('Average daily data correlation: \n', avg_daily_met_corr)

  num_met_df = met_df.drop(columns=['datetime'])
  #print(f'The numerical df: \n {num_met_df} \n *****-----------------***** ')
  #(f'General Info: \n {num_met_df.info()} \n *****-----------------***** ')
  met_corr = num_met_df.corr()
  print(f'The hourly correlation: \n {met_corr} \n *****-----------------***** ')
  
except FileNotFoundError:
  print('File not found {FileNotFoundError}')

import matplotlib.pyplot as plt
from scipy import interpolate
import pandas as pd
import numpy as np
#from scipy.ndimage.filters import gaussian_filter1d


# two made-up timeseries with different periods, for demonstration plot below
#air_temp   = pd.DataFrame(np.random.randn(12), 
#                          index=pd.date_range('1/1/2016', freq='M', periods=12), 
#                          columns=['air_temp'])
#water_temp = pd.DataFrame(np.random.randn(365), 
#                          index=pd.date_range('1/1/2016', freq='D', periods=365), 
#                          columns=['water_temp'])

# the real data import would look something like this:
workouts_filepath = 'C:/Users/wosker4yan/Desktop/Work and Study/sendtex/Python_tutorials/matplotlib_habits_visualization/workouts.csv'
faps_filepath = 'C:/Users/wosker4yan/Desktop/Work and Study/sendtex/Python_tutorials/matplotlib_habits_visualization/f.csv.csv' 
CD = 'C:/Users/wosker4yan/Desktop/Work and Study/sendtex/Python_tutorials/matplotlib_habits_visualization/CD.csv'
PHOT = 'C:/Users/wosker4yan/Desktop/Work and Study/sendtex/Python_tutorials/matplotlib_habits_visualization/PHOT.csv'
PROG = 'C:/Users/wosker4yan/Desktop/Work and Study/sendtex/Python_tutorials/matplotlib_habits_visualization/PROG.csv'




workouts = pd.read_csv(workouts_filepath, header = 0, index_col = 0,
                         parse_dates=True, infer_datetime_format=True)
faps = pd.read_csv(faps_filepath, header = 0, index_col = 0,
                       parse_dates=True, infer_datetime_format=True)

photonics = pd.read_csv(PHOT, header = 0, index_col = 0,
                         parse_dates=True, infer_datetime_format=True)
cold_showers = pd.read_csv(CD, header = 0, index_col = 0,
                       parse_dates=True, infer_datetime_format=True)
programming = pd.read_csv(PROG, header = 0, index_col = 0,
                       parse_dates=True, infer_datetime_format=True)

#Gaussian filtered all the values
#or filtering 





# plot both overlayed


ax = faps.plot(figsize=(20,10))


workouts.plot(ax=ax)
photonics.plot(ax=ax)
programming.plot(ax=ax)
cold_showers.plot(ax=ax)


plt.legend(['NOFAP','workouts', 'Photonics','Porgramming','Cold Showers'])

plt.show()

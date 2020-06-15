import pandas as pd
import plotly.express as px

df = pd.read_csv('C:/Users/wosker4yan/Desktop/Work and Study/sendtex/Python_tutorials/workouts.csv')
df.head()


fig = px.line(df, x = 'date', y = 'score', title='workouts in time')
fig.show()
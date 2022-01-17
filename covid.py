import pandas as pd
import plotly.express as px

df = pd.read_csv("covid.csv")

fig = px.scatter(df, x = "Cases", y = "Date", color = "Country")
fig.show()
import pandas as pd
import plotly.express as px
df=pd.read_csv("https://s3-whitehatjrcontent.whjr.online/curriculum/PRO+Asset/Copy+of+data+-+data.csv")
graph=px.scatter(df,x="date",y="cases",color="country")
graph.show()
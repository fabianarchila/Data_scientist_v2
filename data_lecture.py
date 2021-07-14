import numpy as np 
import pandas as pd
import plotly.express as px



user_data=pd.read_csv('users.csv')  
new =user_data['user_createddate'].str.split(" ",n=1,expand = True)
new=new[0].value_counts()
# new=pd.DataFrame(new)

# new=new.sort_values()

# print(user_data['user_createddate'].value_counts())
print(new[0])

fig = px.line(x=[1, 2, 3, 4], y=[3, 5, 4, 8])




  
 





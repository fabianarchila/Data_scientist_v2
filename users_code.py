
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


user_data=pd.read_csv('users.csv')  #Read users file

# Some backgraund colors
colors = {
    'background': '#FFFFFF',
    'text': '#000000',
    'b_2':'#EFEAEA',
}   


# function that return datafame with date in days or months. The users duplicates are eliminate
def date_sort(data,period):
    new=data.copy()
    new.drop_duplicates(subset ="user_id",keep = False, inplace = True)
    if period==0:
        new['user_createddate']=new['user_createddate'].str.slice(0,10)

    elif period==1:
        new['user_createddate']=new['user_createddate'].str.slice(0,7)
    return new


####### Create the figure with the unique users each day.   
df_1=date_sort(user_data,0)
fig_1 = px.histogram(df_1, x=df_1['user_createddate'],nbins=1000,color_discrete_sequence=['DarkRed'])
fig_1.update_layout(
plot_bgcolor=colors['b_2'],
paper_bgcolor=colors['background'],
font_color=colors['text'],
title={
'text': "New unique users Daily",
'y':0.9,
'x':0.5,
'xanchor': 'center',
'yanchor': 'bottom'},
xaxis_title="Date",
yaxis_title="Users quantity",
font=dict(
        family="bold",
        size=18,
        color="FireBrick"
    )
# font_family="bold"
)

####### Create the figure with the unique users each month.   
df_2=date_sort(user_data,1)
fig_2 = px.histogram(df_2, x=df_2['user_createddate'],color_discrete_sequence=['crimson'])
fig_2.update_layout(
plot_bgcolor=colors['b_2'],
paper_bgcolor=colors['background'],
font_color=colors['text'],
title={
'text': "New unique users Monthly",
'y':0.9,
'x':0.5,
'xanchor': 'center',
'yanchor': 'bottom'},
xaxis_title="Date",
yaxis_title="Users quantity",
font=dict(
        family="bold",
        size=18,
        color="FireBrick"
    )
)


####### Create the figure with the users of each ecosystem
new_d=user_data.copy()
new_d.drop_duplicates(subset ="user_id",keep = False, inplace = True) #Eliminate the duplicates users

fig_5=px.histogram(df_1, x=df_1['ecosystem_name'],nbins=50,facet_col_spacing=0.1 ,color_discrete_sequence=['IndianRed'])
fig_5.update_layout(
plot_bgcolor=colors['b_2'],
paper_bgcolor=colors['background'],
font_color=colors['text'],
title={
'text': "Ecosystem users",
'y':0.9,
'x':0.5,
'xanchor': 'center',
'yanchor': 'bottom'},
xaxis_title="Ecosystem",
yaxis_title="Users quantity",
font=dict(
        family="bold",
        size=18,
        color="FireBrick"
    )
)


##### create the figure of Ecosystem money saved
new_2=user_data.copy()
new_2.drop_duplicates(subset ="user_id",keep = 'last', inplace = True) #Eliminate the first duplicates (the balance is actual)
df_6=new_2.groupby(['ecosystem_name']).money_user_balance_value.sum().reset_index() #Sum the value of the same escosytem

fig_6 = go.Figure(data=[go.Bar(
    x=df_6['ecosystem_name'],
    y=df_6['money_user_balance_value'],
    marker_color='SaddleBrown' # marker color can be a single color value or an iterable
)])

fig_6.update_layout(title={'text': 'Ecosystem money saved','y':0.8,'x':0.5,'xanchor': 'center','yanchor': 'bottom'},
        xaxis_title="Ecosystem",
        yaxis_title="Money",
        plot_bgcolor=colors['b_2'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'],
        font=dict(
        family="bold",
        size=18,
        color="FireBrick"
    ))


 





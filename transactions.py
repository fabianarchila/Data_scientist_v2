
import pandas as pd
import plotly.graph_objects as go

colors_2 = ['Chocolate',] * 2
colors_2[1] = 'crimson'
colors = {
    'background': '#FFFFFF',
    'text': '#000000',
    'b_2':'#EFEAEA',
}
transactions_data=pd.read_csv('transactions.csv')  


dff = transactions_data.groupby(["money_transaction_type_direction"]).balance_historic_transaction_value.sum().reset_index()

fig_3 = go.Figure(data=[go.Bar(
    x=dff['money_transaction_type_direction'],
    y=dff['balance_historic_transaction_value'],
    marker_color=colors_2 # marker color can be a single color value or an iterable
)])
fig_3.update_layout(title={'text': 'Money traced per channel','y':0.8,'x':0.5,'xanchor': 'center','yanchor': 'bottom'},
        xaxis_title="Transaction",
        yaxis_title="Users quantity",
        plot_bgcolor=colors['b_2'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'],
        font=dict(
        family="bold",
        size=18,
        color="FireBrick"
    ))

temp=transactions_data.copy()
temp['balance_historic_transaction_date']=temp['balance_historic_transaction_date'].str.slice(0,10)
temp['balance_historic_transaction_value']=temp['balance_historic_transaction_value']*temp['money_transaction_type_direction'].apply(lambda x:-1 if (x=='cash_out')else 1)
df_2=temp.groupby(['balance_historic_transaction_date']).balance_historic_transaction_value.sum().reset_index()
df_2=df_2.sort_values('balance_historic_transaction_date')
# print(df_2)

fig_4 = go.Figure(data=[go.Bar(
    x=df_2['balance_historic_transaction_date'],
    y=df_2['balance_historic_transaction_value'],
    marker_color='black' # marker color can be a single color value or an iterable
)])

fig_4.update_layout(title={'text': 'Temporary variation of the amount saved by users','y':0.8,'x':0.5,'xanchor': 'center','yanchor': 'bottom'},
        xaxis_title="Date",
        yaxis_title="Money",
        plot_bgcolor=colors['b_2'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'],
        font=dict(
        family="bold",
        size=18,
        color="FireBrick"
    ))

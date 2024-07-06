import pandas as pd
import dash
from dash import Dash, dcc, html
import plotly.express as px

border_deaths_by_discoverer = pd.read_csv("./data/border_deaths_by_discoverer.csv")
death_by_age                = pd.read_csv("./data/death_by_age.csv")
deaths_by_gender            = pd.read_csv("./data/deaths_by_gender.csv")
deaths_nationality          = pd.read_csv("./data/deaths_nationality.csv")
deathtype                   = pd.read_csv("./data/deathtype.csv")
mental_health_conditions_research  = pd.read_csv("./data/mental_health_conditions_research.csv")     
border_deaths_by_discoverer_FLIP = pd.melt(border_deaths_by_discoverer, id_vars=['Discoverer'], var_name='Year', value_name='Count')
death_by_age_Flip= pd.melt(death_by_age  , id_vars=['Age Group'], var_name='Year', value_name='Count')
deaths_nationality.rename(columns={'Nationality': 'location'}, inplace=True)
deaths_nationality_Flip= pd.melt(deaths_nationality, id_vars=['location'], var_name='Year', value_name='Confirmed')
deathtype_Flip = pd.melt(deathtype, id_vars=['Type of Death'], var_name='Year', value_name='Count')
dep = pd.DataFrame(mental_health_conditions_research.loc[:2])
anx = pd.DataFrame(mental_health_conditions_research.loc[3:5])
fati = pd.DataFrame(mental_health_conditions_research.loc[6:8])

fig1 = px.bar(border_deaths_by_discoverer_FLIP, x='Year', y='Count', color='Discoverer', barmode='group', title='Discoveries by USBP and Other* Over Years')
fig2 = px.scatter(death_by_age_Flip, x='Year', y='Count', color='Age Group', title='Discoveries by Age Group Over Years', labels={'Count':'Number of Discoveries'})
fig2.update_traces(marker=dict(size=15))
fig3 = px.choropleth( deaths_nationality_Flip, locations='location', locationmode='country names', color='Confirmed', hover_name='location', animation_frame='Year', title='Confirmed Deaths by Nationality Over Years')
fig4= px.line(deathtype_Flip, x='Year', y='Count', color='Type of Death', title='Death Types Over Years', labels={'Count':'Number of Deaths'})
fig5 = px.pie(dep, values = "percentage",names = "status",title = "Mental Health Condition")
fig6 = px.pie(anx, values = "percentage",names = "status",title = "Mental Health Condition")
fig7 = px.pie(fati, values = "percentage", names = "status",title = "Mental Health Condition")

graph1 = dcc.Graph(figure=fig1)
graph2 = dcc.Graph(figure=fig2)
graph3 = dcc.Graph(figure=fig3) 
graph4 = dcc.Graph(figure=fig4)
graph5 = dcc.Graph(figure=fig5)
graph6 = dcc.Graph(figure=fig6)
graph7 = dcc.Graph(figure=fig7) 


app =dash.Dash()
app.layout = html.Div([html.H1('Covid April', style={'textAlign': 'center', 'color': '#636EFA'}), 
                       graph1, 
                       graph2,
                       graph3, 
                       graph4,
                       graph5,
                       graph6,
                       graph7,
                
                       
])


if __name__ == '__main__':
     app.run_server()

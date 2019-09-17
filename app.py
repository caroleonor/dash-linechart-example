import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables ######

myheading = "Consultation Requests Academic Year 2017-2018 & 2018-2019"
mytitle = "Total case for 4 Major Purposes"
x_values = ['17 fall', '18 spring', '18 summer', '18 fall', '19 spring', '19 summer']
y1_values = [17, 15, 12, 30, 52, 33]
y2_values = [27, 11, 8, 24, 10, 29]
y3_values = [13, 9, 6, 14, 15, 14]
y4_values = [9, 5, 11, 10, 15, 10] 
color1 = '#F1948A'
color2 = '#34495E'
color3 = '#F1C40F'
color4 = '#8E44AD'
name1 = 'Instructional Design'
name2 = 'LMS'
name3 = 'Technology'
name4 = 'Assessment'
tabtitle = 'Consultation Case'
sourceurl = 'https://www.baseball-reference.com'
githublink = 'https://github.com/caroleonor/dash-linechart-example/edit/master/app.py'

########### Set up the chart

# create traces
trace0 = go.Scatter(
    x = x_values,
    y = y1_values,
    mode = 'lines',
    marker = {'color': color1},
    name = name1
)
trace1 = go.Scatter(
    x = x_values,
    y = y2_values,
    mode = 'lines',
    marker = {'color': color2},
    name = name2
)
trace2 = go.Scatter(
    x = x_values,
    y = y3_values,
    mode = 'lines',
    marker = {'color': color3},
    name = name3
)

# assign traces to data
data = [trace0, trace1, trace2]
layout = go.Layout(
    title = mytitle
)

# Generate the figure dictionary
fig = go.Figure(data=data,layout=layout)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()

import dash
from dash import Dash, dcc, html 
import dash_bootstrap_components as dbc
from sidebar import create_sidebar
#css styles
FA621='https://use.fontawesome.com/releases/v6.2.1/css/all.css'
appstyle=['https://codepen.io/chriddyp/pen/bWLwgP.css']
SIDEBAR=create_sidebar()
APP_TITLE='MGC SOFT'

#intialise the app
app=Dash(
    __name__,
    suppress_callback_exceptions=True, #no displaying of error messages to users screen due to bad code
    external_stylesheets=[FA621, appstyle, dbc.themes.LUX,dbc.themes.FLATLY],
    title=APP_TITLE,
    use_pages=True,
    #pages_folder=''
)

#define the app layout
app.layout=dcc.Loading(
    id='loading_content',
    children=[
        dbc.Row([
            dbc.Col([SIDEBAR], xs=12, sm=12, md=3, lg=3, xl=2, xxl=2),
            dbc.Col([
                html.Div(
                    dash.page_container, 
                    style={
                        'boxShadow': '0 4px 8px rgba(1, 0.9, 0.8, 0.9)',  # Add box shadow here
                        "padding": "20px",
                        "background-color": "#add8e6",
                        "border-radius": "6px",
                        "margin-top": "20px",
                        "margin-left": 15,
                        "width": 1550,  # Adjust width to account for sidebar
                        "height":880,  # Adjust height to account for margins
                        "overflowY": "scroll",  # Enable vertical scrolling
                        "background-image": "url('assets/mlima.jpg')",  # Set the background image
                        "background-size": "cover",  # Cover the entire container
                        "background-repeat": "no-repeat",  # Do not repeat the image
                        "background-position": "center"  # Center the image
                    }
                )
            ], xs=12, sm=12, md=9, lg=9, xl=10, xxl=10)
        ])
    ],
    #fullscreen=True,
    #color='primary',
)


#run the app
if __name__ =='__main__':
    app.run(debug=True, threaded=True, port=8888)
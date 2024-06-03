from dash import html
import dash_bootstrap_components as dbc

def create_sidebar():
    sidebar = html.Div(
        [
            html.Div(
                html.H3(
                    [
                        html.Span('Earth', style={'font-weight': 'bold', 'margin-left': 20, 'color': '#4a5d23'}),
                        html.Br(),
                        html.Span('Observation ', style={'font-weight': 'bold', 'margin-left': 20, 'color': '#4a5d23'}),
                        html.Br(),
                        html.Span('Dashboard', style={'font-weight': 'bold', 'margin-left': 20, 'color': '#4a5d23'})
                    ]
                )#, style={'backgroundColor':'#010103'}
            ),
            html.Hr(),
            html.Div([
                dbc.Nav(
                    [
                        dbc.NavItem(
                            dbc.NavLink(
                                [
                                    html.I(className='fa-solid fa-house'),
                                    'Home',  # text beside icon
                                ],
                                href='/',  # root path i.e to loading page
                                style={
                                    # 'color': 'black',
                                    'fontSize': 25
                                },
                            )
                        ),
                        dbc.NavItem(
                            dbc.NavLink(
                                [
                                    html.I(className='fa-solid fa-folder-open'),
                                    'About',  # text beside icon
                                ],
                                href='/about',
                                style={
                                    # 'color': 'black',
                                    'fontSize': 25
                                },
                            )
                        ),
                        dbc.NavItem(
                            dbc.NavLink(
                                [
                                    html.I(className='fa-solid fa-window-restore'), 
                                    'Store',  # text beside icon
                                ],
                                href='/store',
                                style={
                                    # 'color': 'black',
                                    'fontSize': 25
                                },
                            )
                        ),
                        dbc.NavItem(
                            dbc.NavLink(
                                [
                                    html.I(className='fa-solid fa-circle-question'), 
                                    'FAQs',  # text beside icon
                                ],
                                href='/faqs',
                                style={
                                    # 'color': 'black',
                                    'fontSize': 25
                                },
                            )
                        ),
                        dbc.NavItem(
                            dbc.NavLink(
                                [
                                    html.I(className='fa-brands fa-github'), 
                                    'GitHub',  # text beside icon
                                ],
                                href='https://github.com/mulyung1',
                                target='_blank_',  # applies to external links only
                                style={
                                    # 'color': 'black',
                                    'fontSize': 25
                                },
                            )
                        ),
                        dbc.NavItem(
                            dbc.NavLink(
                                [
                                    html.I(className='fa-brands fa-medium'), 
                                    'Medium',  # text beside icon
                                ],
                                href='https://medium.com/@victorsonofmartin',
                                target='_blank_',
                                style={
                                    # 'color': 'black',
                                    'fontSize': 25
                                },
                            )
                        ),
                    ]
                )
                ], style={
                    #'backgroundColor':'#010103', 
                    'height':350}
            ),
            html.Div([
                html.Img(src='assets/R.jpeg', style={'width': '100%', 'height': 'auto'})], 
                    style={
                        #'backgroundColor':'#010103', 
                        'height':350,}
            )
        ],
        style={
            'margin-left': 20,
            'margin-top': 20,
            'backgroundColor': '#ecebbd',
            'height': 880,
            'width': 300,
            'borderRadius': 6,
            'boxShadow': '0 4px 8px rgba(1, 0.9, 0.8, 0.9)'  # Add box shadow here
        }
    )
    return sidebar

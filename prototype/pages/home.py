from dash import html, register_page, dcc, callback, Output, Input
import dash_bootstrap_components as dbc
import folium
import requests
from dash.exceptions import PreventUpdate

register_page(
    __name__,
    name='MGC SOFT SOLNS',
    top_nav=True,
    path='/'
)

#load the data
geod=requests.get(
    'https://raw.githubusercontent.com/python-visualization/folium-example-data/main/world_countries.json'
    ).json()
def layout():
    return dbc.Container([
        dcc.Store(id='geojson_data', data=geod),
        html.H6('Data and evidence to strengthen baseline assessments, inform interventions and monitor impacts across landscapes', style={'font-weight':'bold'}),
        dbc.Row([
            dbc.Col([
                html.Blockquote("This dashboard was developed in response to the ongoing challenge of increasing the impact of development projects through better-informed project design, by using improved baseline assessments, and through results-based management on the ground.",
                    style={
                        "border-left": "5px solid #ccc",
                        "margin": "1.5em 10px",
                        "padding": "0.5em 10px",
                        #"font-style": "italic",
                        "background-color": "#8fbc8f",
                        "border-radius": "4px",
                        'width':200,
                        'boxShadow': '0 4px 8px rgba(1, 0.9, 0.8, 0.9)'  # Add box shadow here
                    }
                ),
            ])
        ]),
        dbc.Row([
            dbc.Col([
                html.Div([
                    html.P('We use robust, readily measurable, and scientifically rigorous, indicators to assess landscape “ecosystem health” in terms of both biophysical indicators (e.g. soil erosion, soil fertility and vegetation dynamics), and socio-economic indicators. Here, the recent revolution in quality and accessibility of Earth Observation (EO) data presents a major opportunity for smallholder farmers and to development projects. Combining EO data of landscape-level ecosystem health, with field level information on production and household income will result in a leap forward in terms of impact.', style={'margin-left':20})
                    ], style={
                        'width': 700,
                        'border-radius':6,
                        'backgroundColor': '#8fbc8f',
                        'boxShadow': '0 4px 8px rgba(1, 0.9, 0.8, 0.9)',  # Add box shadow here
                        #'margin': '20px'
                    }),
                dcc.Graph(id='s')
            ], width=6),
            dbc.Col([
                html.Div(html.Iframe(id='map'), style={'width': '100%', 'height': '80vh'})
            ], width=6)
        ])
    ], fluid=True, 
    style={
        #'backgroundColor':'#010103',
        'height':1180,
        'width':1500,
        'borderRadius':6,
    })

#callback to udate map
@callback(
    Output('map','srcDoc'),
    Input('geojson_data','data')
)
def update_map(geojson_data):
    if geojson_data is None:
        raise PreventUpdate
    
    #create folium map
    m=folium.Map(
        location=[-1.294293047629149, 36.886483551713546],
        zoom_start=2
    )

    # Add multiple tile layers
    folium.TileLayer('openstreetmap').add_to(m)  # OpenStreetMap
    folium.TileLayer('cartodbpositron').add_to(m)  # CartoDB Positron

    # folium.Choropleth(
    #     geo_data=geojson_data,
    #     name="choropleth",
    #     data=filtered_df,
    #     columns=["country", selected_value],
    #     key_on="feature.properties.name",
    #     fill_color="YlGn",
    #     fill_opacity=0.7,
    #     line_opacity=0.2,
    #     legend_name=f"{selected_value} Rate",
    #     tooltip=folium.GeoJsonTooltip(fields=['name', selected_value], aliases=['Country', selected_value], localize=True),
    # ).add_to(m)

    # Add layer control to switch between tile layers
    folium.LayerControl().add_to(m)

    # Save the map to an HTML file
    map_path = 'map.html'
    m.save(map_path)

    # Read the HTML file and return it as the source for the iframe
    with open(map_path, 'r') as f:
         map_html = f.read()

    return map_html
import dash
import dash_leaflet as dl
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    dl.Map(style={'width': '1000px', 'height': '500px'}, center=[0, 0], zoom=10, children=[
        dl.TileLayer(),
        dl.GeoJSON(data={
            "type": "Feature",
            "properties": {
                    "name": "Coors Field",
                    "amenity": "Baseball Stadium",
                    "popupContent": "This is where the Rockies play!",
                },
            "geometry": {
                    "type": "Point",
                    "coordinates": [0, 0]
                }
        })
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8053)

import dash

import dash_leaflet as dl
import dash_html_components as html
import numpy as np
import random
import json

center = np.array([56.05, 10.25])
randx = [random.random() for i in range(1000)]
randy = [random.random() for i in range(1000)]

points = np.array(list(zip(randx, randy)))

circles = []
for idx, point in enumerate(points):
    circle = {
        "key": str(idx),
        "properties": {
            "radius": 10
        },
        "geometry": {
            "type": "Point",
            "coordinates": (center + point).tolist()
        }
    }
    circles.append(circle)

circles = json.dumps(circles)


app = dash.Dash()
app.layout = html.Div([
    dl.Map(style={'width': '1000px', 'height': '500px'}, center=center, zoom=10, children=[
        dl.TileLayer(),
        dl.Circle(center=center.tolist(), radius=10)
#         dl.GeoJSON(data=Circle([1, 0]))
    ])
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8053)

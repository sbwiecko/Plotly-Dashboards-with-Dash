#######
# Objective: Create a dashboard that takes in two or more
# input values and returns their product as the output.
######
# for this exercice we will use a RangeSlider component

# Perform imports here:
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Launch the application:
app = dash.Dash()

# Create a Dash layout that contains input components
# and at least one output. Assign IDs to each component:
app.layout = html.Div(
    [
        html.Label('RangeSlider'),
        dcc.RangeSlider(
            id='my-range-slider',
            min=-5,
            max=6,
            step=None,
            marks={_: str(_) for _ in range(-5, 7)},   # str otherwise zero doesn't show
            value=[-5, 1]
        ),
        html.Div(id='output-multiplication', style={
            'margin-top': 20,
            'font-family': 'cursive',
            'font-size': '26px'
            }
        ),
    ]
)

# Create a Dash callback:
@app.callback(
    Output(component_id='output-multiplication', component_property='children'),
    [Input(component_id='my-range-slider', component_property='value')]
)
def update_view(range_limits):
    return range_limits[0] * range_limits[1]

# Add the server clause:
if __name__ == '__main__':
    app.run_server()

#######
# A very basic Input/Output callback, with State!
######
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(
        id='number-in',
        value=1,
        style={'fontSize':28}
    ),
    html.Button(
        id='submit-button',
        n_clicks=0,
        children='Submit',
        style={'fontSize':28}
    ),
    html.H1(id='number-out')
])

@app.callback(
    Output('number-out', 'children'),       # Input triggers the underlying function, with the option to use it's own Input value
    [Input('submit-button', 'n_clicks')],   # when the Input value(n_clicks) changes, it **triggers** the output function,
    [State('number-in', 'value')])          # which uses both the Input value and the State Value to update the Output.
def output(n_clicks, number):   # notice how n_clicks is linked to n_clicks(Input), and value is linked to the value(State)
    return number               # The Input value(n_click) isn't used in the output function, it serves purely as a **trigger**.

# Input and State are basically the same, the main difference being
# that State doesn't have the ability to trigger the underlying function.

if __name__ == '__main__':
    app.run_server()

#######
# This provides examples of Dash HTML Components.
# Feel free to add things to it that you find useful.
######
import dash
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(
    [
        'This is the outermost Div',
        html.Div(
            'This is an inner Div',    # for single item no need for list as a Div children
            style={
                'color':'blue',
                'border':'2px blue solid',
                'borderRadius':5,
                'padding':10,
                'width':100
            }
        ),
        html.Div(
            'This is another inner Div',
            style={
                'color':'green',
                'border':'4px green solid',
                'margin':5,
                'width':100
            }
        ),
    ],
    # this styles the outermost Div:
    style={
        'width':300,
        'height':100,
        'color':'red',
        'border':'2px red dotted'
    }
)

if __name__ == '__main__':
    app.run_server()

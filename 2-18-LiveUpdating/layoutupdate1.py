#######
# This page updates when refreshed.
######
import dash
import dash_html_components as html
from datetime import datetime

app = dash.Dash()

crash_free = 0

def update_layout():
    global crash_free
    crash_free += 1
    return html.H1('Crash free for {}; time is: '.format(crash_free) + str(datetime.now()))

app.layout = update_layout   # no parentheses has refreshing the page calls app.layout

if __name__ == '__main__':
    app.run_server()

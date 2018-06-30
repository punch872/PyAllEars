import base64
import os
from urllib.parse import quote as urlquote

from flask import Flask, send_from_directory
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


UPLOAD_DIRECTORY = '/Users/shahud/Desktop/profileanalyzer/'

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


# Normally, Dash creates its own Flask server internally. By creating our own,
# we can create a route for downloading files directly:
server = Flask(__name__)
app = dash.Dash(server=server)

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

@server.route('/Users/shahud/Desktop/profileanalyzer/<path:path>')
def download(path):
    """Serve a file from the upload directory."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)

image_filename = 'spy.jpg' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

app.layout = html.Div(
    [
        html.Img(src='data:spy/image;base64,{}'.format(encoded_image.decode())),
        html.H1('PyAllEars : Twitter Profile Analyzer', style={'color':"#FFFFFF",'textAlign': 'center'}),
        html.H2('1 - Enter a twitter user name without #', style={'color':"#FFFFFF",'textAlign': 'center'}),
        html.Div(dcc.Input(id='input-box', type='text')),
        html.Button('Submit', id='button'),
        html.Div(id='output-container-button'),
        dcc.Upload(
            id='upload-data',
            children=html.Div([
#                'Drag and drop or click to select a file to upload.'
            ]),

        ),
        html.H2('2 - WAIT FOR ONE MINUTE! and then Press the "profile.txt" link to download file', style={'color':"#FFFFFF",'textAlign': 'center'}),
        html.H3(id='file-list', style={'color':"text",'textAlign': 'center'})
    ], style={'backgroundColor': '#000000', 'margin-top':'-30px', 'height':'2000px','textAlign': 'center'},
)


def save_file(name, content):
    """Decode and store a file uploaded with Plotly Dash."""
    data = content.encode('utf8').split(b';base64,')[1]
    with open(os.path.join(UPLOAD_DIRECTORY, name), 'wb') as fp:
        fp.write(base64.decodebytes(data))


def uploaded_files():
    """List the files in the upload directory."""
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return files


def file_download_link(filename):
    """Create a Plotly Dash 'A' element that downloads a file from the app."""
    location = '/Users/shahud/Desktop/profileanalyzer/{}'.format(urlquote(filename))
    return html.A(filename, href=location)

@app.callback(
    dash.dependencies.Output('output-container-button', 'children'),
    [dash.dependencies.Input('button', 'n_clicks')],
    [dash.dependencies.State('input-box', 'value')])
def update_output(n_clicks, value):
#    return 'The input value was "{}" and the button has been clicked {} times'.format(
#        value,
#        n_clicks
#    )
    os.system('python3 tweets_analyzer.py -n {} > profile.txt'.format(value))
    os.system('cp profile.txt ../profile.txt')





@app.callback(
    Output('file-list', 'children'),
    [Input('upload-data', 'filename'), Input('upload-data', 'contents')]
)
def update_output(uploaded_filenames, uploaded_file_contents):
    """Save uploaded files and regenerate the file list."""

    if uploaded_filenames is not None and uploaded_file_contents is not None:
        for name, data in zip(uploaded_filenames, uploaded_file_contents):
            save_file(name, data)

    files = uploaded_files()
    if len(files) == 0:
        return [html.Li('No files yet!')]
    else:
        return [html.Li(file_download_link(filename)) for filename in files]




if __name__ == '__main__':
    app.run_server(debug=True)

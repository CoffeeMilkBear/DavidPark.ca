from flask.helpers import send_from_directory
from gmail import sendProxyEmail
from flask import Flask, request

app = Flask(__name__, static_url_path='')

# All static routes are handled in app.yaml. This route is only used when running locally
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/leaveMessage', methods=['POST'])
def leaveMessage():
    sender = request.form['email']
    message = request.form['message']
    sendProxyEmail(sender, 'mdilac52@gmail.com', message)
    return 'OK', 200


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)

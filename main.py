from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', favicon.ico)
@app.route('/css/main.css')
def maincss():
    return send_from_directory('static/css', 'main.css')
@app.route('/images/default.jpg')
def defaultjpg():
    return send_from_directory('static/images', 'default.jpg')
@app.route('/images/logo.png')
def logopng():
    return send_from_directory('static/images', 'logo.png')
@app.route('/images/project1.png')
def project1png():
    return send_from_directory('static/images', 'project1.png')
@app.route('/images/mobilemenu.svg')
def mobilemenusvg():
    return send_from_directory('static/images', 'mobilemenu.svg')
@app.route('/images/mobilemenuexit.svg')
def mobilemenuexitsvg():
    return send_from_directory('static/images', 'mobilemenuexit.svg')

if __name__ == "__main__":
    app.run() 

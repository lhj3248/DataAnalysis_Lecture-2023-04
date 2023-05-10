from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello Flask'

@app.route('/Home')
def Home():
    return render_template('13.carousel.html')

@app.route('/scatter')
def scatter():
    return render_template('09.scatter.html')

@app.route('/hotPlace')
def hotPlace():
    return render_template('10.hotPlace.html')

@app.route('/interpark')
def interpark():
    return render_template('11.interpark.html')

@app.route('/progressbar')
def progressbar():
    return render_template('13.progressbar.html')

if __name__ == '__main__':
    app.run(debug=True)
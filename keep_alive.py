from flask import Flask, render_template
from threading import Thread

app = Flask('Music App', template_folder='templates')

@app.route('/')
def home():
    return render_template('homepage.html')

@app.route('/edward')
def Edward():
    return "Hi fans"
    #return render_template("homepage.html")



def run():
    app.run(host='0.0.0.0', port=8080)


def keep_alive():
    t = Thread(target=run)
    t.start()

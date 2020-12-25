from flask import Flask, render_template
from threading import Thread

app = Flask('Web Page')

@app.route('/')
def home():
    return render_template("homepage.html")

@app.route("/Edward")
def Edward():
  return "Hello World!!1!"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()
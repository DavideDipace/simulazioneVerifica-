from flask import Flask, render_template
app = Flask(__name__)

import datetime

@app.route('/')

def index():
  return render_template("index4.html", Ora=datetime.datetime.now())

@app.route('/mappa')

def mappa():
  return render_template("index5.html",)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__,static_url_path=None, static_folder='static', static_host=None)

@app.route('/')
def profile():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def Submit():
    if request.method == 'POST':
        user = request.form['val']
        comp = random.choice("rps")
        return render_template("result.html",user = user, comp = comp)

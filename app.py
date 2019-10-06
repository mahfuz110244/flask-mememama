from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def make_meme():
    return render_template('base.html', name="MRK")
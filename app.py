from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def make_meme():
    return render_template('base.html',
                           name="MRK",
                           first_line=request.form.get('first_line'),
                           last_line=request.form.get('last_line'))
from flask import Flask, render_template, request
import json

app = Flask(__name__)

memes = []

def load_memes():
    with open('memes.json', 'r') as f:
        memes.extend(json.load(f))

def save_memes():
    with open('memes.json', 'w') as f:
        json.dump(memes, f)

def get_meme(meme_id: int):
    return memes[meme_id]

def add_meme(first_line: str, last_line: str):
    memes.append({
            'first_line': first_line,
            'last_line': last_line
        })
    # save the memes in json files
    save_memes()

@app.route('/', methods=['GET', 'POST'])
def make_meme():
    first_line = request.form.get('first_line', '')
    last_line = request.form.get('last_line', '')

    if request.method == 'POST':
        add_meme(first_line, last_line)
    print(memes)

    return render_template('base.html',
                           name="MRK",
                           first_line=first_line,
                           last_line=last_line)

@app.route('/view/<int:meme_id>')
def view_meme(meme_id):
    meme = get_meme(int(meme_id))
    return render_template('view.html',
                           first_line=meme.get('first_line'),
                           last_line=meme.get('last_line'))

# loads the memes from json file
load_memes()
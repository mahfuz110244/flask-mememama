from flask import Flask, render_template, request, abort
from data import add_meme, get_meme, load_memes, get_all_memes

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def make_meme():
    first_line = request.form.get('first_line', '')
    last_line = request.form.get('last_line', '')

    if request.method == 'POST':
        add_meme(first_line, last_line)

    return render_template('create.html',
                           name="MRK",
                           first_line=first_line,
                           last_line=last_line)

@app.route('/list')
def list_memes():
    return render_template('list.html', memes=get_all_memes())

@app.route('/view/<int:meme_id>')
def view_meme(meme_id):
    try:
        meme = get_meme(int(meme_id))
    except IndexError:
        abort(404)
    return render_template('view.html',
                           first_line=meme.get('first_line'),
                           last_line=meme.get('last_line'))

# loads the memes from json file
load_memes()
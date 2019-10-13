import json, os

memes = []
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(BASE_DIR, 'memes.json')

def load_memes():
    with open(filename, 'r') as f:
        memes.extend(json.load(f))

def save_memes():
    with open(filename, 'w') as f:
        json.dump(memes, f)

def get_meme(meme_id: int):
    return memes[meme_id]

def get_all_memes():
    return memes

def add_meme(first_line: str, last_line: str):
    memes.append({
            'first_line': first_line,
            'last_line': last_line
        })
    # save the memes in json files
    save_memes()
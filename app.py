from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    meaning = None
    if request.method == 'POST':
        word = request.form.get('word')
        if word:
            response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
            if response.status_code == 200:
                data = response.json()
                if data:
                    meaning = data[0]['meanings'][0]['definitions'][0]['definition']
                else:
                    meaning = "No meaning found."
            else:
                meaning = "Error fetching meaning."
    return render_template('index.html', meaning=meaning)

if __name__ == '__main__':
    app.run(debug=True)

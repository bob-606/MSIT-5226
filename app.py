from flask import Flask, request, jsonify, render_template
import sqlite3
from googletrans import Translator

app = Flask(__name__)
DATABASE = 'translations.db'

def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language).text
    return translated_text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.get_json()
    text = data['text']
    target_language = data.get('target_language', 'pt')  # Default to Portuguese
    translated_text = translate_text(text, target_language)
    
    # Save translation data to database
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO WordTranslations (original_text, translated_text) VALUES (?, ?)", (text, translated_text))
    conn.commit()
    conn.close()
    
    return jsonify({'translated_text': translated_text})

if __name__ == '__main__':
    app.run(debug=True)

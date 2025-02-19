from flask import Flask, request, jsonify
from flask_cors import CORS
from googletrans import Translator
app = Flask(__name__)
CORS(app)
translator = Translator()
@app.route('/', methods=['POST'])
def translate():
    data = request.get_json()
    text_to_translate = data.get('sentence', '')
    target_language = data.get('target_lang', 'es')
    try:
        if not text_to_translate:
            return jsonify({'error': 'No sentence provided for translation.'}), 400
        
        translated = translator.translate(text_to_translate, dest=target_language)
        return jsonify({'translated_text': translated.text})
    except exceptions.TranslatorError as e:
        return jsonify({'error': f'Translation failed: {str(e)}'}), 500
    except Exception as e:
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500
@app.route("/health", methods=["GET"])
def health_check():
    """Check if the server is running."""
    return jsonify({"status": "ok"}), 200
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

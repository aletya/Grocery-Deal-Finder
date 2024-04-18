from flask import Flask, request, jsonify
from flask import Flask
from aldi_scraper import get_deals


app = Flask(__name__)

@app.route('/')
def test():
    return "API is working!"

@app.route('/aldi', methods=['GET'])
def aldi_deals():
    user_zip_code = request.args.get('zip_code')
    if user_zip_code:
        user_zip_code = int(user_zip_code)
        return jsonify({'deals': get_deals(user_zip_code)}), 200
    else:
        return jsonify({'error': 'Status code not provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
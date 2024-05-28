from flask import Flask, request, jsonify, send_from_directory
from serpapi import GoogleSearch


app = Flask(__name__)

API_KEY = '1c3c1c37098aea78de666527cad93b0e249973cf1f7b3048fc7ea5458097c6a4'

@app.route('/')
def home():
    return send_from_directory('', 'index.html')

@app.route('/search')
def search():
    keyword = request.args.get('keyword')
    params = {
        "q": keyword,
        "hl": "cs",
        "gl": "cz",
        "google_domain": "google.cz",
        "api_key": API_KEY
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    
    organic_results = results.get('organic_results', [])
    return jsonify(organic_results)

if __name__ == '__main__':
    app.run(debug=True)

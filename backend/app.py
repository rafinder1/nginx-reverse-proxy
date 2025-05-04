from flask import Flask, jsonify

app = Flask(__name__)

teams = [
    {"id": 1, "name": "FC Barcelona"},
    {"id": 2, "name": "Manchester City"},
]

matches = [
    {"home": "FC Barcelona", "away": "Real Madrid", "score": "2-1"},
    {"home": "Manchester City", "away": "Arsenal", "score": "3-0"},
]

@app.route('/api/teams')
def get_teams():
    return jsonify(teams)

@app.route('/api/matches')
def get_matches():
    return jsonify(matches)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

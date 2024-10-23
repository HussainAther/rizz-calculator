# app.py

from flask import Flask, request, jsonify
from rizz_calculator import calculate_rizz, get_user_input

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate_rizz_route():
    data = request.json
    rizz_score = calculate_rizz(data)
    return jsonify({"rizz_score": rizz_score})

if __name__ == '__main__':
    app.run(debug=True)

# rizz_calculator/rizz_calculator.py

def calculate_rizz(user_data):
    total_score = (
        user_data.get('skibidy_rizz', 0) +
        user_data.get('sigma_wolf', 0) +
        user_data.get('chaos_level', 0)
    )

    if total_score >= 25:
        return "You’ve got **Ohio Level 10 Rizz**! Ultimate Sigma Alpha Wolf vibes—everyone’s feeling you."
    elif total_score >= 15:
        return "Solid **Gyatt** level! You’re good, but there’s room for more Skibidy energy."
    else:
        return "Looks like you’re sitting at **L Rizz**. Might be time to tap into some **Grimace Shake** magic!"


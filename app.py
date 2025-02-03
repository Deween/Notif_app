
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    # Get data from the POST request
    data = request.get_json()

    # Print the received data (this will show in Render logs)
    print(f"Received data: {data}")

    # Respond back with the data
    return jsonify({"message": "Data received successfully", "data": data}), 200

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)

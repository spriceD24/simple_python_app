from flask import Flask, request, jsonify
from flask_cors import CORS
import re, time
app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload():
    try:
        data = request.json
        print("Received data:")
        for key, value in data.items():
            print(f"{key}: {value}")
        return jsonify({"message": "Data received successfully!"}), 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"message": "Error processing data!"}), 500

@app.route('/validate', methods=['POST'])
def validate():
    try:
        data = request.json
        result = {}
        print("Validating data:")
        for key, value in data.items():
            print(f"{key}: {value}")
        for key, value in data.items():
            if value < 0:
                result[key] = "Error"
            else:
                result[key] = "OK"
        return jsonify(result), 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({"message": "Error processing data!"}), 500


@app.route('/wire', methods=['GET'])
def multiply_text_length():
    # Get the 'text', 'number', and 'delay' parameters from the query string
    text = request.args.get('text', '')
    number = request.args.get('number', type=int)
    delay = request.args.get('delay', type=float)  # Optional delay parameter, expected as float

    print(f'Calling WIRE {text}, {number}')

    # If the delay parameter is provided and is a positive number, apply the delay
    if delay and delay > 0:
        print(f'Delaying response by {delay} seconds')
        time.sleep(delay)

    # Calculate the result
    result = len(text) * number

    # Return the result as a JSON response
    return jsonify({"result": result})



if __name__ == '__main__':
    app.run(debug=True)

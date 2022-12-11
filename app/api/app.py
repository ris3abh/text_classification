from flask import flash, Flask, jsonify, redirect, request, url_for
from utilities import predict_pipeline

app = Flask(__name__)


@app.post('/predict')
def predict():
    data = request.json
    try:
        sample = data['text']
    except KeyError:
        return jsonify({'error': 'Missing text.'})

    sample = [sample]
    predictions = predict_pipeline(sample)
    try:
        result = jsonify(predictions[0])
    except KeyError:
        result = jsonify({'error': 'Error in prediction.'})
    return result

if __name__ == '__main__':
    app.run(debug = True)

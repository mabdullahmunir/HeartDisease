import os
import sys
import pickle
import json

from sklearn.neural_network import MLPClassifier
from flask import (
	Flask, request, abort, render_template
)

app = Flask(__name__)

@app.route("/predict", methods=['POST'])
def predict():
	# print request.form
	with open('model', 'rb') as fin:
		mdl = pickle.load(fin)

	data = [	
		float(request.form['age']),
		float(request.form['sex']),
		float(request.form['chest']),
		float(request.form['bpressure']),
		float(request.form['cholesterol']),
		float(request.form['blood_sugar']),
		float(request.form['ecg']),
		float(request.form['max_heart']),
		float(request.form['angina']),
		float(request.form['st_depression']),
		float(request.form['peak_st']),
		float(request.form['c_vessel']),
		float(request.form['thal'])
	]
	diagnosis = mdl.predict([data])

	return json.dumps({
		"diagnosis" : str(diagnosis[0])
	})

@app.route("/", methods=['GET'])
def index():
	return render_template('index.html')


if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)
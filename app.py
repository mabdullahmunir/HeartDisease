import pickle

from sklearn.neural_network import MLPClassifier
from flask import (
	Flask, request, render_template
)

app = Flask(__name__)
with open('model', 'rb') as fin:
	mdl = pickle.load(fin, encoding='latin1')

def prepare():
	DEFAULT_AGE= 1
	DEFAULT_SEX = 1
	DEFAULT_CHEST = 1
	DEFAULT_BLOOD_PRESSURE = 115
	DEFAULT_CHOLESTROL = 190
	DEFAULT_BLOOD_SUGAR = 0
	DEFAULT_ECG = 0
	DEFAULT_MAX_HEART = 150 
	DEFAULT_ANGINA = 0 
	DEFAULT_ST_DEPRESSION = 1 
	DEFAULT_PEAK_ST = 2 
	DEFAULT_C_VESSEL = 1 
	DEFAULT_THAL = 3

	data = []
	data.append(request.form['age']) if (request.form['age'] != '') else data.append(DEFAULT_AGE)
	data.append(request.form['sex']) if (request.form['sex'] != '') else data.append(DEFAULT_SEX)
	data.append(request.form['chest']) if (request.form['chest'] != '') else data.append(DEFAULT_CHEST)
	data.append(request.form['bpressure']) if (request.form['bpressure'] != '') else data.append(DEFAULT_BLOOD_PRESSURE)
	data.append(request.form['cholesterol']) if (request.form['cholesterol'] != '') else data.append(DEFAULT_CHOLESTROL)
	data.append(request.form['bloodSugar']) if (request.form['bloodSugar'] != '') else data.append(DEFAULT_BLOOD_SUGAR)
	data.append(request.form['ecg']) if (request.form['ecg'] != '') else data.append(DEFAULT_ECG)
	data.append(request.form['maxHeart']) if (request.form['maxHeart'] != '') else data.append(DEFAULT_MAX_HEART)
	data.append(request.form['angina']) if (request.form['angina'] != '') else data.append(DEFAULT_ANGINA)
	data.append(request.form['stDepression']) if (request.form['stDepression'] != '') else data.append(DEFAULT_ST_DEPRESSION)
	data.append(request.form['peakSt']) if (request.form['peakSt'] != '') else data.append(DEFAULT_PEAK_ST)
	data.append(request.form['cVessel']) if (request.form['cVessel'] != '') else data.append(DEFAULT_C_VESSEL)
	data.append(request.form['thal']) if (request.form['thal'] != '') else data.append(DEFAULT_THAL)

	return data;	

@app.route("/", methods=['GET'])
def index():
	return render_template('index.html')

@app.route("/error", methods=['GET'])
def error():
	return render_template('error.html')

@app.route("/predict", methods=['POST'])
def predict():
	global mdl
	data = prepare()
	diagnosis = mdl.predict([[float(x) for x in data]])[0]

	return render_template('result.html', diagnosis = diagnosis, data = data)

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=5000, debug=True)
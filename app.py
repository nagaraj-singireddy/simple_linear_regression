'''
in this file we are going to write the backend code to load the model and give prediction
'''
import flask
import numpy as np
from flask import render_template, request, Flask
import pickle
app = Flask(__name__)
from sklearn.linear_model import LinearRegression
with open('SLR_MODEL.pkl', 'rb') as f:
    model = pickle.load(f)
@app.route('/')
def default_site():
    return render_template('index.html')
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    value = request.form.values()
    value = [float(i) for i in value]
    value= np.array([value])
    result =model.predict(value)[0]
    return render_template('index.html', prediction_weight=result)
if __name__ == '__main__':
    app.run(debug=True)
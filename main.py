import tensorflow
import keras
import numpy as np
import librosa
#import LivePredictions_CHOPPED as LP
import os
from flask import Flask, flash, request, jsonify, redirect,render_template, Response, url_for
from werkzeug.utils import secure_filename
import numpy as np
import cv2
import re
import base64
import io
import sys
#from flask_cors import CORS, cross_origin
UPLOAD_FOLDER = './'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'wav'])
speech_model = keras.models.load_model('./Emotion_Voice_Detection_Model.h5')
# What if file.wav isn't there or corrupted??? Create some kind of routine or backup wav file 
# to replace a corrupted or missing wav
Speech_Activation_Detection = os.popen('python3 detectVoiceInWave.py ./file.wav ./results.json').read()
SAD_float = float(Speech_Activation_Detection)
data, sampling_rate = librosa.load('./file.wav')
mfccs = np.mean(librosa.feature.mfcc(y=data, sr=sampling_rate, n_mfcc=40).T, axis=0)
x = np.expand_dims(mfccs, axis=2)
x = np.expand_dims(x, axis=0)
pred = str(speech_model.predict_classes(x))
pred_vec = speech_model.predict(x)
pred2 = str(pred_vec[0][3] + pred_vec[0][4]+ pred_vec[0][5]+ pred_vec[0][6])
#Emotion_prediction = str(speech_model.predict(x))
#pred = LP.livePredictions(path='./Emotion_Voice_Detection_Model.h5', file='./file.wav')
#pred.load_model()
#data = str(pred.makepredictions())
app = Flask(__name__)
#CORS(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#app.secret_key = 'super secret key'
#app.config['SESSION_TYPE'] = 'filesystem'


@app.route('/')
def upload_file():
	return render_template('index.html')

@app.route('/messages', methods = ['GET', 'POST'])
def api_message():
	if request.method == 'POST':
		f = open('./file.wav', 'wb')
		f.write(request.data)
		f.close()
	Speech_Activation_Detection = os.popen('python3 detectVoiceInWave.py ./file.wav ./results.json').read()
	SAD_float = float(Speech_Activation_Detection)
	data, sampling_rate = librosa.load('./file.wav')
	mfccs = np.mean(librosa.feature.mfcc(y=data, sr=sampling_rate, n_mfcc=40).T, axis=0)
	x = np.expand_dims(mfccs, axis=2)
	x = np.expand_dims(x, axis=0)
	pred = str(speech_model.predict_classes(x))
	pred_vec = speech_model.predict(x)
	dummy_string = "Total speech negativity score is "
	pred2 = str(pred_vec[0][3] + pred_vec[0][4]+ pred_vec[0][5]+ pred_vec[0][6])
	if SAD_float < .1:
		pred2 = "0"
	
	if pred == "[0]":
		pred = "neutral"
		
	elif pred == "[1]":
		pred = "calm"
		
	elif pred == "[2]":
		pred = "happy"
		
	elif pred == "[3]":
		pred = "sad"
		
	elif pred == "[4]":
		pred = "angry"
		
	elif pred == "[5]":
		pred = "fearful"
		
	elif pred == "[6]":
		pred = "disgust"
		
	elif pred == "[7]":
		pred = "surprised"
		
	
	#Emotion_prediction = str(speech_model.predict(x))
	#pred = LP.livePredictions(path='./Emotion_Voice_Detection_Model.h5', file='./file.wav')
	#pred.load_model()
	#data2 = str(pred.makepredictions())
	#data2 = str(pred.makepredictions())
	#return jsonify(data2)
	#return jsonify(Emotion)
	#return jsonify(pred, dummy_string, pred2)
	return jsonify(pred2)
	#return jsonify(Emotion_prediction)
	#return "dummy"

@app.route('/profile/<username>')
def profile(username):
	return 'username is %s' % username


if __name__ =="__main__":
	app.run(debug=True)


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
	Emotion = os.popen('python3 LivePredictions.py').read()
	#pred = LP.livePredictions(path='./Emotion_Voice_Detection_Model.h5', file='./file.wav')
	#pred.load_model()
	#data = str(pred.makepredictions())
	return jsonify(Emotion)
	#return "dummy"

@app.route('/profile/<username>')
def profile(username):
	return 'username is %s' % username


if __name__ =="__main__":
	app.run(debug=True)


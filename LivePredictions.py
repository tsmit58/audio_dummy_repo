import keras
import numpy as np
import librosa

class livePredictions:

    def __init__(self, path, file):

        self.path = "./Emotion_Voice_Detection_Model.h5"
        self.file = "file.wav"

    def load_model(self):
        '''
        I am here to load you model.

        :param path: path to your h5 model.
        :return: summary of the model with the .summary() function.

        '''
        self.loaded_model = keras.models.load_model(self.path)
        pass
	#return self.loaded_model.summary()

    def makepredictions(self):
        '''
        I am here to process the files and create your features.
        '''
        data, sampling_rate = librosa.load(self.file)
        mfccs = np.mean(librosa.feature.mfcc(y=data, sr=sampling_rate, n_mfcc=40).T, axis=0)
        x = np.expand_dims(mfccs, axis=2)
        x = np.expand_dims(x, axis=0)
        predictions = self.loaded_model.predict_classes(x)
        print( "Prediction is", " ", self.convertclasstoemotion(predictions))

    def convertclasstoemotion(self, pred):
        '''
        I am here to convert the predictions (int) into human readable strings.
        '''
        self.pred  = pred

        if pred == 0:
            pred = "neutral"
            return pred
        elif pred == 1:
            pred = "calm"
            return pred
        elif pred == 2:
            pred = "happy"
            return pred
        elif pred == 3:
            pred = "sad"
            return pred
        elif pred == 4:
            pred = "angry"
            return pred
        elif pred == 5:
            pred = "fearful"
            return pred
        elif pred == 6:
            pred = "disgust"
            return pred
        elif pred == 7:
            pred = "surprised"
            return pred

# Here you can replace path and file with the path of your model and of the file from the RAVDESS dataset you want to use for the prediction,
# Below, I have used a neutral file: the prediction made is neutral.

pred = livePredictions(path='./Emotion_Voice_Detection_Model.h5',
                       file='./file.wav')

pred.load_model()
pred.makepredictions()

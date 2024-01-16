import tensorflow as tf
import numpy as np 

class SpamDetector:
    spam_detector = tf.keras.models.load_model('spamModel/SPAM_DETECTOR')

    def __init__(self):
        return
    
    def __classifyResult(self, result):
        classifications = []

        for element in result:
            if element[0] <= 0.1:
                classifications.append('not-spam')
            elif element[0] <= 0.2:
                classifications.append('maybe-spam')
            else:
                classifications.append('spam')

        return classifications
    
    def predict(self, array):
        if not isinstance(array, list):
            raise TypeError("Must be a list containing strings")
        for item in array:
            if not isinstance(item, str):
                raise TypeError("All entries must be strings")
        
        result = self.spam_detector.predict(array)
        return self.__classifyResult(result)
import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import re
import string
from tensorflow.keras import layers


class Data:

    MAX_FEATURES = 10000
    SEQUENCE_LENGTH = 100
    TRAIN_TEST_SPLIT = 0.75

    vectorize_layer = None

    def __init__(self, max_features=10000, sequence_length=100, ttsplit=0.75):
        self.MAX_FEATURES = max_features
        self.SEQUENCE_LENGTH = sequence_length
    
    def load_data(self):
        texts, labels = [], []
        with open("data/SMSSpamCollection") as f:
            for line in f:
                split = line.split()
                labels.append(split[0].strip())
                texts.append(' '.join(split[1:]).strip())
        return texts, labels

    def __custom_standardization(self, input_data):
      lowercase = tf.strings.lower(input_data)
      stripped_html = tf.strings.regex_replace(lowercase, '<br />', ' ')
      return tf.strings.regex_replace(stripped_html,
                                  '[%s]' % re.escape(string.punctuation),
                                  '')
    
    def __vectorize_text(self, text, label,):
        text = tf.expand_dims(text, -1)
        if(self.vectorize_layer):
            return self.vectorize_layer(text), label
    
    def getData(self):
        x,y = self.load_data()
        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=self.TRAIN_TEST_SPLIT, random_state=412)
        X_train, X_val, y_train, y_val = train_test_split(x, y, test_size=0.1, random_state=102)
        raw_train_dataset = tf.data.Dataset.from_tensor_slices((X_train, y_train))
        raw_test_dataset = tf.data.Dataset.from_tensor_slices((X_test, y_test))
        raw_val_dataset = tf.data.Dataset.from_tensor_slices((X_val, y_val))
        train_text = raw_train_dataset.map(lambda x,y : x)
        self.vectorize_layer = layers.TextVectorization(
            standardize=self.__custom_standardization,
            max_tokens=self.MAX_FEATURES,
            output_mode='int',
            output_sequence_length=self.SEQUENCE_LENGTH)
        train_dataset = raw_train_dataset.map(self.__vectorize_text)
        test_dataset = raw_test_dataset.map(self.__vectorize_text)
        val_dataset = raw_val_dataset.map(self.__vectorize_text)

        return train_dataset, test_dataset, val_dataset
    
    def convertData(self, text):
        text = tf.expand_dims(text, -1)
        if(self.vectorize_layer):
            return self.vectorize_layer(text)
        else:
            self.vectorize_layer = layers.TextVectorization(
                standardize=self.__custom_standardization,
                max_tokens=self.MAX_FEATURES,
                output_mode='int',
                output_sequence_length=self.SEQUENCE_LENGTH
            )
            return self.vectorize_layer(text)
        

myData = Data()
myText = np.array([["The"],["purple"],["cat"],["wants"],["to"],["sell"],["this"],["vaccuum"]])
print(myData.convertData(myText))
        

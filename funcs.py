import json
import random
import pickle
import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer
from keras.models import load_model

intents = json.load(open("intents.json"))
classes = pickle.load(open("classes.pkl", "rb"))
words = pickle.load(open("words.pkl", "rb"))
model = load_model("chatbot_Loki.h5")



def prepare_sentence(sentence):

    ign = ['?','.','!',',']
    lem = WordNetLemmatizer()
    sn_tokens = nltk.word_tokenize(sentence)
    sn_tokens = [lem.lemmatize(word.lower()) for word in sn_tokens if word not in ign]

    return sn_tokens


def words_toarray(tokens):
    bag = []
    for word in words:
        bag.append(1) if word in tokens else bag.append(0)
    
    return np.array(bag)

def class_predictor(snt):
    new_snt = prepare_sentence(snt)
    bag = words_toarray(new_snt)

    result = model.predict(np.array([bag]))

    return classes[np.argmax(result)]


def get_response(snt):
    cl = class_predictor(snt)
    res = []
    for intent in intents["intents"]:
        if cl == intent["tag"]:
            for response in intent["responses"]:
                if response not in res:
                    res.append(response)
    random.shuffle(res)
    return res[0]
            

 
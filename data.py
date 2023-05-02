import json
import random
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer



lematizer = WordNetLemmatizer()

intents = json.loads(open("intents.json").read())

# Extracting words and tags from intents
classes = []
words = []
doc = []
ignore = ["?",".","!","'",","]

for ints in intents["intents"]:
    for ptrn in ints["patterns"]:
        word_in_ptrn = nltk.word_tokenize(ptrn)
        words.extend(word_in_ptrn)

        doc.append((word_in_ptrn, ints["tag"]))

        if ints["tag"] not in classes:
            classes.append(ints["tag"])

words = [lematizer.lemmatize(wrd.lower()) for wrd in words if wrd not in ignore]
words = sorted(list(set(words)))
classes = sorted(classes)

#Storing them as pickles
pickle.dump(words,open("words.pkl","wb"))
pickle.dump(classes,open("classes.pkl","wb"))


#Prepairing the data for training the model

y_empty = [0]*len(classes)
dataset = []

for d in doc:
    bag = []
    word_ptrns = d[0]
    word_ptrns = [lematizer.lemmatize(w.lower()) for w in word_ptrns]

    for wd in words:
        if wd in word_ptrns:
            bag.append(1)
        else:
            bag.append(0)
    
    y = list(y_empty)
    y[classes.index(d[1])] = 1

    dataset.append([bag, y])

random.shuffle(dataset)
dataset = np.array(dataset)

x_train = list(dataset[:,0])
y_train = list(dataset[:,1])


x_train_final = np.array(x_train)
y_train_final = np.array(y_train)


# Moving to jupyter notebook for training and saving the model
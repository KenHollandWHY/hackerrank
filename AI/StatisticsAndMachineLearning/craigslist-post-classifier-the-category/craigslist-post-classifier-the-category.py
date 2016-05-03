import json
#import numpy as np
#from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

_X_train=[]
y_train=[]
with open('training.json','r') as f:
    for index, line in enumerate(f):
        if index == 0:
            continue
        json_obj = json.loads(line)
        _X_train.append(json_obj['heading']+" "+json_obj['section']+" "+json_obj['city'])
        y_train.append(json_obj['category'])

#vectorizer = HashingVectorizer(stop_words='english')
vectorizer = TfidfVectorizer(stop_words='english',ngram_range=(1,3))

X_train = vectorizer.fit_transform(_X_train)

classifier = LinearSVC()
classifier.fit(X_train, y_train)

T = int(raw_input())
_X_test = []
for t in range(T):
    json_obj = json.loads(raw_input())
    _X_test.append(json_obj['heading']+" "+json_obj['section']+" "+json_obj['city'])

y_test = classifier.predict(vectorizer.transform(_X_test))
print("\n".join(y_test))

import json
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import HashingVectorizer

# I got UnicodeDecodeError with python3 on submit

N = 0
topics = [
"gis",
"security",
"photo",
"mathematica",
"unix",
"wordpress",
"scifi",
"electronics",
"android",
"apple"]

_X_train = []
y_train = []

# load training data
with open('training.json') as f:
    for index, line in enumerate(f):
        if(index == 0):
            N = 0
        else:
            json_obj = json.loads(line)
            _X_train.append(json_obj['question']+". "+ json_obj['excerpt'])
            y_train.append(json_obj['topic'])

vectorizer = HashingVectorizer(stop_words='english')
X_train = vectorizer.fit_transform(_X_train)
#print(X_train)

# training
model = LinearSVC()

# Train the model using the training sets
model.fit(X_train, y_train)


# load test data
test_N = int(raw_input().strip())
test_data = []
_X_test = []
for n in range(test_N):
    json_obj = json.loads(raw_input().strip())
    _X_test.append(json_obj['question']+". "+ json_obj['excerpt'])

X_test = vectorizer.fit_transform(_X_test)

# predict
y_predict = model.predict(X_test)

# print the results
for y in y_predict:
    print(y)

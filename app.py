from flask import request, url_for, json, jsonify, Response
from flask_api import FlaskAPI, status, exceptions

#Pandas
import pandas as pd
import numpy as np


#Cv
from sklearn.model_selection import train_test_split

#Import KNN
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics


app = FlaskAPI(__name__)

@app.route("/wake_up/", methods=['GET'])
def wake_up():
    return "Waked up"


@app.route("/predict/", methods=['GET'])
def predict():
    # Create Dataframe from our data.
    headers = ["TABLEU", "C1_AGE", "C1_RANKING", "C1_HANDNESS", "C1_WEAPON", "C2_AGE",
               "C2_RANKING", "C2_HANDNESS", "C2_WEAPON", "WINNER"]

    dataframe = pd.read_csv(r"6_competition_frankings_columns.csv")
    dataframe = pd.read_csv(r"6_competition_frankings_columns.csv", header=1, names=headers)
    dataframe = dataframe.drop(dataframe[dataframe['C2_WEAPON'] == ' None '].index)
    dataframe = dataframe.drop(dataframe[dataframe['C1_WEAPON'] == ' None '].index)
    dataframe.to_csv("testing_csv")


    # Split data from train to test
    X = np.array(dataframe.drop(['WINNER'],1))
    y = np.array(dataframe['WINNER'])
    x1, x2, y1, y2 = train_test_split( X, y, random_state = 100)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=3)

    knn = KNeighborsClassifier(n_neighbors=56, n_jobs=5, leaf_size=29, p=5)

    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    predict = metrics.accuracy_score(y_test, y_pred)

    data = []
    data.append(int(request.data.get('tableu', '')))
    data.append(int(request.data.get('fencer1_age', '')))
    data.append(int(request.data.get('fencer1_ranking', '')))
    data.append(int(request.data.get('fencer1_handness', '')))
    data.append(request.data.get('fencer1_weapon', ''))
    data.append(int(request.data.get('fencer2_age', '')))
    data.append(int(request.data.get('fencer2_ranking', '')))
    data.append(int(request.data.get('fencer2_handness', '')))
    data.append(request.data.get('fencer2_weapon', ''))


    predict = knn.predict_proba([data])
    return str(predict)

@app.route("/me.json", methods=['GET'])
def me():
    token = str(request.args.get('token'))
    if token == 'y38USsxxrszr3E':
        data = {'message': 'correct token'}
        response = 200
    else:
        data = {'message': 'incorrect token'}
        response = 401

    js = json.dumps(data)

    resp = Response(js, status=response, mimetype='application/json')
    return resp

@app.route("/interactive.json",  methods=['POST'])
def interactive():
    data = {
        "type": "modal",
        "title": {
            "type": "plain_text",
            "text": "My App"
        },
        "submit": {
            "type": "plain_text",
            "text": "Submit"
        },
        "close": {
            "type": "plain_text",
            "text": "Cancel",
        },
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "This is a section test"
                }
            },
            {
                "type": "context",
                "elements": [
                    {
                        "type": "mrkdwn",
                        "text": "Last updated: Jan 1, 2019"
                    }
                ]
            }
        ]
    }

    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    return resp

@app.route("/fake_create", methods=['POST'])
def fake_create():
    data = {
        'message': 'this is a message'
    }

    js = json.dumps(data)
    resp = Response(js, status=200, mimetype='application/json')
    return resp

if __name__ == "__main__":
    app.run(debug=False)

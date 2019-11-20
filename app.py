from flask import request, url_for
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


@app.route("/predict/", methods=['GET'])
def test_method():
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
    data.append(int(request.data.get('f1', '')))
    data.append(int(request.data.get('f2', '')))
    data.append(int(request.data.get('f3', '')))
    data.append(int(request.data.get('f4', '')))
    data.append(request.data.get('f5', ''))
    data.append(int(request.data.get('f6', '')))
    data.append(int(request.data.get('f7', '')))
    data.append(int(request.data.get('f8', '')))
    data.append(request.data.get('f9', ''))

    predict = knn.predict_proba([data])
    return str(predict)

if __name__ == "__main__":
    app.run(debug=False)

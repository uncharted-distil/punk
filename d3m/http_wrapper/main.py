from flask import Flask, request
import pandas as pd
import sys
import json
import logging
from punk.feature_selection import PCAFeatures, RFFeatures
from punk.novelty_detection import HeteroscedasticityTest

app = Flask(__name__)

def fixDummyHeaders(headers, dummy_headers, indices):
    results = []
    visited = set()
    for index in indices:
        currHeader = dummy_headers[index]
        fixedIndex = headers[currHeader.split('_')[0]]

        if not fixedIndex in visited:
            results.append(fixedIndex)
            visited.add(fixedIndex)
    return results

@app.route("/pca", methods=['POST'])
def predictPCAFeatures():
    frame = pd.read_csv(request.files.get('file'))
    headerNumStrings = { frame.columns.values[i]: i for i in range(len(frame.columns.values))}
    dummies = pd.get_dummies(frame)
    pca = PCAFeatures()
    results = pca.produce(dummies).tolist()
    return json.dumps(fixDummyHeaders(headerNumStrings, dummies.columns.values, results))

@app.route("/rf", methods=['POST'])
def predictRFFeatures():
    frame = pd.read_csv(request.files.get('file'))
    try:
        targetName = request.form.get('target')
        target = frame[targetName]
        del frame[targetName]
    except:
        return {
            "error": "Target column not found in file. Please include a parameter 'target' in the body of the request that contains the name of the target header"
        }
    rf = RFFeatures()
    headerNumStrings = { frame.columns.values[i]: i for i in range(len(frame.columns.values))}
    dummyTrain = pd.get_dummies(frame)
    results = rf.produce((dummyTrain, pd.get_dummies(target))).tolist()
    return json.dumps(fixDummyHeaders(headerNumStrings, dummyTrain.columns.values, results))

@app.route("/hetero", methods=['POST'])
def predictHetero():
    frame = pd.read_csv(request.files.get('file'))
    hetero = HeteroscedasticityTest()
    return json.dumps(hetero.produce(frame))
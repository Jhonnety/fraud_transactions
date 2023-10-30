import joblib

model = joblib.load('model.pkl')

def isFraud(x):
    return model.predict([x])


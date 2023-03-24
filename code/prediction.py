import pickle
def predict(data):
    rf = pickle.load(open(r'..\model\model_v1.pkl','rb'))
    return rf.predict(data)
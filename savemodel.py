import pickle

with open('model.pkl','wb') as f:
    pickle.dump(model,f)
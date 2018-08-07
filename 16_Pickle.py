import pickle
data = {
    'a' : [1,2.0,3,4+6],
    'b' : ("character string", b"byte string"),
    'c' : {None, True, False}
}
#save
with open('data.pickle', 'wb') as f:
    pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

#road
with open('data.pickle', 'rb') as f:
    data = pickle.load(f)
    print(data)
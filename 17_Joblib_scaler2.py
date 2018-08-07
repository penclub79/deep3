from sklearn import datasets
from sklearn.externals import joblib
import pickle

iris = datasets.load_iris()
X=iris.data
y=iris.target
from sklearn.model_selection import train_test_split
train_X, test_X, train_Y, test_Y = train_test_split(X, y, test_size=0.3, random_state=0)

pickle.dump(train_X, open('train_X.pkl', 'rb'))
pickle.dump(test_X, open('test_X.pkl', 'rb'))
pickle.dump(train_Y, open('train_Y.pkl', 'rb'))
pickle.dump(test_Y, open('test_Y.pkl', 'rb'))
#train , test로 잘라서 저장한거 road 하기

file_name = 'scaler_01.pkl'
scaler = joblib.load(file_name)
train_x_scaled = scaler.transform(train_X)
print(train_x_scaled[:5])

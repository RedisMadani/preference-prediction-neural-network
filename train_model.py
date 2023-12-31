import pandas as pd
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import StratifiedKFold
from sklearn.utils import resample
import datetime as dt
import numpy
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop

# Reading a tab-delimited file
data = pd.read_csv('data.txt', sep='\t')
data.head()

# Checking for any missing values
data.isnull().sum()
data.info()

# Converting the date feature to an ordinal i.e. an integer
# representing the number of days since year 1 day 1
data['F15'] = pd.to_datetime(data['F15'])
data['F15'] = data['F15'].map(dt.datetime.toordinal)

data['F16'] = pd.to_datetime(data['F16'])
data['F16'] = data['F16'].map(dt.datetime.toordinal)

# Upsampling to make the observations from both classes equal
df_majority = data[data.C == 0]
df_minority = data[data.C == 1]

df_minority_upsampled = resample(df_minority, replace=True, n_samples=76353, random_state=123)
df_upsampled = pd.concat([df_majority, df_minority_upsampled])
df_upsampled.C.value_counts()

df_upsampled.drop(['Index'], axis=1, inplace=True)
df_upsampled.head()

# Separating input features (X) and target variable (y)
X = df_upsampled.iloc[:, :22].values
y = df_upsampled.iloc[:, 22].values

# Standardize features by removing the mean and scaling to unit variance from the entire dataset
scaler = preprocessing.StandardScaler().fit(X)
X = scaler.transform(X)

# Splitting the 20% portion of the dataset into a validation set to evaluate the performance of the model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=20)

# Defining NN Model
model = Sequential()
model.add(Dense(1024, input_dim=22, activation='relu'))
model.add(Dropout(0.05))
model.add(Dense(1024, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer=RMSprop(), metrics=['accuracy'])

# Training the model
model.fit(X_train, y_train, epochs=20, batch_size=512, validation_data=(X_test, y_test), shuffle=True, verbose=2)

# Saving the model
model.save('my_model1.h5')

# Classification Report and Confusion matrix
y_pred = model.predict_classes(X_test)
confusion_matrix = confusion_matrix(y_test, y_pred)
print(confusion_matrix)
print(classification_report(y_test, y_pred))

# k-Fold Cross Validation
seed = 7
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
cvscores = []
for train, test in kfold.split(X, y):
    model = Sequential()
    model.add(Dense(1024, input_dim=22, activation='relu'))
    model.add(Dropout(0.05))
    model.add(Dense(1024, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy', optimizer=RMSprop(), metrics=['accuracy'])
    model.fit(X[train], y[train], epochs=20, batch_size=512, verbose=0)
    scores = model.evaluate(X[test], y[test], verbose=0)
    print("%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))
    cvscores.append(scores[1] * 100)

print("%.2f%% (+/- %.2f%%)" % (numpy.mean(cvscores), numpy.std(cvscores)))

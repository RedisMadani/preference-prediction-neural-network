import pandas as pd
from sklearn import preprocessing
import numpy as np
import datetime as dt
from keras.models import load_model

# Reading test data from a tab-delimited file
test_data = pd.read_csv('test.txt', sep='\t')
test_data.head()

# Checking for any missing values
test_data.isnull().sum()
test_data.info()

# Converting the date features to ordinals
test_data['F15'] = pd.to_datetime(test_data['F15'])
test_data['F15'] = test_data['F15'].map(dt.datetime.toordinal)

test_data['F16'] = pd.to_datetime(test_data['F16'])
test_data['F16'] = test_data['F16'].map(dt.datetime.toordinal)

# Extracting the index column and reshaping it
index = test_data.iloc[:, 0].values
index = index.reshape(len(index), 1)

# Dropping the index column from the DataFrame
test_data.drop(['Index'], axis=1, inplace=True)
test_data.head()

# Standardizing the test data using the scaler fitted on training data
test_data_ = test_data.iloc[:, :].values
scaler = preprocessing.StandardScaler().fit(test_data_)
test_data = scaler.transform(test_data_)

# Loading the trained model
model = load_model('my_model1.h5')

# Predicting the target variable for the test data
test_target_pred = model.predict_classes(test_data_)

# Concatenating the index column with the predicted target variable
conct = np.concatenate((index, test_target_pred), axis=1)

# Saving the predictions to a text file
np.savetxt('prediction.txt', conct, fmt='%5s', header='Index       C', delimiter=' ')

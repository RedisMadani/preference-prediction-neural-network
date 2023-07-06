# Predictive Neural Network

This project is focused on developing a neural network model that can predict the likelihood of an individual (X) purchasing a specific product (Y). By leveraging demographic and past activity data as input features, the model aims to classify whether a person will buy the product or not.

## Problem Statement

The problem at hand involves predicting the probability of an individual (X) buying a particular product (Y). The dataset available for analysis contains a comprehensive set of demographic-related features and information about the individual's previous activities. Furthermore, aggregated data pertaining to individuals who typically make purchases of the product (Y) are included as well. The variable "C" indicates whether person X has actually purchased the product Y. The task is to create a program/script that takes a tab-delimited file with these 22 features as input and generates an output file containing the index and predicted value (1 or 0).

### File Descriptions

- `data.txt`: This file contains the training data samples, arranged in a tab-delimited format. Each sample consists of 22 features, along with the target variable "C" denoting whether the person actually bought the product (Y).
- `my_model1.h5`: This file stores the pre-trained neural network model, which was trained using the provided training data.
- `prediction.txt`: After executing the `test.py` script, this file will be generated. It contains the index and predicted values (1 or 0) for each sample in the provided test dataset.
- `test.py`: This script is responsible for making predictions using the pre-trained model. By supplying a test dataset (in tab-delimited format) as input, the script generates an output file (`prediction.txt`) containing the predicted values for each sample.
- `test.txt`: A separate test dataset file is expected to be provided in order to use the `test.py` script and obtain predictions.
- `train_model.py`: Use this script to train the neural network model with the training data available in `data.txt`.
- `visualize.py`: If applicable, this script can be utilized to visualize the architecture or results of the neural network model.

## Usage

To utilize this project effectively, follow these steps:

1. Ensure that the necessary dependencies (such as Python and TensorFlow) are installed.
2. Place your training data into the `data.txt` file, ensuring that each sample includes 22 features and the target variable "C".
3. Execute the `train_model.py` script to train the neural network model using the provided training data.
4. Upon completion of the training process, you can make use of the pre-trained model by loading it through the `my_model1.h5` file in your own scripts.
5. Utilize the `test.py` script to obtain predictions for each sample by providing a separate test dataset (tab-delimited format) named `Classification1Test.txt`.
6. Once the script has run, you will find an output file named `prediction.txt`, which contains the index and predicted values (1 or 0) for each sample in the test dataset.

## Screenshots

![customer_neural](https://github.com/RedisMadani/preference-prediction-neural-network/assets/136177376/8d4a24ad-69f9-4b1e-96e1-8566252ee38f)

## Data Source

The raw data files (data.txt and test.txt) used for training and testing the predictive neural network model was obtained from sources publicly available on GitHub. 

from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponse
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers.core import Dense,Activation,Dropout
from keras.callbacks import EarlyStopping
from sklearn.preprocessing import OneHotEncoder
from keras.optimizers import Adam
import os
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import load_model
from django.shortcuts import render
global model

def index(request):
    if request.method == 'GET':
       return render(request, 'index.html', {})

def User(request):
    if request.method == 'GET':
       return render(request, 'User.html', {})


def Admin(request):
    if request.method == 'GET':
       return render(request, 'Admin.html', {})

def AdminLogin(request):
    if request.method == 'POST':
      username = request.POST.get('username', False)
      password = request.POST.get('password', False)
      if username == 'admin' and password == 'admin':
       context= {'data':'welcome '+username}
       return render(request, 'AdminScreen.html', context)
      else:
       context= {'data':'login failed'}
       return render(request, 'Admin.html', context)


def importdata(): 
    balance_data = pd.read_csv('C:/FakeProfile/Profile/dataset/dataset.txt')
    balance_data = balance_data.abs()
    rows = balance_data.shape[0]  # gives number of row count
    cols = balance_data.shape[1]  # gives number of col count
    return balance_data 

def splitdataset(balance_data):
    X = balance_data.values[:, 0:8] 
    y_= balance_data.values[:, 8]
    y_ = y_.reshape(-1, 1)
    encoder = OneHotEncoder(sparse=False)
    Y = encoder.fit_transform(y_)
    print(Y)
    train_x, test_x, train_y, test_y = train_test_split(X, Y, test_size=0.2)
    return train_x, test_x, train_y, test_y

# def UserCheck(request):
#     if request.method == 'POST':
#       data = request.POST.get('t1', False)
#       input = 'Account_Age,Gender,User_Age,Link_Desc,Status_Count,Friend_Count,Location,Location_IP\n';
#       input+=data+"\n"
#       f = open("C:/FakeProfile/Profile/dataset/test.txt", "w")
#       f.write(input)
#       f.close()
#       test = pd.read_csv('C:/FakeProfile/Profile/dataset/test.txt')
#       test = test.values[:, 0:8]
#       global graph
#       with graph.as_default():
#         model = load_model('C:/FakeProfile/Profile/dataset/model.h5')
#         predict = model.predict_classes(test)
#         print(predict[0])
#         msg = ''
#         if str(predict[0]) == '0':
#            msg = "Given Account Details Predicted As Genuine"
#         if str(predict[0]) == '1':
#            msg = "Given Account Details Predicted As Fake"
#         context= {'data':msg}
#         return render(request, 'User.html', context)


def UserCheck(request):
    if request.method == 'POST':
        data = request.POST.get('t1', False)
        input_data = "Account_Age,Gender,User_Age,Link_Desc,Status_Count,Friend_Count,Location,Location_IP\n"
        input_data += data + "\n"

        # Save input data to file
        file_path = "C:/FakeProfile/Profile/dataset/test.txt"
        with open(file_path, "w") as f:
            f.write(input_data)

        # Load and preprocess test data
        test = pd.read_csv(file_path)
        test = test.values[:, 0:8]  # Extract feature columns

        # Load the trained model
        model_path = "C:/FakeProfile/Profile/dataset/model.h5"
        if not os.path.exists(model_path):
            return render(request, 'User.html', {'data': "Model file not found!"})

        model = load_model(model_path, compile=False)  # Load model without compilation

        # Make predictions
        predictions = np.argmax(model.predict(test), axis=-1)  # Get class labels
        prediction_label = predictions[0]

        # Determine output message
        msg = "Given Account Details Predicted As Genuine" if prediction_label == 0 else "Given Account Details Predicted As Fake"

        return render(request, 'User.html', {'data': msg})

def GenerateModel(request):
    global model
    data = importdata()
    train_x, test_x, train_y, test_y = splitdataset(data)
    model = Sequential()
    model.add(Dense(200, input_shape=(8,), activation='relu', name='fc1'))
    model.add(Dense(200, activation='relu', name='fc2'))
    model.add(Dense(2, activation='softmax', name='output'))
    optimizer = Adam(lr=0.001)
    model.compile(optimizer, loss='categorical_crossentropy', metrics=['accuracy'])
    print('CNN Neural Network Model Summary: ')
    print(model.summary())
    model.fit(train_x, train_y, verbose=2, batch_size=5, epochs=200)
    results = model.evaluate(test_x, test_y)
    ann_acc = results[1] * 100
    model_save_path = "C:/FakeProfile/Profile/dataset/model.h5"
    os.makedirs(os.path.dirname(model_save_path), exist_ok=True)
    model.save(model_save_path)
    context= {'data':'ANN Accuracy : '+str(ann_acc)}
    return render(request, 'AdminScreen.html', context)

def ViewTrain(request):
    if request.method == 'GET':
       strdata = '<table border=1 align=center width=100%><tr><th><font size=4 color=white>Account Age</th><th><font size=4 color=white>Gender</th><th><font size=4 color=white>User Age</th><th><font size=4 color=white>Link Description</th> <th><font size=4 color=white>Status Count</th><th><font size=4 color=white>Friend Count</th><th><font size=4 color=white>Location</th><th><font size=4 color=white>Location IP</th><th><font size=4 color=white>Profile Status</th></tr><tr>'
       data = pd.read_csv('C:/FakeProfile/Profile/dataset/dataset.txt')
       rows = data.shape[0]  # gives number of row count
       cols = data.shape[1]  # gives number of col count
       for i in range(rows):
          for j in range(cols):
             strdata+='<td><font size=3 color=white>'+str(data.iloc[i,j])+'</font></td>'
          strdata+='</tr><tr>'
       context= {'data':strdata}
       return render(request, 'ViewData.html', context)
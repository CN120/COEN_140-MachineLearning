import numpy as np
import matplotlib
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis

def test_dataset(data):
    if len(data) != 150:
        return False

    for row in data:
        if len(row) != 5:
            return False

        for column in row[:-1]:
            if type(column) != np.float64:
                return False
           
        if type(row[-1]) != str:
            return False

    return True

def readFileFunction():
    f=open("iris.csv", "r")
    contents = f.readlines()
    for i in range(len(contents)):
        contents[i] = contents[i][:-1]
        contents[i] = contents[i].split(',')
        for j in range(len(contents[i])-1):
            contents[i][j] = np.float64(contents[i][j])

    return contents

def problem1():
    input_list = readFileFunction()
    print(test_dataset(input_list))
    ret_list = np.array(input_list)


    return ret_list

problem1()


def problem2():
    data =  readFileFunction()
    features = []
    labels = []
    for row in data:
        features.append(row[:-1])
        labels.append(row[-1])



    training_set1 = np.array(features[0:40]+features[50:90]+features[100:140])
    testing_set1 = np.array(features[40:50]+features[90:100]+features[140:150])
    labels_1 = np.array(labels[0:40]+labels[50:90]+labels[100:140])
    correct_labs_1 = np.array(labels[40:50]+labels[90:100]+labels[140:150])

    print(training_set1.shape)
    print(testing_set1.shape)
    print(labels_1.shape)


    lda = LinearDiscriminantAnalysis(solver="svd", store_covariance=True)
    lda.fit(training_set1, labels_1)
    score1_1 = lda.score(training_set1, correct_labs_1)
    score1_2 = lda.score(testing_set1, correct_labs_1)
    print(score1_1,score1_2)

problem2()
# training_set1 = np.empty(shape=(40,4), dtype=np.float64)

# for i in range(40):
#     training_set1[i][0] = np.float64(np_list[i][0])
#     training_set1[i][0] = np.float64(np_list[i][0])

# training_set1 = np_list[0:40]
# testing_set1 = np_list[40:50]

# training_set2 = np_list[50:90]
# testing_set2 = np_list[90:100]

# training_set3 = np_list[100:140]
# testing_set3 = np_list[140:150]

# training_set1.shape(40,5)
# testing_set1.shape(10,5)


# testing_set1[0]
# lda = LinearDiscriminantAnalysis(solver="svd", store_covariance=True)
# y_pred = lda.fit(X, y)
# #.predict(X)

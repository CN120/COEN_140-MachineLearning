import numpy as np

testing_data = None
training_data = None

def readFileFunction():
    f=open("../iris.csv", "r")
    contents = f.readlines()
    for i in range(len(contents)):
        contents[i] = contents[i][:-1]
        contents[i] = contents[i].split(',')
        for j in range(len(contents[i])-1):
            contents[i][j] = np.float64(contents[i][j])       
    return contents

def Problem1():
    global training_data, testing_data
    ret_list = readFileFunction()
    training_data = np.array(ret_list[0:40]+ret_list[50:90]+ret_list[100:140])
    testing_data = np.array(ret_list[40:50]+ret_list[90:100]+ret_list[140:150])
    SolveForMu(40,4,training_data[0:40])


def SolveForMu(N, num_feat, class_data):
    mu = np.array([0,0,0,0])
    for i in range(N):
        for j in range(num_feat):
            mu[j] += class_data[i][j]   #adds each row of feature data to final mu vector
    for k in range(num_feat):
        mu[k] = mu[k]/N 
    return mu

Problem1()

def readFunction():
    f=open("students.csv", "r")
    contents = f.readlines()
    for i in range(len(contents)):
        contents[i] = contents[i][:-1]
        contents[i] = contents[i].split(',')
    return contents

def secondElmt(elmts):
    return elmts[1]

students = readFunction()
students.sort(key=secondElmt)
print(students)

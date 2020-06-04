import random

from student import Student


def findCourceIndex(array, student):
    for i in range(len(array)):
        if array[i][0].cource == student.cource:
            return i
    return -1


coursesWithStudents = []
allStudents = []
f = open("Test input/1.txt", "r")
f1 = f.readlines()
for x in f1:
    line = x.split()
    stud = Student(line[0], int(line[1]), line[2], int(line[3]))
    allStudents.append(stud)
    if findCourceIndex(coursesWithStudents, stud) == -1:
        coursesWithStudents.append([stud])
    else:
        coursesWithStudents[findCourceIndex(coursesWithStudents, stud)].append(stud)


def compUtil(s):
    return s.avg


def main():
    output = ""
    for cource in coursesWithStudents:
        cource.sort(key=compUtil)



    f = open("Output/1.txt", "w+")
    f.write(output)
    print(output)


main()

import random

from student import Student


def findCourceIndex(array, student):
    for i in range(len(array)):
        if array[i][0].cource == student.cource:
            return i
    return -1


coursesWithStudents = []
f = open("Test input/1.txt", "r")
f1 = f.readlines()
for x in f1:
    line = x.split()
    stud = Student(line[0], int(line[1]), line[2], int(line[3]))
    if findCourceIndex(coursesWithStudents, stud) == -1:
        coursesWithStudents.append([stud])
    else:
        coursesWithStudents[findCourceIndex(coursesWithStudents, stud)].append(stud)


def main():
    output = ""
    for cource in coursesWithStudents:
        bestMales = [Student("", "", "male", 0)]
        bestFemales = [Student("", "", "female", 0)]
        for stud in cource:
            if stud.sex == "male":
                if stud.avg > bestMales[0].avg:
                    bestMales.clear()
                    bestMales.append(stud)
                elif stud.avg == bestMales[0].avg:
                    bestMales.append(stud)
            if stud.sex == "female":
                if stud.avg > bestFemales[0].avg:
                    bestFemales.clear()
                    bestFemales.append(stud)
                elif stud.avg == bestFemales[0].avg:
                    bestFemales.append(stud)
        if bestMales[0].avg > 0 and bestFemales[0].avg > 0:
            output = output + "Курс: " + str(cource[0].cource) + " " + random.choice(bestFemales).name + " " + random.choice(
                bestMales).name + "\n"

    f = open("Output/1.txt", "w+")
    f.write(output)
    print(output)


main()

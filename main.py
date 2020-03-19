from section import Section

sections = []
f = open("Test input/2.txt", "r")
f1 = f.readlines()
for x in f1:
    line = x.split()
    sections.append(Section(int(line[0]), int(line[1])))


def isOverlap(s):
    for sec1 in s:
        for sec2 in s:
            if not (sec2 is sec1):
                for sec3 in s:
                    if not (sec3 is sec2 or sec3 is sec1):
                        if (sec2.x1 <= sec1.x1 <= sec2.x2) or (sec2.x1 >= sec1.x2 >= sec2.x2):
                            return 1
                        if (sec2.x1 <= sec1.x2 <= sec2.x2) or (sec2.x1 >= sec1.x1 >= sec2.x2):
                            return 1
                        if (sec2.x1 <= sec3.x1 <= sec2.x2) or (sec2.x1 >= sec3.x2 >= sec2.x2):
                            return 1
                        if (sec2.x1 <= sec3.x2 <= sec2.x2) or (sec2.x1 >= sec3.x1 >= sec2.x2):
                            return 1
                        if (sec3.x1 <= sec1.x1 <= sec3.x2) or (sec3.x1 >= sec1.x2 >= sec3.x2):
                            return 1
                        if (sec3.x1 <= sec1.x2 <= sec3.x2) or (sec3.x1 >= sec1.x1 >= sec3.x2):
                            return 1
    return 0


def lengthOfThree(s1, s2, s3):
    return s1.len() + s2.len() + s3.len()


def main():
    maxLength = 0
    indexes = []
    i1 = 0
    j1 = 0
    k1 = 0
    for i in sections:
        i1 += 1
        for j in sections:
            j1 += 1
            if not (j is i):
                for k in sections:
                    k1 += 1
                    if not (k is j or k is i):
                        if not isOverlap([i, j, k]) and lengthOfThree(i, j, k) > maxLength:
                            maxLength = lengthOfThree(i, j, k)
                            indexes = [i1, j1, k1]
                            f = open("Output/1.txt", "w+")
                            f.write("First " + str(i1))
                            f.write(" Second " + str(j1))
                            f.write(" Third " + str(k1))
                k1 = 0
        j1 = 0
    print(maxLength)
    print(indexes)


main()

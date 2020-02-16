from section import Section

sections = []
f = open("Test input/1.txt", "r")
f1 = f.readlines()
for x in f1:
    line = x.split()
    sections.append(Section(int(line[0]), int(line[1])))


def isOverlap(s1, s2, s3):
    # TODO fancy intersection check
    return 0


def lengthOfThree(s1, s2, s3):
    return s1.len() + s2.len() + s3.len()


def main():
    maxLength = 0
    for i in sections:
        for j in sections:
            for k in sections:
                if not isOverlap(i, j, k) and lengthOfThree(i, j, k) > maxLength:
                    maxLength = lengthOfThree(i, j, k)
    print(maxLength)


main()

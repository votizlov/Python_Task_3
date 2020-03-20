from device import Device

devices = []
f = open("Test input/1.txt", "r")
f1 = f.readlines()
for x in f1:
    line = x.split()
    devices.append(Device(line[0], int(line[1]), int(line[2]), int(line[3])))


def main():
    names = []
    k = int(input("How many devices?"))
    m = int(input("Min memory"))
    r = int(input("Min rating"))
    priceOfAll = 0
    probableDevices = []
    for d in devices:
        if d.rate >= r and d.memo >= m:
            probableDevices.append(d)
    if not probableDevices.__len__() < k:
        for i in range(k):
            currentD = probableDevices[0]
            for d in probableDevices:
                if d.price < currentD.price:
                    currentD = d
            names.append(currentD.name)
            priceOfAll += currentD.price
            probableDevices.remove(currentD)

    f = open("Output/1.txt", "w+")
    f.write(" Price " + str(priceOfAll) + " ")
    for name in names:
        f.write(str(name) + ", ")
    print(priceOfAll)
    print(names)


main()

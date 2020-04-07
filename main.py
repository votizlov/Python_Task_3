from device import Device

devices = []
f = open("Test input/1.txt", "r")
f1 = f.readlines()
for x in f1:
    line = x.split()
    devices.append(Device(line[0], int(line[1]), int(line[2]), int(line[3])))

def writeOutput(list):
    f = open("Output/1.txt", "w+")
    f.write(" Price " + str(list[0].price) + " ")
    for name in list:
        f.write(str(name.name) + ", ")
    print(list[0].price)
    print(list[0].name)

def main():
    names = []
    k = int(input("How much money?"))
    priceOfAll = 0
    probableDevices = []
    t = devices[0].memo
    for d in devices:
        if d.price <= k:
            if d.memo == t:
                probableDevices.append(d)
            elif d.memo > t:
                probableDevices.clear()
                probableDevices.append(d)
    if probableDevices.__len__() == 1:
        writeOutput(probableDevices)
        return
    t = probableDevices[0].rate
    probableDevices1 = []
    for d in probableDevices:
        if d.rate == k:
            probableDevices1.append(d)
        elif d.rate > k:
            probableDevices1.clear()
            probableDevices1.append(d)
    if probableDevices1.__len__() == 1:
        writeOutput(probableDevices1)
        return
    probableDevices.clear()
    for d in probableDevices1:
        if d.name == "samsung" or d.name == "asus":
            probableDevices.append(d)
    if probableDevices.__len__() == 1:
        writeOutput(probableDevices)
        return
    else:
        writeOutput(probableDevices)
        return


main()

from device import Device

devices = []
f = open("Test input/1.txt", "r")
f1 = f.readlines()
for x in f1:
    line = x.split()
    devices.append(Device(line[0], int(line[1]), int(line[2]), int(line[3])))


def main():
    names = []
    k = input("How many devices?")
    m = input("Min memory")
    r = input("Min rating")
    price = 0
    priceOfAll = 0
    for i in range(int(k)):
        price = devices[0].price
        currentD = devices[0]
        for d in devices:
            if d.price < price and d.rate >= r and d.memo >= m:
                currentD = d
        names.append(currentD.name)
        priceOfAll += price
        devices.remove(currentD)

    f = open("Output/1.txt", "w+")
    f.write(" Price " + str(priceOfAll))
    for name in names:
        f.write(str(name))
    print(price)
    print(names)


main()

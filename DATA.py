import sys

argv = list(map(int, sys.argv[1:]))
tank = argv[0]
full = tank
destination = argv[1]
stations = argv[2:]
count = 0

if(destination > tank):
    print("impossible")
else:
    tank = tank - destination
    for station in stations:
        if(tank >= station):
            tank = full
            count = count + 1

        else:
            print("impossible")

            sys.exit()

print(count)

import sys

def get_resource_values_from_file(file):
    res = []
    time = []
    for line in open(file):
        l = line.rstrip("\n")
        l = l.split()
        res.append(float(l[0]))
        time.append(float(l[1]))
    return res, time

def main():
    try:
        resource_l, time_l = get_resource_values_from_file(sys.argv[1])
        result_l = list()
        for i in range(1, len(resource_l)):
            dr = resource_l[i] - resource_l[i - 1]
            dt = time_l[i] - time_l[i - 1]
            result_l.append(dr / dt)
        print("Average income per second: {0:.2f}".format(sum(result_l) / len(result_l)))
    except:
        print("Something is fucked up!")

if __name__ == '__main__':
    main()

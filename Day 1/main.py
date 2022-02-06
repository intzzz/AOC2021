def main():
    print(task1(read_input("input.txt")))
    print(task2(read_input("input.txt")))


def task2(input_list):
    measurements_of_three = []
    for x in range(len(input_list)):
        if x + 2 >= len(input_list):
            continue
        else:
            measurements_of_three.append(input_list[x] + input_list[x + 1] + input_list[x + 2])

    return task1(measurements_of_three)


def task1(input_list):
    increased_measurements = 0
    for x in range(len(input_list)):
        if x == 0:
            continue
        else:
            if input_list[x] > input_list[x - 1]:
                increased_measurements += 1
    return increased_measurements


def read_input(file_name):
    f = open(file_name, 'r')
    return [int(x) for x in f.read().split()]


if __name__ == "__main__":
    main()

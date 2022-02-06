def main():
    print(task1(read_input("input.txt")))
    print(task2(read_input("input.txt")))


def task2(input_list):
    forward = 0
    aim = 0
    depth = 0

    for x in input_list:
        command = x.split(' ')
        units = int(command[1])
        if command[0] == "forward":
            forward += units
            depth += aim * units
        elif command[0] == "up":
            aim -= units
        elif command[0] == "down":
            aim += units
        else:
            "ERROR"
            exit()
    return forward * depth


def task1(input_list):
    forward = 0
    depth = 0
    for x in input_list:
        command = x.split(' ')
        units = int(command[1])
        if command[0] == "forward":
            forward += units
        elif command[0] == "up":
            depth -= units
        elif command[0] == "down":
            depth += units
        else:
            "ERROR"
            exit()
    return depth * forward


def read_input(file_name):
    f = open(file_name, 'r')
    return [str(x) for x in f.read().split('\n')]


if __name__ == "__main__":
    main()

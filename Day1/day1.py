from ReadDataFile import read_data

datalines = read_data("Day1/input_day1.txt")

list_of_elves = []


def part1():
    count = 0
    sum = 0
    id = 1
    max = 0
    max_index = -1
    for line in datalines:
        elf = {
            'id': 0,
            'calories': 0,
            'nr_of_items': 0
        }
        if line == "":
            elf = {
                'id': id,
                'calories': sum,
                'nr_of_items': count,
            }
            if sum > max:
                max = sum
                max_index = id
            count = 0
            sum = 0
            list_of_elves.append(elf)
            id += 1
        else:
            count += 1
            sum += int(line)


def part2():
    # To return a new list, use the sorted() built-in function...
    newlist = sorted(list_of_elves, key=lambda x: x['calories'], reverse=True)

    print(newlist[0]['calories'] + newlist[1]['calories'] + newlist[2]['calories'])

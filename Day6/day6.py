from ReadDataFile import read_data
from Day6.msg_decoder import Decoder

data = read_data("Day6/input_day6.txt")


def part1():
    data2 = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
    msg = Decoder(data[0])
    print(msg.marker)


def part2():
    data2 = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    msg = Decoder(data[0])
    print(msg.marker)

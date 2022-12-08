from MyMods.ReadDataFile import read_data

datalines = read_data("Day2/input_day2.txt")

datalines2 = """A Y
B X
C Z"""


def part1():
    scores = {
        'A': 1,
        'B': 2,
        'C': 3,
        'X': 1,
        'Y': 2,
        'Z': 3,
        'L': 0,
        'D': 3,
        'W': 6
    }
    score = 0
    # lines = datalines.split("\n")
    for line in datalines:
        round_score = line.split(" ")
        score += scores[round_score[1]]
        if round_score[0] == 'A':
            if round_score[1] == 'X':
                score += scores['D']
            elif round_score[1] == 'Y':
                score += scores['W']
            else:
                score += scores['L']
        elif round_score[0] == 'B':
            if round_score[1] == 'X':
                score += scores['L']
            elif round_score[1] == 'Y':
                score += scores['D']
            else:
                score += scores['W']
        elif round_score[0] == 'C':
            if round_score[1] == 'X':
                score += scores['W']
            elif round_score[1] == 'Y':
                score += scores['L']
            else:
                score += scores['D']
    print(score)


def part2():
    scores = {
        'A': 1,
        'B': 2,
        'C': 3,
        'X': 0,
        'Y': 3,
        'Z': 6,
    }
    score = 0
    # lines = datalines2.split("\n")
    for line in datalines:
        round_score = line.split(" ")
        if round_score[0] == 'A':
            if round_score[1] == 'X':
                score += scores['C'] + scores['X']
            elif round_score[1] == 'Y':
                score += scores['A'] + scores['Y']
            else:
                score += scores['B'] + scores['Z']
        elif round_score[0] == 'B':
            if round_score[1] == 'X':
                score += scores['A'] + scores['X']
            elif round_score[1] == 'Y':
                score += scores['B'] + scores['Y']
            else:
                score += scores['C'] + scores['Z']
        elif round_score[0] == 'C':
            if round_score[1] == 'X':
                score += scores['B'] + scores['X']
            elif round_score[1] == 'Y':
                score += scores['C'] + scores['Y']
            else:
                score += scores['A'] + scores['Z']
        print("score this round : ", score)
    print(score)

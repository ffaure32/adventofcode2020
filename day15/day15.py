def solution2(input):
    return solution_real(input, 30000000)

def solution(input):
    return solution_real(input, 2020)

def solution_real(input, turns):
    last_index = dict()
    spoken_numbers = list()
    for i in range(len(input)):
        spoken_numbers.append(input[i])
        last_index[input[i]] = list()
        last_index[input[i]].append(i)

    for i in range(len(input),turns):
        spoken_number = spoken_numbers[i-1]
        next_spread = 0
        if spoken_number in last_index:
            last_times_spoken = last_index[spoken_number]
            if len(last_times_spoken)>1:
                next_spread = last_times_spoken[-1]-last_times_spoken[-2]
        if next_spread not in last_index:
            last_index[next_spread] = list()
        last_index[next_spread].append(i)
        spoken_numbers.append(next_spread)
    return spoken_numbers[-1]
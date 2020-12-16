def solution2(input):
    return solution_real(input, 30000000)

def solution(input):
    return solution_real(input, 2020)

def solution_real(input, turns):
    last_index = dict()
    for i in range(len(input)):
        last_index[input[i]] = list()
        last_index[input[i]].append(i)
    last_spoken = input[len(input)-1]

    for i in range(len(input),turns):
        next_spread = 0
        if last_spoken in last_index:
            last_times_spoken = last_index[last_spoken]
            if len(last_times_spoken)>1:
                next_spread = last_times_spoken[-1]-last_times_spoken[-2]
        if next_spread not in last_index:
            last_index[next_spread] = list()
        last_index[next_spread].append(i)
        last_spoken = next_spread
    return last_spoken
from utils import file_utils


def no_winner(player1, player2):
    return len(player1) > 0 and len(player2) > 0


def prepare_data(file_name):
    lines = file_utils.get_lines(file_name)
    player1 = [int(card) for card in lines[0].split(',')]
    player2 = [int(card) for card in lines[1].split(',')]
    return player1, player2


def play_game(player1, player2):
    while no_winner(player1, player2):
        play_round(player1, player2)
    if len(player1) > 0:
        return player1
    else:
        return player2


def play_round(player1, player2):
    next1 = player1.pop(0)
    next2 = player2.pop(0)
    if next1 > next2:
        player1.append(next1)
        player1.append(next2)
    else:
        player2.append(next2)
        player2.append(next1)


def play_recursive_round(player1_copy, player2_copy):
    winner = play_recursive_game(player1_copy, player2_copy)
    if winner == player1_copy:
        return 1
    else:
        return 2


def play_second_round(player1, player2):
    if len(player1)-1 >= player1[0] and len(player2)-1 >= player2[0]:
        next1 = player1.pop(0)
        next2 = player2.pop(0)
        winner = play_recursive_round(player1[:next1], player2[:next2])
        if winner == 1:
            player1.append(next1)
            player1.append(next2)
        else:
            player2.append(next2)
            player2.append(next1)
    else:
        play_round(player1, player2)



def hash_players(player1, player2):
    return "".join(map(str, player1))+";"+"".join(map(str, player2))


def play_recursive_game(player1, player2):
    played_rounds = set()
    while no_winner(player1, player2):
        played_round = hash_players(player1, player2)
        if played_round in played_rounds:
            return player1
        else:
            played_rounds.add(played_round)
        play_second_round(player1, player2)
    if len(player1) > 0:
        return player1
    else:
        return player2



def solution2(file_name):
    player1, player2 = prepare_data(file_name)
    winner = play_recursive_game(player1, player2)
    return calculater_winner_score(winner)


def solution(file_name):
    player1, player2 = prepare_data(file_name)
    winner = play_game(player1, player2)
    return calculater_winner_score(winner)


def calculater_winner_score(winner):
    factor = 1
    sum = 0
    for card in reversed(winner):
        sum += factor * card
        factor += 1
    return sum


def test_prepare_data():
    assert [3, 2, 10, 6, 8, 5, 9, 4, 7, 1] == prepare_data('test_1')


def test_solution():
    assert 306 == solution('test_1')


def test_solution_real():
    result = solution('input')
    assert 35299 == result


def test_solution2():
    result = solution2('input')
    print(result)
    assert 291 == result


def test_solution2_real():
    result = solution2('input')
    print(result)
    assert 33266 == result

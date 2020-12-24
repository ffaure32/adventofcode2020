from utils import file_utils


def no_winner(player1, player2):
    return len(player1) > 0 and len(player2) > 0


def prepare_data(file_name):
    lines = file_utils.get_lines(file_name)
    player1 = [int(card) for card in lines[0].split(',')]
    player2 = [int(card) for card in lines[1].split(',')]

    while no_winner(player1, player2):
        next1 = player1.pop(0)
        next2 = player2.pop(0)
        if next1 > next2:
            player1.append(next1)
            player1.append(next2)
        else:
            player2.append(next2)
            player2.append(next1)
    if len(player1) > 0:
        return player1
    else:
        return player2


def solution(file_name):
    winner = prepare_data(file_name)
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

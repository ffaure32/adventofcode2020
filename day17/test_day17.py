import day17, day172

def test_neighbours():
    total = day17.solution("test_1")
    assert total == 112

def test_neighbours_real():
    total = day17.solution("input")
    assert total == 286

def test_neighbours2():
    total = day172.solution("test_1")
    assert total == 848

def test_neighbours2_real():
    total = day172.solution("input")
    assert total == 848


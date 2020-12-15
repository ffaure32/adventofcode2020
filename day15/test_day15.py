import day15

def test_solution():
    assert 436 == day15.solution([0,3,6])

def test_samples():
    assert 1 == day15.solution([1,3,2])
    assert 10 == day15.solution([2,1,3])
    assert 27 == day15.solution([1,2,3])

def test_solution_real():
    assert 240 == day15.solution([14,8,16,0,1,17])

#def test_solution2():
    #assert 175594 == day15.solution2([0,3,6])

def test_solution2_real():
    assert 240 == day15.solution2([14,8,16,0,1,17])

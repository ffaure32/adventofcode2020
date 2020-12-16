import day7


def test_parse_line_with_one_content():
    ruleString = "bright white bags contain 1 shiny gold bag."
    rules = day7.parse_rule(ruleString)
    assert len(rules) == 1
    assert rules[0].contained == "shiny gold"
    assert rules[0].container == "bright white"
    assert rules[0].count == 1


def test_parse_line_with_no_content():
    ruleString = "faded blue bags contain no other bags."
    rules = day7.parse_rule(ruleString)
    assert len(rules) == 0


def test_parse_line_with_no_content():
    ruleString = "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags."
    rules = day7.parse_rule(ruleString)
    assert len(rules) == 2


# parser tous les liens
# filter shiny gold
# tant que pas 0 chercher parents


def test_parse_all_rules():
    rules = day7.prepare_data("test_1")
    assert len(rules) == 13



def test_parse_all_real_rules():
    rules = day7.prepare_data("input")
    assert len(rules) == 1473


def test_find_shiny():
    prepared_data = day7.prepare_data("test_1")
    shiny_rules = day7.find_parents(prepared_data, "shiny gold")
    assert len(shiny_rules) == 2


def test_day7():
    result = day7.solution("test_1")
    assert result == 4

def test_day7_real():
    result = day7.solution("input")
    assert result == 233

def test_day7_part2():
    result = day7.solution2("test_1")
    assert result == 32

def test_day7_real_part2():
    result = day7.solution2("input")
    assert result == 421550

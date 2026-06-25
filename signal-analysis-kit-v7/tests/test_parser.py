from signal_analysis_kit.parser import parse_line, parse_text


def test_parse_single_token_line():
    event = parse_line("09:11 МСК — НЖТИ 93348 АМИЛОВКУС 4443 8162")
    assert event.time == "09:11"
    assert event.timezone == "МСК"
    assert event.tag == "НЖТИ"
    assert event.identifier == "93348"
    assert event.tokens == ["АМИЛОВКУС"]
    assert event.numbers == [4443, 8162]


def test_parse_compound_token_line():
    event = parse_line("10:42 МСК — НЖТИ 71253 ГИДОПРАХ 6117 6933 ПРЕДСТОЯЩИЙ 2975 6431")
    assert event.tokens == ["ГИДОПРАХ", "ПРЕДСТОЯЩИЙ"]
    assert event.numbers == [6117, 6933, 2975, 6431]


def test_parse_text():
    events = parse_text("09:16 МСК — НЖТИ 26340 РАСТИРАНИЕ 7231 2405")
    assert len(events) == 1

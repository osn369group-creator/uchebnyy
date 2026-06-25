from signal_analysis_kit.parser import parse_file
from signal_analysis_kit.analysis import classify, summarize


def test_sample_analysis():
    events = parse_file("data/sample.txt")
    summary = summarize(events)
    result = classify(events)
    assert summary["event_count"] == 10
    assert summary["compound_events"] == 3
    assert "structured_protocol" in result["labels"]

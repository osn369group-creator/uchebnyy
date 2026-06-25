from __future__ import annotations

from collections import Counter
import math

from signal_analysis_kit.parser import SignalEvent


def hhmm_to_minutes(value: str) -> int:
    h, m = value.split(":")
    return int(h) * 60 + int(m)


def entropy(items: list[object]) -> float:
    if not items:
        return 0.0
    counts = Counter(items)
    total = len(items)
    return -sum((n / total) * math.log2(n / total) for n in counts.values())


def intervals(events: list[SignalEvent]) -> list[int]:
    values = [hhmm_to_minutes(e.time) for e in events]
    return [b - a for a, b in zip(values, values[1:])]


def detect_bursts(events: list[SignalEvent], threshold: int = 12) -> list[dict]:
    out = []
    for idx, minutes in enumerate(intervals(events), start=1):
        if minutes <= threshold:
            out.append({"index": idx, "interval_minutes": minutes, "mode": "burst"})
    return out


def summarize(events: list[SignalEvent]) -> dict:
    ints = intervals(events)
    all_tokens = [token for event in events for token in event.tokens]
    all_numbers = [number for event in events for number in event.numbers]
    return {
        "event_count": len(events),
        "intervals_minutes": ints,
        "interval_mean": sum(ints) / len(ints) if ints else 0,
        "interval_min": min(ints) if ints else 0,
        "interval_max": max(ints) if ints else 0,
        "unique_tokens": len(set(all_tokens)),
        "token_entropy": entropy(all_tokens),
        "number_entropy": entropy(all_numbers),
        "numeric_blocks": len(all_numbers),
        "compound_events": sum(1 for e in events if len(e.tokens) > 1),
        "burst_events": len(detect_bursts(events)),
    }


def classify(events: list[SignalEvent]) -> dict:
    summary = summarize(events)
    labels = []
    if len(set(e.tag for e in events)) <= 1:
        labels.append("structured_protocol")
    if summary["burst_events"] >= 2:
        labels.append("burst_scheduler")
    if summary["number_entropy"] >= 3.0:
        labels.append("randomized_numeric_layer")
    if summary["compound_events"] > 0:
        labels.append("compound_token_mode")
    return {"labels": labels or ["low_structure_stream"], "summary": summary}

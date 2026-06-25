from __future__ import annotations

from dataclasses import dataclass
import re

NUMBER_RE = re.compile(r"^\d{4}$")
ID_RE = re.compile(r"^\d{5}$")

@dataclass
class SignalEvent:
    time: str
    timezone: str
    tag: str
    identifier: str
    tokens: list[str]
    numbers: list[int]
    raw: str

    def to_dict(self) -> dict:
        return {
            "time": self.time,
            "timezone": self.timezone,
            "tag": self.tag,
            "identifier": self.identifier,
            "tokens": self.tokens,
            "numbers": self.numbers,
            "raw": self.raw,
        }


def _strip_comment(line: str) -> str:
    return re.sub(r"\s*\(.+?\)\s*$", "", line).strip()


def parse_line(line: str) -> SignalEvent:
    raw = line.strip()
    clean = _strip_comment(raw).replace("—", " ").replace("-", " ")
    parts = clean.split()
    if len(parts) < 6:
        raise ValueError(f"Too few fields: {raw}")

    time = parts[0]
    timezone = parts[1]
    tag = parts[2]
    identifier = parts[3]
    if not ID_RE.match(identifier):
        raise ValueError(f"Expected 5-digit id, got {identifier!r}")

    tail = parts[4:]
    split_at = None
    for i, item in enumerate(tail):
        if NUMBER_RE.match(item):
            split_at = i
            break
    if split_at is None:
        raise ValueError(f"No numeric blocks found: {raw}")

    tokens = tail[:split_at]
    numbers = [int(x) for x in tail[split_at:] if NUMBER_RE.match(x)]
    return SignalEvent(time, timezone, tag, identifier, tokens, numbers, raw)


def parse_text(text: str) -> list[SignalEvent]:
    events = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        events.append(parse_line(line))
    return events


def parse_file(path: str) -> list[SignalEvent]:
    with open(path, "r", encoding="utf-8") as f:
        return parse_text(f.read())

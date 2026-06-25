from __future__ import annotations

import random

TOKENS = [
    "АМИЛОВКУС", "РАСТИРАНИЕ", "ГЕНОЛИС", "ГИДОПРАХ", "ПРЕДСТОЯЩИЙ",
    "ПРИДИРЧИВЫЙ", "УТЮГОНИТ", "ВОЛОКИТА", "АИСТОТИТР", "УЛУСОКОРМ",
    "ПОЛУОСТРОВ", "СЛУХОБЛИН", "ЛЕССОЛИТР",
]


def minutes_to_hhmm(minutes: int) -> str:
    minutes %= 24 * 60
    return f"{minutes // 60:02d}:{minutes % 60:02d}"


def generate_lines(count: int = 10, seed: int | None = None) -> list[str]:
    rng = random.Random(seed)
    current = 9 * 60 + 11
    lines = []
    for _ in range(count):
        identifier = f"{rng.randint(0, 99999):05d}"
        token_count = 2 if rng.random() < 0.25 else 1
        tokens = rng.sample(TOKENS, token_count)
        numbers = [f"{rng.randint(0, 9999):04d}" for _ in range(token_count * 2)]
        lines.append(" ".join([minutes_to_hhmm(current), "МСК", "—", "НЖТИ", identifier, *tokens, *numbers]))
        current += rng.randint(4, 12) if rng.random() < 0.35 else rng.randint(25, 80)
    return lines

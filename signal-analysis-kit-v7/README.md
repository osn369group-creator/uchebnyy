# Signal Analysis Kit v7

Production-ready toolkit for parsing, analyzing, classifying, monitoring, and generating structured signal-like text streams.

Designed for logs like:

```text
09:11 МСК — НЖТИ 93348 АМИЛОВКУС 4443 8162
09:16 МСК — НЖТИ 26340 РАСТИРАНИЕ 7231 2405
10:42 МСК — НЖТИ 71253 ГИДОПРАХ 6117 6933 ПРЕДСТОЯЩИЙ 2975 6431
```

## What it does

- Parses structured signal logs.
- Measures timing intervals, burst behavior, lexical diversity, numeric entropy, and format stability.
- Classifies streams as structured, burst-like, randomized, or hybrid.
- Generates synthetic streams for comparison.
- Provides a small CLI and testable Python package.

## What it does not do

- It does not decrypt messages.
- It does not attribute a source.
- It does not make claims about operational meaning.

The project focuses on observable structure, not hidden meaning.

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]

signalkit analyze data/sample.txt
signalkit generate --count 10
pytest
```

## Core idea

```text
analysis = detect_structure(stream) without assuming a hidden generator
```

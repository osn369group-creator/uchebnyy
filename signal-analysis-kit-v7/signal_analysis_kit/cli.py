from __future__ import annotations

import json
import typer

from signal_analysis_kit.parser import parse_file, parse_text
from signal_analysis_kit.analysis import classify, summarize
from signal_analysis_kit.generator import generate_lines

app = typer.Typer(help="Structured signal analysis toolkit")


@app.command()
def analyze(path: str):
    events = parse_file(path)
    typer.echo(json.dumps(classify(events), ensure_ascii=False, indent=2))


@app.command()
def parse(path: str):
    events = parse_file(path)
    typer.echo(json.dumps([e.to_dict() for e in events], ensure_ascii=False, indent=2))


@app.command()
def generate(count: int = 10, seed: int = 42):
    for line in generate_lines(count=count, seed=seed):
        typer.echo(line)


@app.command()
def analyze_text(text: str):
    events = parse_text(text)
    typer.echo(json.dumps({"summary": summarize(events), "classification": classify(events)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    app()

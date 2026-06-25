from setuptools import setup, find_packages

setup(
    name="signal-analysis-kit",
    version="0.7.0",
    packages=find_packages(),
    install_requires=["numpy", "typer", "rich"],
    extras_require={"dev": ["pytest"]},
    entry_points={"console_scripts": ["signalkit=signal_analysis_kit.cli:app"]},
)

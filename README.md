# Idle Language

## Developers

- Jesús Alejandro Galván Villarreal
- Luis Daniel Villarreal Ortega

## Requirements

- Python 3.7.2
- Antlr4

## Usage

To compile grammar and run idle, run the following command in your terminal:
```bash
$ ./idle <file-name>
```

## Development
To recompile grammar with antlr4:

```bash
$ antlr4 -Dlanguage=Python3 Idle.g4
```

To only run the compiler without recompiling the grammar:

```bash
$ python3 Idle.py <file-name>
```

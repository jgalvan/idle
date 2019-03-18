# Idle Language

## Developers

- Jesús Alejandro Galván Villarreal
- Luis Daniel Villarreal Ortega

## Requirements

- Python 3.7.2

## Usage

To run the compiler, in your terminal run the following command:
```bash
$ python Idle.py <file-name>
```

## Development
To recompile grammar with antlr:

```bash
$ antlr4 -Dlanguage=Python3 Idle.g4
```
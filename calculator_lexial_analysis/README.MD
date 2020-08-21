# Lexical Analysis

## Description

- recognize and tokenize Math expressions


## Input Output
- `"2 + 2"`:
    - `2 => number::int`
    - `+ => operator::plus`
    - `2 => number::int`

- `"4.4*3 + (3 / 4)"`:
    - `4.4 => number::float`
    - `* => operator::start`
    - `+ => operator::plus`
    - `( => parenthesis::open`
   -  `3 => number::int`
    - `/ => operator::bar`
    - `4 => number::int`
    - `) => parenthesis::close`
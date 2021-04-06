# Awkword in Python

A word generator for creative fantasy language construction.
Based on the tool at http://akana.conlang.org/tools/awkwords/.

# Features

- Split letters and phones into categories
- Define how letters from different categories interact and pair up with a custom regex-like grammar.
- Create complex phonotactical rules for words from simple building blocks.

# Categories

A category has a name (an uppercase letter) and a body (a string that follows the grammar in the next section).  Category bodies can contain other category names, leading to complex interactions.

# Main pattern

The main pattern is the starting point of the generator and uses categories' names to generate substrings, which then evaluate to a singular word.  See the example.

# Grammar

## Basic syntax

`/` divides text into options and chooses one randomly.
`a/b/c` will evaluate to *a*, *b*, or *c*.

`[]` treats its contents as a single unit.
`r[ed/am/ing]` will evaluate to *red*, *ram* or *ring*

`()` treats its contents like `[]` but might also evaluate to nothing (50% chance to).
`ham(mer/burger)` will evaluate to *ham*, *hammer* or *hamburger*.

## Weights

Assigning weights to a slash-delimited list of text will make options more or less likely.
`a*3/e` is 3 times more likely to evaluate to *a* than to *e*.

## Filters

Some results are undesirable, and can be filtered out with `^`.
`[VV]^aa` with `V=a/e/i` cannot evaluate to *aa* but any other combination of `VV` is permissible.

# Examples

With categories
```
C=p/t/k/s/m/n
H=w/h/r/l
V=a/i/u
N=m/n
X=[C(H)]^nh^mh
```

and the main pattern `XV(XV)(N)`, the following words might be generated.

*tra nwe pekan kiphi sane ke pinrim ke khin mi srin kekla pama nwa klin papram tiphe mriken pratha swithe kwenem trate than min te klim mam pemri sre nlasan kisa simren tan ma kin mamwam*
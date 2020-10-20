from tictactoe import winner


X = "X"
O = "O"
EMPTY = None

# X
print(
    X is winner([
        [X, X, X],
        [O, O, EMPTY],
        [X, EMPTY, EMPTY]
    ])
)

# O
print(
    O is winner([
        [X, X, EMPTY],
        [O, O, O],
        [X, EMPTY, EMPTY]
    ])
)

# None
print(
    None is winner([
        [X, X, EMPTY],
        [O, O, EMPTY],
        [X, EMPTY, EMPTY]
    ])
)

# X
print(
    X is winner([
        [X, X, EMPTY],
        [X, O, EMPTY],
        [X, EMPTY, EMPTY]
    ])
)

# O
print(
    O is winner([
        [X, O, EMPTY],
        [EMPTY, O, EMPTY],
        [X, O, EMPTY]
    ])
)

# X
print(
    X is winner([
        [X, O, EMPTY],
        [EMPTY, X, EMPTY],
        [X, O, X]
    ])
)

# O
print(
    O is winner([
        [X, EMPTY, O],
        [EMPTY, O, EMPTY],
        [O, O, X]
    ])
)

# X
print(
    X is winner([
        [O, O, X],
        [EMPTY, X, O],
        [X, EMPTY, EMPTY]
    ])
)

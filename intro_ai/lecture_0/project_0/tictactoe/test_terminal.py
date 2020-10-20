from tictactoe import terminal


X = "X"
O = "O"
EMPTY = None

print(
    True is terminal(
        [
            [X, O, EMPTY],
            [EMPTY, X, EMPTY],
            [X, O, X]
        ]
    )
)


print(
    False is terminal(
        [
            [X, O, EMPTY],
            [EMPTY, X, EMPTY],
            [X, O, EMPTY]
        ]
    )
)

print(
    True is terminal(
        [
            [X, X, O],
            [O, O, X],
            [X, O, O]
        ]
    )
)

from tictactoe import result, initial_state


X = "X"
O = "O"
EMPTY = None


print(
    [
        [EMPTY, EMPTY, X],
        [EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ] == result(
        initial_state(),
        (0, 2)
    )
)

print(
    [
        [EMPTY, EMPTY, X],
        [EMPTY, O, EMPTY],
        [EMPTY, EMPTY, EMPTY]
    ] == result([       
            [EMPTY, EMPTY, X],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]
        ],
        (1, 1)
    )
)

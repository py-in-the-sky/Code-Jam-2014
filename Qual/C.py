def transform(board, click, R, C):
    "transform board into expected format"
    rows = (board[(r-1)*C:r*C] for r in xrange(1, R+1))
    new_board = '\n'.join(rows)
    first_zero = next(i for i,e in enumerate(new_board) if e=='0')
    new_board = new_board[:first_zero] + click + new_board[first_zero+1:]
    return ''.join('.' if e=='0' else e for e in new_board)


def satisfies(state):
    "return True if meets all constraints; otherwise False"
    board, mines, rows_left = state
    return mines >= 0 and rows_left >= 0


def contiguous_zeros(board):
    ## BFS to ensure all zeros are contiguous
    ## get count of all zeros
    ## then start w/ one zero and to BFS to count all contiguous zeros
    ## return whether these counts are equal
    pass


def is_goal(state):
    ## any board passed here will already meet all constraints
    board, mines, rows_left = state
    return mines == rows_left == 0 and contiguous_zeros(board)


def get_last_row(board, C): return board[-C:] if board else None


def place_zeros(row_above):
    ## place zeros as neighbors to numbers but not to mines
    ## wherever a zero is placed, neighbor it with '.'
    C = len(row_above)
    ZERO = '0'
    SOME_NUMBER = '.0'
    OPEN = '_'
    MINE = '*'
    mine_indeces = (i for i,e in enumerate(row_above) if e==MINE)
    mine_neighbors = set().union(j for j in
                                 sum(([i-1,i,i+1] for i in mine_indeces), [])
                                 if 0<=j<C)
    number_neighbors = set()
    number_indeces = (i for i,e in enumerate(row_above) if e in SOME_NUMBER)
    for i in number_indeces:
        _candidates = tuple(j for j in (i-1,i,i+1) if 0<=j<C and j not in mine_neighbors)
        if not _candidates:
            ## the number under consideration cannot have any zero neighbors
            return tuple()
        else:
            number_neighbors.update(_candidates)


    ## make sure every number from row_above neighbors a zero in the new row
    ## but that no new zero neighbors a mine

    return ''.join(ZERO if e in SOME_NUMBER else OPEN for e in row_above)


def successors(state):
    "return all possible successor states that satisfy constraints"
    def count_mines(row): return sum(e=='*' for e in row)

    board, mines, rows_left = state
    if not rows_left:
        return []  # no successors
    elif board:  # have at least one row arranged so far
        new_rows = place_zeros( get_last_row(board, C) )
        return ( (board+r, mines-count_mines(r), rows_left-1) for r in new_rows )
    else:  # no rows arranged yet
        pass


def search(R, C, M):
    """use constraint propagation to find and return a board
    if no satisfying board found, return None"""
    ## DFS with a stack
    ## optimal subproblem:
    ## - construct the board one row at a time, from top to bottom
    ## - assume board so far is contructed according to constraints
    ## - then to extend the board by one row, give all non-zero numbers from the bottom
    ##   row of the board so far a zero neighbor in the new row you're adding
    ## - if at the end you've obeyed constraints and have placed all mines, then
    ##   return board; otherwise let None be returned
    start = (None, M, R)  # (board-so-far, mines-left, rows-left)
    # visited = set()  # what to keep in here?  bottom row, mines, rows left?
    stack = [ start ]

    while stack:
        # pull off stack w/ stack.pop(), check constraints
        # if constraints met, extend and add to stack w/ stack.append(new_row)
        # otherwise, don't add to stack
        state = stack.pop()
        if is_goal(state):
            return transform(state[0])
        # visited.add( (get_last_row(state[0], C), state[1], ... )
        for s in successors(state, C):  # all successors that satisfy constraints
            if satisfies(s):
                stack.append(s)


def solve(R, C, M):
    "return 'Impossible' or '\n'.join(rows)"
    ## a board can be solved iff:
    ##  - R*C-M == 1, or
    ##  - all zeros form a contiguous group and all numbers neighbor a zero
    CLICK = 'c'

    if (R*C - M) == 1:
        row1 = CLICK + '*'*(C-1)
        infix = '\n' if R>1 else ''
        other_rows = ('*'*C for _ in xrange(R-1))
        return row1 + infix + '\n'.join(other_rows)
    else:
        result = search(R, C, M)
        return transform(result, CLICK, R, C) if result else 'Impossible'


def main(fin, fout=None):
    """steps:
    1) read data from fin
    2) operate on data
    3) write answers to fout

    Note: fin is read-only and fout allows writing"""
    ## methods for reading from and writing to file objects:
    ## http://docs.python.org/2/tutorial/inputoutput.html#methods-of-file-objects

    T = int(fin.readline().strip())
    for t in xrange(T):
        R, C, M = map(int, fin.readline().strip().split())
        solution = solve(R, C, M)
        if fout is not None:
            fout.write('Case #{}:\n{}\n'.format(t+1, solution))
        else:
            print 'Case #{}:\n{}'.format(t+1, solution)


if __name__ == '__main__':
    ## TESTING ON PRACTICE INPUT
    with open('C-practice.in', 'r') as fin:
        main(fin)

    ## SMALL SUBMISSION
    # with open('C-small-attempt0.in', 'r') as fin:
    #     with open('C-small.out', 'w') as fout:
    #         main(fin, fout)

    ## LARGE SUBMISSION
    # with open('C-large.in', 'r') as fin:
    #     with open('C-large.out', 'w') as fout:
    #         main(fin, fout)

    print 'done!'

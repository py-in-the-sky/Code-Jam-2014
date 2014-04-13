def is_goal(state):
    """checks whether all spots/mines have been used, all non-zero numbers have
    have at least one zero neighbor, and all zeros form a contiguous group"""
    pass

def successors(state):
    "return successor states with constraints propagated"
    pass

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
        spots = R*C
        start_state = ('0'*spots, spots, M)  # board, spots-left, mines-left
        stack = [ start_state ]
        while stack:
            s = stack.pop()

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

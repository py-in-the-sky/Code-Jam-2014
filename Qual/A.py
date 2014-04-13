def solve(answer_a, answer_b, board_a, board_b):
    row_a = board_a[answer_a-1]
    row_b = board_b[answer_b-1]
    intersection = set(row_a).intersection(row_b)
    if not intersection:
        return 'Volunteer cheated!'
    if len(intersection) > 1:
        return 'Bad magician!'
    else:
        return intersection.pop()

def main(fin, fout):
    """steps:
    1) read data from fin
    2) operate on data
    3) write answers to fout

    Note: fin is read-only and fout allows writing"""
    ## methods for reading from and writing to file objects:
    ## http://docs.python.org/2/tutorial/inputoutput.html#methods-of-file-objects

    T = int(fin.readline().strip())
    for t in xrange(T):
        answer_a = int(fin.readline().strip())
        board_a = [map(int, fin.readline().strip().split()) for _ in xrange(4)]
        answer_b = int(fin.readline().strip())
        board_b = [map(int, fin.readline().strip().split()) for _ in xrange(4)]
        solution = solve(answer_a, answer_b, board_a, board_b)
        fout.write('Case #{}: {}'.format(t+1, solution) + '\n')
        # print 'Case #{}: {}'.format(t+1, solution)


if __name__ == '__main__':
    with open('A-small-attempt0.in', 'r') as fin:
        with open('A-small.out', 'w') as fout:
            main(fin, fout)

    print 'done!'

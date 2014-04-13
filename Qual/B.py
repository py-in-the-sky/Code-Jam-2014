from Queue import PriorityQueue

def is_goal(state):
    seconds, cookies, rate, C, F, X = state
    return cookies == X

def successors(state):
    ## two successors:
    ##  1. buy one farm and return new [new_seconds, cookies=0, rate+F, ...]
    ##  2. buy no farms but go for X cookies and return [new_seconds, cookies=X, ...]
    seconds, cookies, rate, C, F, X = state
    successor1 = (seconds+(C/rate), 0, rate+F, C, F, X)
    successor2 = (seconds+(X/rate), X, rate, C, F, X)
    return (successor1, successor2)

def solve(C, F, X):
    ## BFS w/ priority queue where cost is seconds and choice is go for X or go for a farm
    explored = set()
    queue = PriorityQueue()
    start = (0, 0, 2, C, F, X)  # seconds=0, cookies=0, rate=2, C, F, X
    queue.put(start)

    while not queue.empty():
        state = queue.get()
        if is_goal(state):
            return state[0]
        explored.add(state[1:])
        for s in successors(state):
            if s[1:] not in explored:
                queue.put(s)


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
        C, F, X = map(float, fin.readline().strip().split())
        solution = solve(C, F, X)
        fout.write('Case #{0}: {1:.7f}'.format(t+1, solution) + '\n')
        # print 'Case #{0}: {1:.7f}'.format(t+1, solution)


if __name__ == '__main__':
    # with open('B-practice.in', 'r') as fin:
    with open('B-large.in', 'r') as fin:
        with open('B-large.out', 'w') as fout:
            main(fin, fout)

    print 'done!'

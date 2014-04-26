from Queue import PriorityQueue
from collections import Counter

def is_consistent(state, goal, i):
    """verify goal and state match up to, but not including, bit i
    return value is equal to is_goal's when i == len(goal)+1 """
    _goal  = Counter(c[:i] for c in goal)
    _state = Counter(c[:i] for c in state)
    return _goal == _state

def is_goal(state, goal):
    """check whether every current in state is a current in goal
    NB: goal and state are sets of mutually unique currents"""
    return all(c in goal for c in state)

def flip(bit): return '0' if bit=='1' else '1'

def successors(nchanges, state, i):
    """flip bit i or don't flip it
    and move index of the bit under consideration, i, up one"""
    _flip = tuple(c[:i]+flip(c[i])+c[i+1:] for c in state)
    flip_it = [nchanges+1, _flip, i+1]
    dont    = [nchanges, state, i+1]
    return (flip_it, dont)

def solve(N, L, start, goal):
    """search for minimum bit switches to make start == goal
    NB: treat goal and start as sets of currents -- that is, order doesn't
    matter in comparing start to goal and all currents in start/goal
    are mutually unique"""
    # BFS w/ priority queue; queue orders by min bits flipped
    start_state = (0, start, 0)  # ( n_bits_flipped, state_of_currents, index )
    queue = PriorityQueue()
    queue.put( start_state )

    while not queue.empty():
        nchanges, state, index = queue.get()

        if is_goal(state, goal):
            return nchanges

        for nch,s,i in successors(nchanges, state, index):
            if is_consistent(s, goal, i):
                # when i = len(goal)+1, s will be added to queue
                # only if s == goal
                queue.put([nch, s, i])

    return 'NOT POSSIBLE'


def main(fin, fout=None):
    T = int(fin.readline().strip())
    for t in xrange(T):
        N, L = map(int, fin.readline().strip().split())
        start = tuple(fin.readline().strip().split())
        goal = frozenset(fin.readline().strip().split())
        solution = solve( N, L, start, goal )
        if fout is not None:
            fout.write('Case #{}: {}\n'.format(t+1, solution))
        else:
            print 'Case #{}: {}'.format(t+1, solution)


if __name__ == '__main__':
    ## ADJUST PROBLEM INDEX AND MODE
    problem = 'A'  # 'A', 'B', 'C', or 'D'
    mode = 'large'  # 'practice', 'small', 'large'

    if mode is 'practice':
        with open(problem+'-practice.in', 'r') as fin:
            main(fin)

    elif mode is 'small':
        with open(problem+'-small-practice.in', 'r') as fin:
            with open(problem+'-small.out', 'w') as fout:
                main(fin, fout)

    elif mode is 'large':
        with open(problem+'-large-practice.in', 'r') as fin:
            with open(problem+'-large.out', 'w') as fout:
                main(fin, fout)

    print ('done!' if mode in ('practice', 'small', 'large')
           else 'please choose a proper mode -- practice, small, or large')

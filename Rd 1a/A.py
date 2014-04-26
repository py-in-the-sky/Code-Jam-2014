# from Queue import PriorityQueue

def is_goal(state, goal): return state == goal

def flip(bit): return '0' if bit=='1' else '1'

def successors(nchanges, state, i):
    return (
            [nchanges+1, frozenset(c[:i]+flip(c[i])+c[i+1:] for c in state)],
            [nchanges, state]
            )

def solve(N, L, start, goal):
    # BFS w/ priority queue
    # explored = set()
    # queue = PriorityQueue()
    start_state = [0, start]  # [ n_changes_to_currents, state_of_currents ]
    # queue.put(start_state)
    queue = [ start_state ]

    for i in xrange(L+1):
    # while not queue.empty():
    #   nchanges, state = queue.get()
        new_queue = []
        for nchanges,state in queue:
            if is_goal(state, goal):
                return nchanges

            # explored.add(state)
            if i < L:
                for nch,s in successors(nchanges, state, i):
                    # if s not in explored:
                        new_queue.append([nch, s])
        queue = new_queue
        # print queue

    return 'NOT POSSIBLE'


def main(fin, fout=None):
    T = int(fin.readline().strip())
    for t in xrange(T):
        N, L = map(int, fin.readline().strip().split())
        start = frozenset(fin.readline().strip().split())
        goal = frozenset(fin.readline().strip().split())
        solution = solve( N, L, start, goal )
        if fout is not None:
            fout.write('Case #{}: {}\n'.format(t+1, solution))
        else:
            print 'Case #{}: {}'.format(t+1, solution)


if __name__ == '__main__':
    ## ADJUST PROBLEM INDEX AND MODE
    problem = 'A'  # 'A', 'B', 'C', or 'D'
    mode = 'practice'  # 'practice', 'small', 'large'

    if mode is 'practice':
        with open(problem+'-practice.in', 'r') as fin:
            main(fin)

    elif mode is 'small':
        with open(problem+'-small-attempt0.in', 'r') as fin:
            with open(problem+'-small.out', 'w') as fout:
                main(fin, fout)

    elif mode is 'large':
        with open(problem+'-large.in', 'r') as fin:
            with open(problem+'-large.out', 'w') as fout:
                main(fin, fout)

    print ('done!' if mode in ('practice', 'small', 'large')
           else 'please choose a proper mode -- practice, small, or large')

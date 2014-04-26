def is_binary(tree):
    cond1 = all(len(v) in (0,2) for v in tree.values())

def solve(edges):
    pass


def main(fin, fout=None):
    T = int(fin.readline().strip())
    for t in xrange(T):
        N = int(fin.readline().strip())
        edges = set(tuple(map(int, fin.readline().strip().split()))
                    for _ in xrange(N-1))
        solution = solve( edges )
        if fout is not None:
            fout.write('Case #{}: {}\n'.format(t+1, solution))
        else:
            print 'Case #{}: {}'.format(t+1, solution)


if __name__ == '__main__':
    ## ADJUST PROBLEM INDEX AND MODE
    problem = 'B'  # 'A', 'B', 'C', or 'D'
    mode = 'practice'  # 'practice', 'small', 'large'

    if mode is 'practice':
        with open(problem+'-practice.in', 'r') as fin:
            main(fin)

    elif mode is 'small':
        with open(problem+'-small-attempt1.in', 'r') as fin:
            with open(problem+'-small.out', 'w') as fout:
                main(fin, fout)

    elif mode is 'large':
        with open(problem+'-large.in', 'r') as fin:
            with open(problem+'-large.out', 'w') as fout:
                main(fin, fout)

    print ('done!' if mode in ('practice', 'small', 'large')
           else 'please choose a proper mode -- practice, small, or large')

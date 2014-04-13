## input file is second command-line argument; output file is third


##########  MAIN TEMPLATE   ##########
def solve( ... ):
    pass

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
        ...  # get parameters here
        solution = solve( ... )
        if fout is not None:
            fout.write('Case #{}: {}\n'.format(t+1, solution))
        else:
            print 'Case #{}: {}'.format(t+1, solution)


if __name__ == '__main__':
    ## ADJUST PROBLEM INDEX
    problem = 'A'  # 'A', 'B', 'C', or 'D'

    ## TESTING ON PRACTICE INPUT
    with open(problem+'-practice.in', 'r') as fin:
        main(fin)

    ## SMALL SUBMISSION
    # with open(problem+'-small-attempt0.in', 'r') as fin:
    #     with open(problem+'-small.out', 'w') as fout:
    #         main(fin, fout)

    ## LARGE SUBMISSION
    # with open(problem+'-large.in', 'r') as fin:
    #     with open(problem+'-large.out', 'w') as fout:
    #         main(fin, fout)

    print 'done!'


##########  MEMOIZATION TEMPLATE   ##########
"""
See code from Design of Computer Programs
"""
def memo(f):
    cache = {}
    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            result = cache[args] = f(*args)
            return result
        except TypeError:  # unhashable argument
            return f(*args)
    return _f

##########  BFS TEMPLATE   ##########
"""
See code from Design of Computer Programs
keys to BFS:
    - a general template for BFS
        - queue for min-steps; priority queue for min-cost (e.g., containing tuples of (running_cost, data))
        - states in hashable data structures (e.g., tuples instead of lists)
        - a 'visited' hash set to prevent duplication of work
            - cache just data in 'visited', not the whole (running_cost, data) state (the first
              time you visite data is along the least expensive path through data)
    - a domain-specific transition function with heuristics for generating next states
    - a domain-specific is_goal? function for checking whether goal is met

BFS using caching to prevent duplicating paths in a search; memoization uses caching to
prevent duplicating calculations in a tree aggregation
"""

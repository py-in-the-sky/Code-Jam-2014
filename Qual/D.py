"""
0.0 < mass < 1.0
all blocks have different masses

Ken's strategy: choose smallest mass larger than what Naomi announces; if he
    doesn't have a larger mass, then play smallest mass
See the functions deceitful and honest for Naomi's strategies
"""
# from itertools import takewhile

def deceitful(Naomi, Ken):
    ## Naomi knows the masses of Ken's blocks
    ## strategy: Naomi sacrifices her smallest blocks against Ken's largest blocks
    Naomi.reverse()  # reversed for efficient removal of elements
    ## Naomi now listed from largest to smallest
    naomi_score = 0
    while Naomi:
        ## each loop represents one round of the game for Naomi (i.e., decide
        ## which block to play and play it, simulating Ken's response)
        ## keep playing until no more blocks left (i.e., Naomi is an empty tuple)
        n = Naomi.pop()
        if n < Ken[0]:  # Naomi's smallest block is smaller than Ken's smallest
            ## Naomi says its mass is between Ken's two largest blocks
            Ken.pop()  # Ken plays his largest block and collects a point
        elif n > Ken[0]:  # Naomi's smallest block is larger than Ken's smallest
            ## this branch doesn't exactly simulate the game; rather, we know
            ## that eventually in the game, Ken[0] will be beat by one of Naomi's
            ## blocks since they have the same number of blocks and Ken[0] is
            ## smaller than all of Naomi's
            Ken.pop(0)  # so we get rid of Ken's smallest block
            naomi_score += 1  # and Naomi (eventually) collects a point against that block

    return naomi_score

def honest(Naomi, Ken):
    ## strategy: just announce honestly
    ken_score = 0  # Ken's points
    i = -1  # index of the largest block played by Ken so far
    for n in Naomi:
        ## for each block in Naomi's list, find the smallest of Ken's blocks
        ## that haven't been played and give Ken a point, simulating him playing
        ## that smallest block (loop invariant: i is the index of the largest
        ## block played by Ken so far)
        ## otherwise break out of the loop because all of Naomi's blocks are
        ## larger than Ken's (i.e., Ken can't earn any more points)
        i = next((k+i+1 for k,e in enumerate(Ken[i+1:]) if e>n), None)
        if i is not None:
            ken_score += 1
        else:
            break
    return len(Naomi) - ken_score

def solve(Naomi, Ken):
    Naomi = sorted(Naomi)  # smallest to largest
    Ken = sorted(Ken)
    z = honest(Naomi, Ken)
    y = deceitful(Naomi, Ken)  # deceitful mutates lists, so it comes after honest
    return (y, z)

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
        N = int(fin.readline().strip())
        Naomi = map(float, fin.readline().strip().split())
        Ken = map(float, fin.readline().strip().split())
        y, z = solve(Naomi, Ken)
        if fout is not None:
            fout.write('Case #{}: {} {}\n'.format(t+1, y, z))
        else:
            print 'Case #{}: {} {}'.format(t+1, y, z)


if __name__ == '__main__':
    ## ADJUST PROBLEM INDEX
    problem = 'D'  # 'A', 'B', 'C', or 'D'

    ## TESTING ON PRACTICE INPUT
    with open(problem+'-practice.in', 'r') as fin:
        main(fin)

    # # SMALL SUBMISSION
    # with open(problem+'-small-practice.in', 'r') as fin:
    #     with open(problem+'-small.out', 'w') as fout:
    #         main(fin, fout)

    ## LARGE SUBMISSION
    # with open(problem+'-large-practice.in', 'r') as fin:
    #     with open(problem+'-large.out', 'w') as fout:
    #         main(fin, fout)

    print 'done!'

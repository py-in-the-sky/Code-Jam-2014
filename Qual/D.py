"""
0.0 < mass < 1.0
all blocks have different masses

Ken's strategy: choose smallest mass larger than what Naomi announces; if he
    doesn't have a larger mass, then play smallest mass
Naomi's deceitful strategy: announce a mass between Ken's two largest and then
    actually play her smallest mass; after all her masses are larger than Ken's,
    then she no longer has to be deceitful
Naomi's war strategy: play from smallest to largest, announcing honestly
"""
# from itertools import takewhile

def deceitful(Naomi, Ken, naomi=0):
    # Naomi = tuple(list(reversed(Naomi)))
    # if not Naomi:
    #     return naomi
    while Naomi:
        while Naomi and Naomi[0]<Ken[0]:
            Naomi = Naomi[1:]
            Ken = Ken[:-1]
        while Naomi and Naomi[0]>Ken[0]:
            naomi += 1
            Naomi = Naomi[1:]
            Ken = Ken[1:]
    # return deceitful(Naomi, Ken, naomi)
    return naomi

def honest(Naomi, Ken):
    ken = 0
    i = -1
    for n in Naomi:
        i = next((k+i+1 for k,e in enumerate(Ken[i+1:]) if e>n), None)
        if i is not None:
            ken += 1
        else:
            break
    return len(Naomi) - ken

def solve(Naomi, Ken):
    Naomi = tuple(sorted(Naomi))  # smallest to largest
    Ken = tuple(sorted(Ken))
    y = deceitful(Naomi, Ken)
    z = honest(Naomi, Ken)
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
    # with open(problem+'-practice.in', 'r') as fin:
    #     main(fin)

    # # SMALL SUBMISSION
    # with open(problem+'-small-practice.in', 'r') as fin:
    #     with open(problem+'-small4.out', 'w') as fout:
    #         main(fin, fout)

    ## LARGE SUBMISSION
    with open(problem+'-large-practice.in', 'r') as fin:
        with open(problem+'-large2.out', 'w') as fout:
            main(fin, fout)

    print 'done!'

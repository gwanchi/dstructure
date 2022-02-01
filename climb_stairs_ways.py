"""
Given a staircase of n steps, and a set of possible steps that we can climb at a time named possibleSteps, create a function that returns the number ways that a person can take to reach the top of the staircase.
"""


def waysToClimb(n, possibleSteps):
    if n == 0:
        return 1
    nbWays = 0
    for steps in possibleSteps:
        if (n - steps) >= 0:
            nbWays += waysToClimb(n - steps, possibleSteps)
    return nbWays

def waysToClimb2(n, possibleSteps):
    nbWaysArr = [0]*(n+1)
    nbWaysArr[0] = 1
    for i in range(1, n+1):
        nbWays = 0
        for steps in possibleSteps:
            if (i-steps) >= 0:
                nbWays += nbWaysArr[i-steps]
        nbWaysArr[i] = nbWays
    return nbWaysArr[n]

print(waysToClimb2(7, {2, 3, 4}))

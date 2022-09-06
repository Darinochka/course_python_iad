import itertools


def check_gap(features):

    for x in itertools.combinations(features[:3], 2):      # sides of the brick
        for s in itertools.permutations(features[3:], 2):  # sides of the gap
            if x[0] <= s[0] and x[1] <= s[1]:
                return "YES"
    return "NO"


n = 5
features = [int(input()) for i in range(n)]

print(check_gap(features))

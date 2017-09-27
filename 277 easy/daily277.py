# https://www.reddit.com/r/dailyprogrammer/comments/4uhqdb/20160725_challenge_277_easy_simplifying_fractions/
# Essentially, take a bunch of fractions and simplify them


# Euclidean Algorithm
def my_gcd(x: int, y: int):
    if y == 0:
        return x
    return my_gcd(y, x % y)


# Reads input into int array
file = list(map(int, open('input_daily277.txt', 'r').read().replace('\n', ' ').split(' ')))
for i in range(0, len(file) - 2, 2):
    gcd = my_gcd(file[i], file[i + 1])
    print('%d %d' % (file[i] / gcd, file[i + 1] / gcd))

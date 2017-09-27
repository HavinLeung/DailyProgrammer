# https://www.reddit.com/r/dailyprogrammer/comments/5bn0b7/20161107_challenge_291_easy_goldilocks_bear/
# Essentially, take in goldilock's weight and max temperature
# and print out every chair/soup combination that works for her

inputs = list(map(int, open('file.txt').read().replace('\n', ' ').split(' ')))
for x in range(2, len(inputs), 2):
    if inputs[x] > inputs[0] and inputs[x+1] < inputs[1]:
        print(int(x/2), end=' ')

def vote(votes):
    votes = sorted(votes)
    max_vote = 0
    for k in set(votes):
        if max_vote < votes.count(k):
            max_vote = k
    return max_vote


if __name__ == '__main__':
    print(vote([1, 1, 1, 2, 3]))
    print(vote([1, 3, 3, 2, 2]))

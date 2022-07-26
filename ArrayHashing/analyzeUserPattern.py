"""
1152. Analyze User Website Visit Pattern

You are given two string arrays username and website and an integer array timestamp. All the given arrays are of the same length and the tuple [username[i], website[i], timestamp[i]] indicates that the user username[i] visited the website website[i] at time timestamp[i].

A pattern is a list of three websites (not necessarily distinct).

For example, ["home", "away", "love"], ["leetcode", "love", "leetcode"], and ["luffy", "luffy", "luffy"] are all patterns.
The score of a pattern is the number of users that visited all the websites in the pattern in the same order they appeared in the pattern.

For example, if the pattern is ["home", "away", "love"], the score is the number of users x such that x visited "home" then visited "away" and visited "love" after that.
Similarly, if the pattern is ["leetcode", "love", "leetcode"], the score is the number of users x such that x visited "leetcode" then visited "love" and visited "leetcode" one more time after that.
Also, if the pattern is ["luffy", "luffy", "luffy"], the score is the number of users x such that x visited "luffy" three different times at different timestamps.
Return the pattern with the largest score. If there is more than one pattern with the same largest score, return the lexicographically smallest such pattern.
"""

from collections import Counter, defaultdict
def mostVisitedPattern(username, timestamp, website):

    user_activities_count = Counter(username)
    user_without_enough_activities = set([user for user in username if user_activities_count[user] < 3])

    users_activities = [[username[i], website[i], timestamp[i]] for i in range(len(username))]
    pattern_score = defaultdict(int)

    for user in set(username):
        if user in user_without_enough_activities:
            continue
        else:
            user_activities = [users_activities[i] for i in range(len(users_activities)) if users_activities[i][0] == user]
            user_activities.sort(key=lambda x: x[2])

            visited = set()
            for i in range(len(user_activities)-2):
                for j in range(i+1, len(user_activities)-1):
                    for k in range(j+1, len(user_activities)):
                        pattern = (user_activities[i][1], user_activities[j][1], user_activities[k][1])
                        if pattern not in visited:
                            pattern_score[pattern] += 1
                            visited.add(pattern)

    max_freq = max(pattern_score.values())
    res = sorted([pattern for pattern in pattern_score if pattern_score[pattern] == max_freq])[0]
    return list(res)

# time: n(n**3)
# space: n(n**3)

#w We may utilize combination function and Counter.update()


def test():
    username = ["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"]
    timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    website = ["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"]
    assert mostVisitedPattern(username, timestamp, website) == ["home","about","career"]
    username = ["ua","ua","ua","ub","ub","ub"]
    timestamp = [1,2,3,4,5,6]
    website = ["a","b","a","a","b","c"]
    assert mostVisitedPattern(username, timestamp, website) == ["a","b","a"]
    print("All tests passed!")
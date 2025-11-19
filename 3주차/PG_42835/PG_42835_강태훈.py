def solution(people, limit):
    people.sort()
    ans, s, e = 0, 0, len(people) - 1
    
    while s <= e:
        s = s + (people[s] + people[e] <= limit)
        e -= 1
        ans += 1
    return ans

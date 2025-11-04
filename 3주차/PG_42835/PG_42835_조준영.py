def solution(people, limit):
    people.sort()
    left = 0
    right = len(people)-1

    answer = 0

    while left<=right:
        answer+=1

        if left != right and people[left]+people[right]<=limit:
            left+=1
        right -= 1
    return answer
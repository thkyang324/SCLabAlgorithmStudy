"""
문제: Two Sum (LeetCode #1)
플랫폼: LeetCode
난이도: 🟢 쉬움
유형: 자료구조 - 해시

문제 설명:
정수 배열 nums와 목표값 target이 주어졌을 때,
배열에서 두 수를 더해 target이 되는 두 인덱스를 반환하시오.

접근 방법:
1. 해시맵을 사용하여 O(n) 시간 복잡도로 해결
2. 각 원소를 순회하면서 (target - 현재 값)이 해시맵에 있는지 확인
3. 있으면 해당 인덱스와 현재 인덱스를 반환
4. 없으면 현재 값과 인덱스를 해시맵에 저장

시간 복잡도: O(n)
공간 복잡도: O(n)
"""

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    # 해시맵: {값: 인덱스}
    hash_map = {}
    
    for i, num in enumerate(nums):
        # target - num이 해시맵에 있는지 확인
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        
        # 현재 값을 해시맵에 저장
        hash_map[num] = i
    
    return []  # 해가 없는 경우 (문제 조건상 항상 해가 존재)


# 테스트 케이스
if __name__ == "__main__":
    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {twoSum(nums1, target1)}")
    print(f"Expected: [0, 1]\n")
    
    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(f"Input: nums = {nums2}, target = {target2}")
    print(f"Output: {twoSum(nums2, target2)}")
    print(f"Expected: [1, 2]\n")
    
    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    print(f"Input: nums = {nums3}, target = {target3}")
    print(f"Output: {twoSum(nums3, target3)}")
    print(f"Expected: [0, 1]")

def solution(nums):
    # O(n)
    ht = set(nums)
    longest = 0

    for num in nums:
        if num not in ht:
            continue
        count = 1
        queue = [num]
        ht.remove(num)

        while queue:
            current = queue.pop(0)
            if current + 1 in ht:
                count += 1
                queue.append(current + 1)
                ht.remove(current + 1)
            if current - 1 in ht:
                count += 1
                queue.append(current - 1)
                ht.remove(current - 1)
        if count > longest:
            longest = count

    return longest
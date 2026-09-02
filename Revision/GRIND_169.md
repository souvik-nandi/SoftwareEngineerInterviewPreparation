# 1. First Bad Version

## Problem Information

- **Problem Name:** First Bad Version
- **Problem Link:** [First Bad Version](https://leetcode.com/problems/first-bad-version)
- **Difficulty:** Easy
- **Topics:** Binary Search
- **Pattern:** First True / Lower Bound Binary Search

---

## Problem Statement

You are given `n` versions `[1, 2, ..., n]`.

You are told that after a certain version, all subsequent versions become bad.

Given an API:

```python
isBadVersion(version)
```

Return the first bad version while minimizing the number of API calls.

---

## Constraints

```text
1 <= bad <= n <= 2^31 - 1
```

---

## My Solution

```python
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 1
        high = n

        while low < high:
            cur = low + (high - low) // 2

            badVersionFlag = isBadVersion(cur)

            if badVersionFlag:
                high = cur
            else:
                low = cur + 1

        return low
```

---

## Solution Explanation

The versions form a monotonic sequence:

```text
Good Good Good Good Bad Bad Bad Bad
```

This allows us to use Binary Search.

- If `mid` is bad, the first bad version can be `mid` itself or somewhere before it.
  - Move `high = mid`
- If `mid` is good, the first bad version must be after `mid`.
  - Move `low = mid + 1`

Continue until `low == high`.

The final value represents the first bad version.

---

## Time Complexity

- **Time:** `O(log n)`
- **Space:** `O(1)`

---

## Disadvantages of My Solution

- Requires understanding of Binary Search boundary conditions.
- Easy to introduce off-by-one errors.
- Not intuitive for developers unfamiliar with the "first occurrence" Binary Search pattern.

---

## Best Solution

Your solution is already the optimal solution.

```python
class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        while left < right:
            mid = left + (right - left) // 2

            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1

        return left
```

---

## Best Solution Explanation

This is a classic "First True" Binary Search.

The search space always contains the answer.

When a bad version is found, we keep it in the search space because it may be the first bad version.

When a good version is found, we eliminate it and everything before it.

Eventually, only one candidate remains.

---

## Time Complexity of Best Solution

- **Time:** `O(log n)`
- **Space:** `O(1)`

---

## Pattern Recognition

Use this Binary Search template when:

- Array/sequence is monotonic.
- Condition changes from False → True.
- Need to find the first occurrence of something.
- Need to minimize expensive API calls.

Typical pattern:

```text
False False False False True True True
```

---

## Key Learning

- Learn the "First True" Binary Search template.
- When `mid` can still be the answer:

```python
high = mid
```

not

```python
high = mid - 1
```

- Use:

```python
mid = low + (high - low) // 2
```

to avoid overflow in Java/C++.

---

## Common Mistakes

### Mistake 1

```python
high = mid - 1
```

May skip the actual first bad version.

### Mistake 2

```python
while low <= high
```

Makes boundary handling more complex.

### Mistake 3

Returning `high` without maintaining proper loop invariants.

---

## Edge Cases

### Case 1

```text
n = 1
bad = 1
```

Output:

```text
1
```

### Case 2

```text
bad = n
```

Last version is the first bad version.

### Case 3

```text
bad = 1
```

All versions are bad.

---

## Revision Notes

### Binary Search Template

```python
while low < high:
    mid = low + (high - low) // 2

    if condition(mid):
        high = mid
    else:
        low = mid + 1

return low
```

Remember:

> Whenever the current element can still be the answer, keep it in the search space.

---

## Status

- Solved Date: 2026-09-02
- Confidence Level: 5/5


# Grind 169 Notes

## 1 : Two Sum
### https://leetcode.com/problems/two-sum/
### Solution I submitted

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = dict()

        for idx, item in enumerate(nums):
            rem = target - item
            if rem in numDict:
                return [numDict[rem], idx]
            numDict[item] = idx

        return [-1, -1]

```

### Problems in the solution

* **None.** The logic is optimal.
* *(Minor)* `dict()` is slightly slower than the literal `{}`.

### Most optimized solution

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[n] = i

```

### Why the optimized solution is better

* **Same Complexity:** Both are  time and  space.
* **Syntax:** Using `{}` is the standard, slightly faster Pythonic way to initialize a dictionary.

---

## 2 : Valid Parentheses
### https://leetcode.com/problems/valid-parentheses/

### Solution I submitted
```python
class Solution:
    def isValid(self, s: str) -> bool:
        bracketsMap = { ')': '(', '}': '{', ']': '[' }
        validBracketsStart = set(['(', '{', '['])
        queue = []

        for c in s:
            if c in validBracketsStart:
                queue.append(c)
            elif c in bracketsMap:
                if not (queue and queue[-1] == bracketsMap[c]):
                    return False
                queue.pop()
            else:
                return False
            
        if queue:
            return False
        return True

```

### Problems in the solution

1. **Semantic Naming:** Named the variable `queue` (FIFO) but used it as a `stack` (LIFO).
2. **Redundant Logic:** `validBracketsStart` set is unnecessary; if a char isn't a closing bracket, it's an opening one.
3. **Inefficient Edge Case:** Missing a check for odd-length strings (which are always false), causing full traversal for those cases.
4. **Check at end:** The final `if queue` check can be returned directly.

### Most optimized solution

```python
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0: return False # Fast fail O(1)
        
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for c in s:
            if c in bracket_map:
                # Pop if stack exists, else use dummy '#'
                if bracket_map[c] != (stack.pop() if stack else '#'):
                    return False
            else:
                stack.append(c)
                
        return not stack

```

### Why the optimized solution is better

* **Performance:** Adds an  fast-fail for odd-length strings.
* **Readability:** Removes redundant sets and manual checks. Uses correct semantic naming (`stack`).

---

## 3 : Merge Two Sorted Lists
### https://leetcode.com/problems/merge-two-sorted-lists/
### Solution I submitted

```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2
        h3 = ListNode(0)
        newStart = h3

        while h1 or h2:
            nextVal = 0
            h1Val = h1.val if h1 else float('inf')
            h2Val = h2.val if h2 else float('inf')

            if h1Val < h2Val:
                nextVal = h1Val
                h1 = h1.next
            else:
                nextVal = h2Val
                h2 = h2.next
                
            h3.next = ListNode(nextVal)
            h3 = h3.next
        
        return newStart.next

```

### Problems in the solution

1. **Space Inefficiency:** Creates a **new node** (`ListNode(nextVal)`) for every element, resulting in  space.
2. **Complex Logic:** The `while h1 or h2` loop with `float('inf')` checks is harder to read and debug.
3. **Redundant Iterations:** Continues looping even when one list is empty.

### Most optimized solution

```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        # Loop only while BOTH have data
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1   # Point to existing node
                list1 = list1.next
            else:
                tail.next = list2   # Point to existing node
                list2 = list2.next
            tail = tail.next
            
        # Attach the remainder (one is guaranteed to be None)
        tail.next = list1 if list1 else list2
        
        return dummy.next

```

### Why the optimized solution is better

* **Space Complexity:**  extra space. It reuses existing nodes by "weaving" pointers rather than copying values.
* **Simplicity:** The logic cleanly handles the end of the lists by attaching the remainder in one step.

---

## 4 : Best Time to Buy and Sell Stock

### [https://leetcode.com/problems/best-time-to-buy-and-sell-stock/](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

### Solution I submitted

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxVal = 0
        maxProfit = 0

        for i in range(n-1, -1, -1):
            curVal = prices[i]
            if curVal > maxVal:
                maxVal = curVal
            else:
                maxProfit = max(maxProfit, maxVal - curVal)
        
        return maxProfit

```

### Problems in the solution

1. **Intuition:** While mathematically correct, iterating backwards is slightly less intuitive than simulating time forward (buying before selling).
2. **Naming:** `maxVal` is a bit generic; `max_future_price` would more clearly indicate that you are looking ahead for a selling point.
3. **Complexity:** None. This solution is actually **optimal** ( time,  space).

### Most optimized solution

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price # Found a cheaper buy price
            elif price - min_price > max_profit:
                max_profit = price - min_price # Update max profit
                
        return max_profit

```

### Why the optimized solution is better

* **Chronological Flow:** It iterates forward, which mimics the real-world passage of time (you encounter a buying opportunity *before* a selling opportunity).
* **Readability:** It is the standard "Greedy" pattern for this problem, making it immediately recognizable to interviewers.
* *Note: Your backward-pass solution is technically just as fast and memory-efficient.*

---

## 5 : Valid Palindrome
### https://leetcode.com/problems/valid-palindrome/

### Solution I submitted
```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n-1

        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() == s[r].lower():
                l += 1
                r -= 1
            else:
                return False
        
        return True

```

### Problems in the solution

* **None.** This solution is excellent.
* **Minor Flow:** Using `if/elif` means if you have 10 spaces in a row, the main `while` loop runs 10 times to skip them one by one. Using inner `while` loops (see below) allows you to skip them all in a single pass of the outer loop, though the complexity remains the same.

### Most optimized solution

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            # Move left pointer forward until an alphanumeric char is found
            while l < r and not s[l].isalnum():
                l += 1
            
            # Move right pointer backward until an alphanumeric char is found
            while l < r and not s[r].isalnum():
                r -= 1
            
            # Compare characters
            if s[l].lower() != s[r].lower():
                return False
            
            # After a successful match, move both pointers inward
            l, r = l + 1, r - 1
            
        return True

```

### Why the optimized solution is better

* **Handling Groups of Symbols:** By using nested `while` loops (e.g., `while ... not isalnum(): l += 1`), we skip *consecutive* non-alphanumeric characters instantly rather than re-evaluating the main loop condition for every single space or comma.
* **Readability:** It separates the "skipping logic" from the "comparison logic" more distinctly.

### Time and Space Complexity

* **Time:** O(n) (We traverse the string exactly once with two pointers).
* **Space:** O(1) (No new strings or data structures are created; we operate in place).

---

## 6 : Invert Binary Tree

### [https://leetcode.com/problems/invert-binary-tree/](https://leetcode.com/problems/invert-binary-tree/)

### Solution I submitted

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invertChildren(node):
            if not node:
                return
            node.left, node.right = node.right, node.left
            invertChildren(node.left)
            invertChildren(node.right)
        
        invertChildren(root)
        return root

```

### Problems in the solution

1. **Redundant Helper Function:** You defined an inner function `invertChildren` to handle the recursion. This is unnecessary because the main function `invertTree` already takes a `root` and returns a node, so it can be used recursively directly.
2. **Verbosity:** The helper function adds extra lines of code without adding any logical benefit or performance gain.

### Most optimized solution

```python
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Swap the children
        root.left, root.right = root.right, root.left
        
        # Recursively invert the subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

```

### Why the optimized solution is better

* **Conciseness:** It removes the need for a nested helper function, making the code cleaner and easier to read.
* **Standard Pattern:** This uses the method itself for recursion, which is the standard Pythonic pattern for tree problems.

### Time and Space Complexity

* **Time:** O(n) (We visit every node exactly once).
* **Space:** O(h) (The recursion stack will grow to the height of the tree. In the worst case of a skewed tree, this is O(n); for a balanced tree, it is O(log n)).

---

## 7 : Valid Anagram

### [https://leetcode.com/problems/valid-anagram/](https://leetcode.com/problems/valid-anagram/)

### Solution I submitted

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = [0] * 26

        for c in s:
            counter[ord(c) - ord('a')] += 1
        
        for c in t:
            pos = ord(c) - ord('a')

            if counter[pos] == 0:
                return False
            counter[pos] -= 1
        
        for item in counter:
            if item != 0:
                return False
        
        return True

```

### Problems in the solution

1. **Missing Length Check:** If `len(s)` is different from `len(t)`, they cannot be anagrams. Adding this check at the very beginning is an O(1) optimization that skips all loops for length mismatches.
2. **Redundant Final Loop:** If you check the lengths at the start, the final loop (`for item in counter`) becomes unnecessary. If the lengths are equal and you successfully process every character in `t` without the count dropping below zero, the `counter` array is mathematically guaranteed to be all zeros.

### Most optimized solution

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Optimization: Length mismatch = impossible to be anagrams
        if len(s) != len(t):
            return False
            
        counter = [0] * 26

        for c in s:
            counter[ord(c) - ord('a')] += 1
        
        for c in t:
            pos = ord(c) - ord('a')
            # If count is 0, t has more of this char than s
            if counter[pos] == 0:
                return False
            counter[pos] -= 1
            
        return True

```

### Why the optimized solution is better

* **Efficiency:** The length check provides an instant exit for invalid inputs.
* **Conciseness:** Removing the final loop reduces code size while maintaining correctness (relying on the invariant that equal lengths + subset match = exact match).

### Time and Space Complexity

* **Time:** O(n) (We iterate through both strings once).
* **Space:** O(1) (The counter array is fixed at size 26, regardless of input size).

---

## 8 : Binary Search

### [https://leetcode.com/problems/binary-search/](https://leetcode.com/problems/binary-search/)

### Solution I submitted

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n-1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1

```

### Problems in the solution

* **None.** This is the standard implementation.
* **Integer Overflow (Contextual):** In Python, `(low + high) // 2` is safe because integers have arbitrary precision. However, in languages like C++ or Java, `low + high` can exceed the maximum integer limit. It is good interview practice to calculate `mid` safely.

### Most optimized solution

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while low <= high:
            # Safe calculation for mid (prevents overflow in C++/Java)
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return -1

```

### Why the optimized solution is better

* **Overflow Safety:** Calculating `mid` as `low + (high - low) // 2` is mechanically the same as `(low + high) // 2` but prevents potential integer overflow in strictly typed languages. Using this form shows the interviewer you are aware of low-level constraints.

### Time and Space Complexity

* **Time:** O(log n) (The search space is divided in half during every iteration).
* **Space:** O(1) (Iterative approach uses constant extra space).

---

## 9 : Flood Fill

### [https://leetcode.com/problems/flood-fill/](https://leetcode.com/problems/flood-fill/)

### Solution I submitted

```python
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        startColor = image[sr][sc]

        if startColor != color:
            maxRow = len(image)
            maxCol = len(image[0])
            queue = [(sr, sc)]

            while queue:
                row, col = queue.pop()
                image[row][col] = color

                for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                    nr, nc = row + dr, col + dc

                    if (0 <= nr < maxRow and 0 <= nc < maxCol) and image[nr][nc] == startColor:
                        queue.append((nr, nc)) 
        
        return image

```

### Problems in the solution

1. **Duplicate Processing:** You color the pixel *after* popping it from the stack. This is dangerous because multiple neighbors might add the same node to the `queue` before it gets popped and colored. This causes the stack to grow exponentially with duplicate entries.
2. **Naming Mismatch:** You named the variable `queue`, but `queue.pop()` removes the *last* element, making it a **Stack** (DFS). A real queue uses `pop(0)` (BFS).
3. **Performance Trap (pop(0)):** Using pop(0) on a standard Python list is an O(k) operation (where k is the list length) because it must shift all remaining elements. This degrades the overall time complexity to O(N²) in the worst case. You must use collections.deque for O(1) pops.
4. **Verbosity:** The iterative approach with manual boundary checks inside the loop is slightly more verbose than the standard recursive DFS.

### Most optimized solution

```python
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        start_color = image[sr][sc]
        
        # Optimization: If the start color is already the target color, no change needed
        if start_color == color:
            return image
        
        def dfs(r, c):
            if image[r][c] == start_color:
                image[r][c] = color
                
                # Check neighbors directly
                if r >= 1: dfs(r-1, c)
                if r+1 < len(image): dfs(r+1, c)
                if c >= 1: dfs(r, c-1)
                if c+1 < len(image[0]): dfs(r, c+1)
        
        dfs(sr, sc)
        return image

```

### Why the optimized solution is better

* **Safety:** Recursive DFS implicitly handles the "visited" state by changing the color immediately upon entry, preventing infinite loops or duplicate processing.
* **Conciseness:** The recursive logic is cleaner and maps directly to the "flooding" intuition of the problem.
* **Performance:** It avoids the overhead of managing a manual stack with potential duplicate entries.

### Time and Space Complexity

* **Time:** O(N) (We process every pixel exactly once).
* **Space:** O(N) (The recursion stack can go as deep as the number of pixels in the worst case, e.g., a straight line).

---

## 10 : Lowest Common Ancestor of a Binary Search Tree

### [https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

### Solution I submitted

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node = root

        while node:
            if node.val > p.val and node.val > q.val:
                node = node.left
            elif node.val < p.val and node.val < q.val:
                node = node.right
            else:
                return node
        
        return None

```

### Problems in the solution

* **None.** You have correctly identified that for a BST, the LCA is the first node where the split occurs (one value is smaller, one is larger) or where the node equals one of the targets.
* **Optimization:** This iterative approach is actually superior to the recursive one because it avoids the memory overhead of the system stack.

### Most optimized solution

```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Optimization: We can reuse 'root' instead of creating 'node' var
        # Just walk down the tree until the split point is found
        while root:
            if root.val > p.val and root.val > q.val:
                root = root.left
            elif root.val < p.val and root.val < q.val:
                root = root.right
            else:
                return root
        return None

```

### Why the optimized solution is better

* **Space Complexity:** By using an iterative `while` loop instead of recursion, we achieve **O(1) space complexity**. A recursive solution would consume O(h) space on the call stack.
* **Simplicity:** The logic relies purely on the BST property (left < root < right), making it very intuitive.

### Time and Space Complexity

* **Time:** O(h) (where h is the height of the tree; O(log n) for balanced, O(n) for skewed).
* **Space:** O(1) (Iterative approach uses no extra memory).

---
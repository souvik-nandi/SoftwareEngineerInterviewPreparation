## 71. Simplify Path

Given a string `path`, which is an absolute path (starting with a slash `/`) to a file or directory in a Unix-style file system, convert it to the simplified canonical path.

In a Unix-style file system, a period `.` refers to the current directory, a double period `..` refers to the directory up a level, and any multiple consecutive slashes (i.e., `//`) are treated as a single slash `/`. For this problem, any other format of a path is considered invalid.

The simplified canonical path should have the following format:
1. The path starts with a single slash `/`.
2. Any two directories are separated by a single slash `/`.
3. The path does not end with a trailing `/`.
4. The path only contains the directories on the path from the root directory to the target file or directory (i.e., no periods `.` or double periods `..`).

### Problem Examples

#### Example 1:
- **Input:** `path = "/home/"`
- **Output:** `"/home"`
- **Explanation:** The simplified path is "/home", with no trailing slash.

#### Example 2:
- **Input:** `path = "/../"`
- **Output:** `"/"`
- **Explanation:** Going one level up from the root directory leads to the root itself.

#### Example 3:
- **Input:** `path = "/home//foo/"`
- **Output:** `"/home/foo"`
- **Explanation:** The extra slashes are collapsed into a single slash.

#### Example 4:
- **Input:** `path = "/a/./b/../../c/"`
- **Output:** `"/c"`
- **Explanation:** The "." refers to the current directory, so it's ignored; the ".." moves up one directory.

### Possible Solutions

1. **Stack-Based Path Simplification**

### Solution 1: Stack-Based Path Simplification

```python
class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.replace("//", "/")
        dirsList = path.split("/")
        stack = []

        for dirItem in dirsList:
            if dirItem == "..":
                if stack:
                    stack.pop()
            elif dirItem == "." or dirItem == "":
                continue
            else:
                stack.append(dirItem)

        return "/" + "/".join(stack)
```

#### Algorithm Description

1. **Normalize the Path**:
   - The input path may contain multiple consecutive slashes `//`. These are first normalized by replacing them with a single slash `/` to avoid unnecessary empty directory components.

2. **Split the Path**:
   - The path is split by slashes `/` into a list `dirsList`, where each element represents a directory name or a special component (`.` or `..`).

3. **Using a Stack for Simplification**:
   - The stack is used to keep track of the directories that form the simplified path.
   - For each directory in `dirsList`:
     - If the directory is `".."` and the stack is not empty, the top directory is popped from the stack, simulating moving up one level in the directory hierarchy.
     - If the directory is `"."` or an empty string (from consecutive slashes), it is ignored.
     - Otherwise, the directory is a valid directory name and is added to the stack.
   
4. **Construct the Simplified Path**:
   - The stack now contains the simplified path components. They are joined together with slashes to form the final simplified path.

5. **Return the Simplified Path**:
   - The simplified path is returned by concatenating a leading slash `/` with the joined stack elements.

#### Complexity Analysis

- **Time Complexity**: `O(n)`
  - The algorithm processes each character in the path string exactly once. The string splitting, stack operations, and final string joining all occur in linear time relative to the number of characters `n`.

- **Space Complexity**: `O(n)`
  - The space used by the stack and the list `dirsList` is proportional to the number of directory components in the path.

#### Potential Pitfalls

1. **Handling of Special Characters**:
   - Ensure that periods `.` and double periods `..` are correctly handled to represent the current directory and parent directory, respectively.
   
2. **Edge Cases**:
   - Edge cases such as paths with multiple consecutive slashes, leading or trailing slashes, and paths that resolve to the root directory need to be handled correctly.

3. **Empty Stack**:
   - When `".."` is encountered and the stack is empty, it means we're trying to move above the root directory, which is invalid in Unix-style file systems. This is correctly handled by simply continuing with an empty stack.

### Conclusion

The stack-based path simplification approach is optimal for this problem, efficiently managing the different components of the path string to produce the correct simplified path. It provides clear and correct handling of special cases like `.` and `..`, making it a robust solution for simplifying Unix-style file paths.

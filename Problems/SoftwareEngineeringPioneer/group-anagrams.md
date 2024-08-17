# 49. Group Anagrams

## Problem Description
Given an array of strings, group the anagrams together. An anagram is a word formed by rearranging the letters of a different word using all the original letters exactly once. For example, `"eat"`, `"tea"`, and `"ate"` are anagrams of each other.

### Example
- **Input:** `["eat", "tea", "tan", "ate", "nat", "bat"]`
- **Output:** `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`

## Solution 1: Using Sorting and Hash Map

### Algorithm

1. **Sort Each Word**
   - For each word in the list, sort the characters to obtain a canonical form of the word (e.g., `"tea"` becomes `"aet"`).

2. **Group Anagrams**
   - Use a hash map (dictionary) where the key is the sorted word and the value is a list of words that match that sorted key.

3. **Return Groups**
   - Return the values of the hash map, which represent the groups of anagrams.

### Code

```python
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramTable = defaultdict(list)

        for word in strs:
            # Sort the characters in the word to get the canonical form
            sortedWord = ''.join(sorted(word))
            # Append the original word to the list of the sorted key
            anagramTable[sortedWord].append(word)

        # Return the list of anagram groups
        return list(anagramTable.values())
```

### Complexity
- **Time Complexity:** `O(n * k log k)`, where `n` is the number of words and `k` is the maximum length of a word. Sorting each word takes `O(k log k)`, and this operation is done for each of the `n` words.
- **Space Complexity:** `O(n * k)`, where `n` is the number of words and `k` is the maximum length of a word. This accounts for the storage of the words and the hash map.

## Solution 2: Using Prime Numbers (Optimized Hashing)

### Algorithm

1. **Assign Prime Numbers**
   - Assign a unique prime number to each letter of the alphabet.

2. **Compute Hash**
   - Compute the hash of each word by multiplying the prime numbers corresponding to its characters.

3. **Group Anagrams**
   - Use a hash map where the key is the computed hash and the value is a list of words with that hash.

4. **Return Groups**
   - Return the values of the hash map, which represent the groups of anagrams.

### Code

```python
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Prime numbers for each letter in the alphabet
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        def get_hash(word: str) -> int:
            hash_value = 1
            for char in word:
                hash_value *= primes[ord(char) - ord('a')]
            return hash_value

        anagramTable = defaultdict(list)

        for word in strs:
            # Compute hash value for the word
            hash_value = get_hash(word)
            # Append the original word to the list of the hash key
            anagramTable[hash_value].append(word)

        # Return the list of anagram groups
        return list(anagramTable.values())
```

### Complexity
- **Time Complexity:** `O(n * k)`, where `n` is the number of words and `k` is the maximum length of a word. Calculating the hash value for each word is `O(k)`, and this is done for each of the `n` words.
- **Space Complexity:** `O(n * k)`, where `n` is the number of words and `k` is the maximum length of a word. This accounts for the storage of the words and the hash map.

## Solution 3: Using Character Count Tuples

### Algorithm

1. **Create Frequency Tuple**
   - Create a tuple representing the frequency of each character in the word.

2. **Group Anagrams**
   - Use a hash map where the key is the frequency tuple and the value is a list of words that match that tuple.

3. **Return Groups**
   - Return the values of the hash map, which represent the groups of anagrams.

### Code

```python
from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramTable = defaultdict(list)

        for word in strs:
            # Create a frequency tuple that represents the word
            charCount = [0] * 26  # Assuming only lowercase 'a' to 'z'
            for char in word:
                charCount[ord(char) - ord('a')] += 1
            
            # Use the tuple as the key
            anagramTable[tuple(charCount)].append(word)

        # Return the list of anagram groups
        return list(anagramTable.values())
```

### Complexity
- **Time Complexity:** `O(n * k)`, where `n` is the number of words and `k` is the maximum length of a word. Creating the frequency tuple for each word takes `O(k)`, and this is done for each of the `n` words.
- **Space Complexity:** `O(n * k)`, where `n` is the number of words and `k` is the maximum length of a word. This accounts for the storage of the words and the hash map.

## Comparison

### Sorting and Hash Map Approach
- **Pros:**
  - **Simplicity:** Easy to understand and implement.
  - **Clear and Direct:** Straightforward approach with clear operations.
- **Cons:**
  - **Time Complexity:** Sorting each word can be slower for long words or large lists.

### Prime Number Hashing Approach
- **Pros:**
  - **Time Efficiency:** Faster as it avoids sorting by using a unique hash.
  - **Unique Hashing:** Provides a unique identifier for anagrams.
- **Cons:**
  - **Complexity:** Slightly more complex to implement due to prime number hashing.
  - **Prime Number Choice:** Requires careful selection of primes to avoid collisions.

### Character Count Tuples Approach
- **Pros:**
  - **Efficient:** Directly represents the frequency of characters, which is very efficient.
  - **Simple Hashing:** Uses a fixed-size tuple for hashing, which is straightforward to compute.
- **Cons:**
  - **Tuple Size:** Limited to a fixed size of 26 for lowercase letters; not suitable for extended character sets.

### Conclusion
- **Sorting and Hash Map Approach:** Preferred for its simplicity and direct approach. Suitable for general use cases where ease of implementation is crucial.
- **Prime Number Hashing Approach:** Chosen for its potential efficiency gains, especially in cases where sorting becomes a bottleneck. More suitable for performance-critical applications.
- **Character Count Tuples Approach:** Provides a balance between efficiency and simplicity. Ideal for cases with only lowercase letters and when you need a straightforward yet efficient solution.

Each solution has its own strengths and trade-offs, making them suitable for different scenarios depending on the specific requirements of performance and complexity.

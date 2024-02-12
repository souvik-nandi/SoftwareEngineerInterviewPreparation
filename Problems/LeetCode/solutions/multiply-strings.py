'''

Problem Statement: Multiply Strings

Link: https://leetcode.com/problems/multiply-strings
Tags: ['Math', 'String']
Difficulty: Medium

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
 
Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

 
Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.



'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        int_map = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}
        nums1 = [int_map[x] for x in num1[::-1]]
        nums2 = [int_map[x] for x in num2[::-1]]
        final = [0 for _ in range(len(nums1) + len(nums2))]

        posa = 0
        carry = 0
        for a in nums1:
            posb = 0
            for b in nums2:
                final[posa + posb] = final[posa + posb] + a * b + carry
                final[posa + posb], carry = final[posa + posb] % 10,  final[posa + posb] // 10
                posb += 1
            
            final[posa + posb] = carry
            carry = 0
            posa += 1
    
        final = ''.join([str(x) for x in final[::-1]]).lstrip("0")
        
        return "0" if final == "" else final

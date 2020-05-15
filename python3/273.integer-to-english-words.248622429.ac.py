#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#
# https://leetcode.com/problems/integer-to-english-words/description/
#
# algorithms
# Hard (26.39%)
# Likes:    915
# Dislikes: 2541
# Total Accepted:    160.2K
# Total Submissions: 606.5K
# Testcase Example:  '123'
#
# Convert a non-negative integer to its english words representation. Given
# input is guaranteed to be less than 2^31 - 1.
# 
# Example 1:
# 
# 
# Input: 123
# Output: "One Hundred Twenty Three"
# 
# 
# Example 2:
# 
# 
# Input: 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# 
# Example 3:
# 
# 
# Input: 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty
# Seven"
# 
# 
# Example 4:
# 
# 
# Input: 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven
# Thousand Eight Hundred Ninety One"
# 
# 
#

# @lc code=start
GROUPS = {
    3: 'Thousand',
    6: 'Million',
    9: 'Billion'
}

DIGIT = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine'
}

TENS = {
    '1': 'Eleven',
    '2': 'Twelve',
    '3': 'Thirteen',
    '4': 'Fourteen',
    '5': 'Fifteen',
    '6': 'Sixteen',
    '7': 'Seventeen',
    '8': 'Eighteen',
    '9': 'Nineteen'
}

SECOND_DIGIT = {
    '1': 'Ten',
    '2': 'Twenty',
    '3': 'Thirty',
    '4': 'Forty',
    '5': 'Fifty',
    '6': 'Sixty',
    '7': 'Seventy',
    '8': 'Eighty',
    '9': 'Ninety',
}

def group_word(_len):
    return GROUPS[_len]

def digit_word(digit):
    return DIGIT[digit]
    
def two_digit_word(first_digit, second_digit):
    if first_digit == '1' and second_digit != '0':
        return TENS[second_digit]
        
    ret = [SECOND_DIGIT[first_digit]]
    if second_digit != '0':
        ret.append(DIGIT[second_digit])
    return ' '.join(ret)

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        digits = collections.deque(str(num))
        words, zeros = [], 0
        while digits:
            curr_digit = digits.popleft()
            mod = (len(digits)+1) % 3
            
            if mod == 0 and words and zeros < 3:
                words.append(group_word(len(digits) + 1))
                zeros = 0
            if curr_digit == '0':
                zeros += 1
                continue
            
            if mod == 0:
                words.append(digit_word(curr_digit))
                words.append('Hundred')
            elif mod == 2:
                words.append(two_digit_word(curr_digit, digits.popleft()))
            else:
                words.append(digit_word(curr_digit))
        return ' '.join(words)
# @lc code=end

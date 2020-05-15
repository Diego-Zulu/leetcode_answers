#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#
# https://leetcode.com/problems/text-justification/description/
#
# algorithms
# Hard (26.86%)
# Likes:    613
# Dislikes: 1494
# Total Accepted:    130.4K
# Total Submissions: 484.7K
# Testcase Example:  '["This", "is", "an", "example", "of", "text", "justification."]\n16'
#
# Given an array of words and a width maxWidth, format the text such that each
# line has exactly maxWidth characters and is fully (left and right)
# justified.
# 
# You should pack your words in a greedy approach; that is, pack as many words
# as you can in each line. Pad extra spaces ' ' when necessary so that each
# line has exactly maxWidth characters.
# 
# Extra spaces between words should be distributed as evenly as possible. If
# the number of spaces on a line do not divide evenly between words, the empty
# slots on the left will be assigned more spaces than the slots on the right.
# 
# For the last line of text, it should be left justified and no extra space is
# inserted between words.
# 
# Note:
# 
# 
# A word is defined as a character sequence consisting of non-space characters
# only.
# Each word's length is guaranteed to be greater than 0 and not exceed
# maxWidth.
# The input array words contains at least one word.
# 
# 
# Example 1:
# 
# 
# Input:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# Output:
# [
# "This    is    an",
# "example  of text",
# "justification.  "
# ]
# 
# 
# Example 2:
# 
# 
# Input:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# Output:
# [
# "What   must   be",
# "acknowledgment  ",
# "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall
# be",
# because the last line must be left-justified instead of fully-justified.
# ⁠            Note that the second line is also left-justified becase it
# contains only one word.
# 
# 
# Example 3:
# 
# 
# Input:
# words =
# ["Science","is","what","we","understand","well","enough","to","explain",
# "to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
# Output:
# [
# "Science  is  what we",
# ⁠ "understand      well",
# "enough to explain to",
# "a  computer.  Art is",
# "everything  else  we",
# "do                  "
# ]
# 
# 
#

# @lc code=start
def build_line(curr_line, curr_line_length, maxWidth):
    line = []
    min_spaces = len(curr_line) - 1
    mandatory_length = curr_line_length + min_spaces
    padding = maxWidth - mandatory_length
    if not min_spaces:
        return ''.join([curr_line[0], ' '*padding])
    else:
        separation, extra_spaces = divmod(padding, min_spaces)
        separation += 1
    for i in range(len(curr_line)-1):
        line.append(curr_line[i])
        spaces_to_append = separation
        if extra_spaces:
            extra_spaces -= 1
            spaces_to_append += 1
        for _ in range(spaces_to_append):
            line.append(' ')
    line.append(curr_line[-1])
    return ''.join(line)

def build_left_line(curr_line, maxWidth):
    line = []
    line_length = 0
    for i in range(len(curr_line)-1):
        word = curr_line[i]
        line.append(word)
        line.append(' ')
        line_length += 1 + len(word)
    line.append(curr_line[-1])
    line_length += len(curr_line[-1])
    while line_length < maxWidth:
        line_length += 1
        line.append(' ')
    return ''.join(line)

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ret = []
        curr_line, curr_line_length = [], 0
        for word in words:
            min_spaces = 0 if not curr_line else len(curr_line)
            if curr_line_length + min_spaces + len(word) <= maxWidth:
                curr_line.append(word)
                curr_line_length += len(word)
            else:
                ret.append(build_line(curr_line, curr_line_length, maxWidth))
                curr_line, curr_line_length = [word], len(word)
        if curr_line:
            ret.append(build_left_line(curr_line, maxWidth))
        return ret
# @lc code=end

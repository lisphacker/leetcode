class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_start = 0
        longest_end = -1

        start = 0
        end = -1
        letters = set()
        i = 0
        while i < len(s):
            c = s[i]
            if c in letters:
                if end - start > longest_end - longest_start:
                    longest_start = start
                    longest_end = end

                letters.remove(s[start])
                start += 1
            else:
                letters.add(c)
                end = i
                i += 1

        if end - start > longest_end - longest_start:
            longest_start = start
            longest_end = end

        return longest_end - longest_start + 1
        
def run_test(s: str):
    print(s, Solution().lengthOfLongestSubstring(s))

if __name__ == '__main__':
    run_test('abcabcbb')
    run_test('bbbbb')
    run_test('pwwkew')
    run_test('au')
    run_test('')

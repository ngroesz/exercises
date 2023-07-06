# https://leetcode.com/problems/roman-to-integer/

class Solution(object):
    value_by_symbol = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        accumulator = 0

        #import pdb; pdb.set_trace()

        skip_next = False
        for i, c in enumerate(s):
            if skip_next:
                skip_next = False
                continue
            if c == 'I':
                if i < len(s) - 1:
                    if s[i + 1] == 'V':
                        accumulator += 4
                        skip_next = True
                        continue
                    if s[i + 1] == 'X':
                        accumulator += 9
                        skip_next = True
                        continue
            if c == 'X':
                if i < len(s) - 1:
                    if s[i + 1] == 'L':
                        accumulator += 40
                        skip_next = True
                        continue
                    if s[i + 1] == 'C':
                        accumulator += 90
                        skip_next = True
                        continue
            if c == 'C':
                if i < len(s) - 1:
                    if s[i + 1] == 'D':
                        accumulator += 400
                        skip_next = True
                        continue
                    if s[i + 1] == 'M':
                        accumulator += 900
                        skip_next = True
                        continue

            accumulator += self.value_by_symbol[c]

        return accumulator


if __name__ == '__main__':
  s = Solution()

  print(s.romanToInt('III'))
  print(s.romanToInt('LVIII'))
  print(s.romanToInt('MCMXCIV'))

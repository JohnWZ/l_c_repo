'''
vi ~/.gitconfig 尝试修改终端和网页端用户名为John，试试是否依旧能commit
将上面一行整理到git笔记中
'''
class Solution:
    def romanToInt(self, s: str) -> int:
        numeral_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }

        result = 0

        for i in range(len(s)):
        	# if the latter value is less than or equal to the previous value, add directly
        	# when i = 0, i-1 means the last character. So add the first value directly
        	if numeral_map[s[i]] <= numeral_map[s[i-1]] or i == 0:
        		result += numeral_map[s[i]]
        	# if the latter value is greater than the previous value, 
        	# subtract it twice as it was added before
        	else:
        		result += numeral_map[s[i]] - numeral_map[s[i-1]]*2

        return result

def main():
    x = input("Input a Roman number: ")
    s = Solution()
    while x != 0:
        print(s.romanToInt(x))
        x = input("Input a Roman number: ")


if __name__ == '__main__':
    main()
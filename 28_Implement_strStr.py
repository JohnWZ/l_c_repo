class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

def main():
    haystack = input("Input the haystack: ")
    needle = input("Input the needle: ")
    s = Solution()
    while True:
        print(s.strStr(haystack, needle))
        haystack = input("Input the haystack: ")
        needle = input("Input the needle: ")


if __name__ == '__main__':
    main()
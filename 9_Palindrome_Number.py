class Solution:
    def isPalindrome(self, x: int) -> bool:
    	# these conditions are special condition based on the testcase
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        else:
            reverted_number = 0
            while x > reverted_number:
                reverted_number = int(reverted_number * 10 + x % 10)
                x //= 10
                
        #print (x, " and ", reverted_number)
        return (x == reverted_number or x == int(reverted_number/10))


def main():
    x = int(input("Input a number: "))
    s = Solution()
    while x != 0:
        print(s.isPalindrome(x))
        x = int(input("Input a number: "))


if __name__ == '__main__':
    main()
class Solution:
    def reverse(self, x: int) -> int:
        # check if the input integer overflows
        if x > 2**31-1 or x < -(2**31):
            return 0
        
        # if input is a negative number 
        isNegative = False
        if x < 0:
            isNegative = True
            x = -x
        # reverse the abs number
        a = 0
        while x != 0:
            a = a*10+x%10
            x = x//10
        
        if isNegative:
            a = -a
            
        # check if the output integer overflows
        if a > 2**31-1 or a < -(2**31):
            return 0
        else:
            return a

def main():
    x = int(input("Input a number: "))
    s = Solution()
    while x != 0:
        print(s.reverse(x))
        x = int(input("Input a number: "))


if __name__ == '__main__':
    main()
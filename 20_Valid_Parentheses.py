class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # make a dictionary to store all the parentheses
        lookup = {"(":")", "{":"}", "[":"]"}
        # 字典有点像指针array，遍历查找字典的时候扫描的是key，要引用对应的value时用[key]
        for elem in s:
            # if find a left parentheses, append it into a stack
            if elem in lookup:
                stack.append(elem)
            # when find a right parentheses, if it not matches the left parentheses at the top of the stack, return false
            # when find a right parentheses and the stack is empty, which means not match as well
            elif len(stack) == 0 or lookup[stack.pop()] != elem:
                return False

        # when go through all elements, but there are still something left in the stack, which means not match, return false
        if len(stack) != 0:
            return False
        return True


def main():
    x = input("Input a string of parentheses: ")
    s = Solution()
    while True:
        print(s.isValid(x))
        x = input("Input a string of parentheses: ")


if __name__ == '__main__':
    main()
class Solution:
    def generateParenthesis(self, n: int):
        # if n is 0, return empty list
        if n == 0:
            return []

        # initialize a empty list for result
        result = []
        # call the function
        self.generator(n,n,"",result)
        return result

    def generator(self, left, right, elem, result):
        # return condition:
        # if the number of right parenthesis is larger than the left side, return (get out the current level of interation)
        # otherwise it won't be a well-formed parentheses
        if right < left:
            return
        # the end of iteration: when the number of left and right are all reduced to 0, 
        # append it to result list
        if left == 0 and right == 0:
            result.append(elem)
        # when the number of left parenthesis still bigger than 0
        # go to next iteration, left-1 and add a "(" to the elem
        if left > 0:
            self.generator(left-1, right, elem+"(", result)
        if right > 0:
            self.generator(left, right-1, elem+")", result)
# draw a picture or calculate it by hand to have a better understanding of the process of this iteration

def main():
    n = int(input("Number of n:"))
    s = Solution()
    print(s.generateParenthesis(n))
    while True:
        n = int(input("Number of n:"))
        print(s.generateParenthesis(n))


if __name__ == '__main__':
    main()
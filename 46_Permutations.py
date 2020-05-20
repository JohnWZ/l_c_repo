class Solution:
    def permute(self, nums):
        if len(nums) <= 1:
            return [nums]

        answer = []
        # enumerate() can return both the index and the value of the number
        for i, num in enumerate(nums):
            # n is a list which contains all the elements of nums except i
            # 依次选择list中所有的元素作为开头，剩下的进入下一轮递归
            n = nums[:i] + nums[i+1:]
            # j will be a result of permute(n), get all results with for loop
            for j in self.permute(n):
                # append j to the list [num] which contains only one elment num
                answer.append([num] + j)

        return answer

def main():
    arr= []
    l = int(input("Length of the array:"))
    for i in range(l):
        elem = int(input(f"arr[{i}]:"))
        arr.append(elem)

    s = Solution()
    print(s.permute(arr))
    while True:
        arr.clear()
        l = int(input("Length of the array:"))
        for i in range(l):
            elem = int(input(f"arr[{i}]:"))
            arr.append(elem)
        print(s.permute(arr))


if __name__ == '__main__':
    main()
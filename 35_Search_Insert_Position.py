class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        return len(nums)

def main():
    arr= []
    l = int(input("Length of the array:"))
    for i in range(l):
        elem = int(input(f"arr[{i}]:"))
        arr.append(elem)
    target = int(input("Input the target:"))

    s = Solution()
    print(s.searchInsert(arr, target))
    while True:
        arr.clear()
        l = int(input("Length of the array:"))
        for i in range(l):
            elem = int(input(f"arr[{i}]:"))
            arr.append(elem)
        target = int(input("Input the target:"))
        print(s.searchInsert(arr, target))


if __name__ == '__main__':
    main()
class Solution:
    def removeDuplicates(self, nums) -> int:
        counter = 0;
        for i in range(len(nums)):
            if nums[counter] != nums[i]:
                counter += 1
                nums[counter] = nums[i]
                   
        return counter+1

def main():
    arr= []
    l = int(input("Length of the array:"))
    for i in range(l):
        string = input(f"arr[{i}]:")
        arr.append(string)

    s = Solution()
    length = s.removeDuplicates(arr)
    print("The length of the removeDuplicate() array is:", length)
    print("The removeDuplicate() array is: [", end = "")
    for i in range(length):
        print (arr[i], end = ", ")
    print("]")
    while True:
        arr.clear()
        l = int(input("Length of the array:"))
        for i in range(l):
            string = input(f"arr[{i}]:")
            arr.append(string)
        length = s.removeDuplicates(arr)
        print("The length of the removeDuplicate() array is:", length)
        print("The removeDuplicate() array is: [", end = "")
        for i in range(length):
            print (arr[i], end = ", ")
        print("]")


if __name__ == '__main__':
    main()
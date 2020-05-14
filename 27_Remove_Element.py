class Solution:
    def removeElement(self, nums, val: int) -> int:
        # make an indicator pointing to the last element
        # scan from the first element, when find the target value
        # swap it with the indicator-th element, and indicator move to previous element
        indicator = len(nums)-1
        print("->Indicator is: ", indicator)
        print("->Indicator value is: ", nums[indicator])
        for i in range(len(nums)):
            print("i=",i, f"nums[{i}]=", nums[i], "val=", val)
            if nums[i] == val:
                print('The target value finded at:',i) # <--The process cannot get in here?
                nums[indicator], nums[i] = nums[i], nums[indicator]
                indicator -= 1
                # move i back in case the swaped indicator-th element also equals to val
                i -= 1

        print("->New indicator is: ", indicator)
        print("The result list is: [", end = '')
        for i in range(indicator-1):
            print(nums[i], end = ', ')
        print("]")

        return indicator+1



def main():
    arr = []
    l = int(input("Length of the array: "))
    for i in range(l):
        string = input(f"arr[{i}]:")
        arr.append(string)

    val = int(input("The target value: "))

    s = Solution()
    n = s.removeElement(arr, val)
    print("The result length is: ", n)
    '''print("The result list is: [", end = '')
    for i in range(n):
        print(arr[i], end = ', ')
    print("]")'''
    while True:
        arr.clear()
        l = int(input("Length of the array: "))
        val = int(input("The target value: "))
        for i in range(l):
            string = input(f"arr[{i}]:")
            arr.append(string)
        n = s.removeElement(arr, val)
        print("The result length is: ", n)
        '''print("The result list is: [", end = '')
        for i in range(n):
            print(arr[i], end = ', ')
        print("]")'''


if __name__ == '__main__':
    main()
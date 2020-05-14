class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # make an indicator pointing to the last element
        # scan from the first element, when find the target value
        # swap it with the indicator-th element, and indicator move to previous element
        indicator = len(List)-1
        for i in range(len(List)):
            if List[i] == val:
                temp = List[indicator]
                List[indicator] = List[i]
                List[i] = List[indicator]
                indicator -= 1
                # move i back in case the swaped indicator-th element also equals to val
                i -= 1

        return indicator-1



def main():
    arr= []
    l = int(input("Length of the array:"))
    for i in range(l):
        string = input(f"arr[{i}]:")
        arr.append(string)

    s = Solution()
    n = s.removeElement(arr)
    print("The result list is: [", end = '')
    for i in range(n):
        print(arr[i], end = ', ')
    print("]")
    while True:
        arr.clear()
        l = int(input("Length of the array:"))
        for i in range(l):
            string = input(f"arr[{i}]:")
            arr.append(string)
        n = s.removeElement(arr)
    print("The result list is: [", end = '')
    for i in range(n):
        print(arr[i], end = ', ')
    print("]")


if __name__ == '__main__':
    main()
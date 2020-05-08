class Solution:
	def longestCommonPrefix(self, strs) -> str:
		if not strs:
			return ""

		# pick strs[0] as a reference, compare the rest of strs[1:]
		# if not match, return the longest common prefix so far
		# if all matchs but any of strs[1:] is shorter than strs[0], stop and return
		for i in range(len(strs[0])):
			for string in strs[1:]:
				if i >= len(string) or strs[0][i] != string[i]:
					return strs[0][:i]

		# if there is only one string in the array, return it
		return strs[0]

	# Another way to do it. Source: https://www.youtube.com/watch?v=cGQez9SiScw&list=PL2rWx9cCzU84eBz9Xfp9Rah5Fexq5yrh8&index=5
	def longestCommonPrefix2(self, strs) -> str:
		result = ""
		i = 0

		while True:
			try:
				#set用于遍历查找strs里面所有string的每一个string[i]，
				#把所有不同的string[i]都找出来返回，相同的字母只保留一个
				# so if the length of sets == 1, which means they all the same
				# add it to result
				# if the length is not == 1, just break
				sets = set(string[i] for string in strs)
				if len(sets) == 1:
					result += sets.pop()
					i += 1
				else: break
			except Exception as e:
				break

		return result

def main():
	arr= []
	l = int(input("Length of the array:"))
	for i in range(l):
		string = input(f"arr[{i}]:")
		arr.append(string)

	s = Solution()
	print(s.longestCommonPrefix2(arr))
	while True:
		arr.clear()
		l = int(input("Length of the array:"))
		for i in range(l):
			string = input(f"arr[{i}]:")
			arr.append(string)
		print(s.longestCommonPrefix(arr))


if __name__ == '__main__':
	main()
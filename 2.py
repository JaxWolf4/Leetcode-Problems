class Solution:
    def singleNumber(self, nums):
        lists = {}
        for number in nums:
            if number in lists:
                del lists[number]
            else:
                lists[number] = 1
        for values in lists.keys():
            print("The single number is", values)
            return values

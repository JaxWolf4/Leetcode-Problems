class Solution:
    def singleNumber(self, nums):
        lists = {}
        for number in nums:
            try:
                lists.pop(number)
            except:
                lists[number] = 1
        for values in lists.keys():
            print("The single number is", values)
            return values
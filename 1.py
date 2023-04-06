class Solution:
    def romanToInt(self, s):
        num = {"CM":900,"I":1,"IV":4,"V":5,"X":10,"CD":400,"C":100,"D":500,"M":1000,"IX":9,"XL":40,"XC":90,"L":50}
        total = 0
        counter = 0
        for letter in s:
            if letter not in num:
                print("Not Valid Num")
        while len(s) > counter:
            if s[counter:counter+2] in num:
                total = total + num[s[counter:counter+2]]
                counter = counter + 2
            elif s[counter:counter+1] in num:
                total = total + num[s[counter]]
                counter = counter + 1
            elif s[counter]:
                total = total + num[s[counter]]
                counter = counter + 1
        return total
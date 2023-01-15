class Solution:
    def letterCombinations(self, digits: str) :
        car = {'2' : 'abc',
        '3' : 'def',
        '4' : 'ghi',
        '5' : 'jkl',
        '6' : 'mno',
        '7' : 'pqrs',
        '8' : 'tuv',
        '9' : 'wxyz',}
        ans = []
        k = 1
        s = ""
        if len(digits) == 0 :
            return ans
        else :
            if len(digits) == 1 :
                for i in range(len(car[digits])) :
                    ans.append(car[digits][i])
                return ans
            if len(digits) == 2 :
                for x in range(len(car[digits[0]])) :
                    for y in range(len(car[digits[1]])) :
                        s = car[digits[0]][x]+car[digits[1]][y]
                        ans.append(s)
                return ans
            if len(digits) == 3 :
                for x in range(len(car[digits[0]])) :
                    for y in range(len(car[digits[1]])) :
                        for z in range(len(car[digits[2]])) :
                            s = car[digits[0]][x]+car[digits[1]][y]+car[digits[2]][z]
                            ans.append(s)
                return ans
            if len(digits) == 4 :
                for x in range(len(car[digits[0]])) :
                    for y in range(len(car[digits[1]])) :
                        for z in range(len(car[digits[2]])) :
                            for t in range(len(car[digits[3]])) :
                                s = car[digits[0]][x]+car[digits[1]][y]+car[digits[2]][z]+car[digits[3]][t]
                                ans.append(s)
                return ans

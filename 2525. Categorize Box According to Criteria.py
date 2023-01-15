class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) :
        b1 = False
        b2 = False
        h = False
        if int(length) >=10**4 or int(width) >= 10**4 or int(height) >= 10**4 :
            b1 = True
        if int(length*width*height) >= 10**9 :
            b2 = True
        if int(mass) >=100 :
            h = True
        if (b1 or b2) and h :
            return "Both"
        elif (not (b1 or b2)) and h :
            return "Heavy"
        elif (b1 or b2) and not h :
            return "Bulky"
        else :
            return "Neither"
            
        
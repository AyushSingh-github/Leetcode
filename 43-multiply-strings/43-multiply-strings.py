class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #Pythonic
        #return str(int(num1)*int(num2))
        
        #using ascii value to calc current value of string n -48 (ascii of 0) to get exact number form and then simple unit place multiplication and addition to previous ans to get full 3 digit num or bigger (for both num1 num2)
        
        unit_place,current1 = 1,0
        
        for i in range(len(num1)-1,-1,-1):
            current1 = ((ord(num1[i]) - 48)*unit_place)+current1
            unit_place *=10
        #print(current1)
        
        unit_place,current2 = 1,0
        
        for i in range(len(num2)-1,-1,-1):
            current2 = ((ord(num2[i]) - 48)*unit_place)+current2
            unit_place *=10
        #print(current2)
        
        return str(current1*current2)

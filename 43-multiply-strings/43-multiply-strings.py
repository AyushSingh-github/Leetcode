class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #Pythonic
        #return str(int(num1)*int(num2))
        
        #using ascii value to calc current value of string n -48 (ascii of 0) to get exact number form and then simple unit place multiplication and addition to previous ans to get full 3 digit num or bigger (for both num1 num2)
        '''
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
        '''

        # using pre defined values till 0 to 9 and find corresponding values in int form for calc

        num_map = {
            '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
            '5': 5, '6': 6, '7': 7, '8': 8, '9': 9
        }
        
        
        first_num = 0
        for i in range(len(num1)-1, -1, -1):
            first_num += num_map[num1[i]] * (10 ** (len(num1) - 1 - i))
        
        second_num = 0
        for i in range(len(num2)-1, -1, -1):
            second_num += num_map[num2[i]] * (10 ** (len(num2) - 1 - i))
            
        return f'{first_num * second_num}'

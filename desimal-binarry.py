def DecimalToBinary(num): 
      
   if num > 1: 
      DecimalToBinary(int(num / 2)) 
   print(num % 2,end = '') 

if __name__ == '__main__': 
       
   dec_val = int(input('number\n'))
        
   DecimalToBinary(dec_val)
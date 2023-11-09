        
file = open( "one_hundred.txt" )
"""
opens file 
"""
data = file.read()
"""
gains list of numbers in str format 
"""

lines = data.split("\n")


file.close


m_list = []


for numbers in lines :
    
    nums=numbers.split()
    
    for i in nums :
        
        numeral = int(i)
        
        if numeral not in m_list:
            
            m_list.append(numeral)

print(sorted(m_list))
   


       
       
        

        
        

   
    
 
        
        
        

    

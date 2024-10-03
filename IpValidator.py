FINAL_STATES = {'q33', 'q36', 'q38', 'q34', 'q37', 'q39', 'q13', 'q40', 'q49', 'q53'}

class IPValidator:
    def __init__(self):
        self.current_state = 'q0'

def is_letter_or_digit(self, char):
    return 'a' <= char <= 'z' or 'A' <= char <= 'Z' or '0' <= char <= '9'

def transition(self, char):
        print(f"Current state: {self.current_state}, Char: {char}")
        
        if self.current_state == 'q0':
            if char == 1:
                self.current_state = 'q19'
                return True 
            elif char == 2:
                self.current_state = 'q20'
                return True
            elif char == 0:
                self.current_state = 'q56'
                return True

        # Transiciones de 1
        elif self.current_state == 'q19':
            if char in '0123456789':  
                self.current_state = 'q1'
                return True 
            elif char == '.':
                self.current_state = 'q4'
                return True 

        elif self.current_state == 'q1':
            if char in '0123456789':
                self.current_state = 'q2'
                return True 
            elif char == '.':
                self.current_state = 'q4'
                return True  

        elif self.current_state == 'q2':
            if char == '.':
                self.current_state = 'q4'
                return True  

        # Transiciones de 2
        elif self.current_state == 'q20':
            if char in '012345':
                self.current_state = 'q3'
                return True 
            elif char in '0123456789':
                self.current_state = 'q22'
                return True 

        elif self.current_state == 'q3':
            if char == '.':
                self.current_state = 'q4'
                return True  
            elif char in '012345':
                self.current_state = 'q21'
                return True  
    
        elif self.current_state == 'q21':
            if char == '.':
                self.current_state = 'q4'
                return True 

        elif self.current_state == 'q22':
            if char == '.':
                self.current_state = 'q4'
                return True 
            elif char in '0123456789':
                self.current_state = 'q23'
                return True  
    
        elif self.current_state == 'q23':
            if char == '.':
                self.current_state = 'q4'
                return True 
        
        # Transiciones desde q4
        elif self.current_state == 'q4':
            if char == '1':
                self.current_state = 'q5'
                return True 
            elif char == '2':
                self.current_state = 'q6'
                return True

# Transiciones de 1
        elif self.current_state == 'q5':
            if char in '0123456789':  
                self.current_state = 'q24'
                return True
            elif char == '.':
                self.current_state = 'q7'
                return True 

        elif self.current_state == 'q24':
            if char in '0123456789':
                self.current_state = 'q16'
                return True 
            elif char == '.':
                self.current_state = 'q7'
                return True  

        elif self.current_state == 'q16':
            if char == '.':
                self.current_state = 'q7'
                return True  

        # Transiciones de 2
        elif self.current_state == 'q6':
            if char in '012345':
                self.current_state = 'q8'
                return True
            elif char in '0123456789':
                self.current_state = 'q17'
                return True  

        elif self.current_state == 'q8':
            if char == '.':
                self.current_state = 'q7'  
                return True
            elif char in '012345':
                self.current_state = 'q18' 
                return True 
    
        elif self.current_state == 'q18':
            if char == '.':
                self.current_state = 'q7'
                return True  

        elif self.current_state == 'q17':
            if char == '.':
                self.current_state = 'q7' 
                return True 
            elif char in '0123456789':
                self.current_state = 'q25'
                return True  
    
        elif self.current_state == 'q25':
            if char == '.':
                self.current_state = 'q7'
                return True 

 # Transiciones desde q7
        elif self.current_state == 'q7':
            if char == '1':
                self.current_state = 'q9'
                return True 
            elif char == '2':
                self.current_state = 'q10'
                return True

# Transiciones de 1
        elif self.current_state == 'q9':
            if char in '0123456789':  
                self.current_state = 'q1' 
                return True
            elif char == '.':
                self.current_state = 'q27'
                return True

        elif self.current_state == 'q11':
            if char in '0123456789':
                self.current_state = 'q26' 
                return True 
            elif char == '.':
                self.current_state = 'q27'
                return True

        elif self.current_state == 'q26':
            if char == '.':
                self.current_state = 'q27'  
                return True

        # Transiciones de 2
        elif self.current_state == 'q10':
            if char in '012345':
                self.current_state = 'q28' 
                return True
            elif char in '0123456789':
                self.current_state = 'q30'
                return True  

        elif self.current_state == 'q28':
            if char == '.':
                self.current_state = 'q27' 
                return True 
            elif char in '012345':
                self.current_state = 'q29' 
                return True 
    
        elif self.current_state == 'q29':
            if char == '.':
                self.current_state = 'q7' 
                return True 

        elif self.current_state == 'q30':
            if char == '.':
                self.current_state = 'q27' 
                return True 
            elif char in '0123456789':
                self.current_state = 'q31' 
                return True 
    
        elif self.current_state == 'q31':
            if char == '.':
                self.current_state = 'q27' 
                return True

 # Transiciones desde q27
        elif self.current_state == 'q27':
            if char == '1':
                self.current_state = 'q12' 
                return True
            elif char == '2':
                self.current_state = 'q32'
                return True

# Transiciones de 1
        elif self.current_state == 'q12':
            if char in '0123456789':  
                self.current_state = 'q33'
                return True 
            elif char == '/':
                self.current_state = 'qCIDR' 
                return True

        elif self.current_state == 'q33':
            if char in '0123456789':
                self.current_state = 'q34'  
                return True
            elif char == '/':
                self.current_state = 'qCIDR'
                return True  

        elif self.current_state == 'q34':
            if char == '/':
                self.current_state = 'qCIDR' 
                return True 

        # Transiciones de 2
        elif self.current_state == 'q32':
            if char in '012345':
                self.current_state = 'q36' 
                return True
            elif char in '0123456789':
                self.current_state = 'q38'  
                return True

        elif self.current_state == 'q36':
            if char == '/':
                self.current_state = 'qCIDR' 
                return True 
            elif char in '012345':
                self.current_state = 'q37'  
                return True
    
        elif self.current_state == 'q37':
            if char == '/':
                self.current_state = 'qCIDR'  
                return True

        elif self.current_state == 'q38':
            if char == '/':
                self.current_state = 'qCIDR' 
                return True
            elif char in '0123456789':
                self.current_state = 'q39'  
                return True
    
        elif self.current_state == 'q39':
            if char == '/':
                self.current_state = 'qCIDR' 
                return True

# Transiciones desde qCIDR
        elif self.current_state == 'qCIDR':
            if char == '8':
                self.current_state = 'q13' 
                return True
            elif char == '1':
                self.current_state = 'q15'
                return True
            elif char == '2':
                self.current_state = 'q47'
                return True

# Transiciones de 15

        elif self.current_state == 'q15':
            if char == '6':
                self.current_state = 'q40' 
                return True

# Transiciones de q47

        elif self.current_state == 'q47':
            if char == '4':
                self.current_state = 'q49' 
                return True
            
# Transiciones de hexadecimal

        elif self.current_state == 'q56':
            if char == 'x':
                self.current_state = 'q41' 
                return True
            
        elif self.current_state == 'q41':
            if char in '0123456789abcdefABCDEF':
                self.current_state = 'q42' 
                return True
            
        elif self.current_state == 'q42':
            if char in '0123456789abcdefABCDEF':
                self.current_state = 'q43' 
                return True
            
        elif self.current_state == 'q43':
            if char in '0123456789abcdefABCDEF':
                self.current_state = 'q44' 
                return True
            
        elif self.current_state == 'q44':
            if char in '0123456789abcdefABCDEF':
                self.current_state = 'q46' 
                return True
            
        elif self.current_state == 'q46':
            if char in '0123456789abcdefABCDEF':
                self.current_state = 'q48' 
                return True
            
        elif self.current_state == 'q48':
            if char in '0123456789abcdefABCDEF':
                self.current_state = 'q51' 
                return True
            
        elif self.current_state == 'q51':
            if char in '0123456789abcdefABCDEF':
                self.current_state = 'q52' 
                return True
            
        elif self.current_state == 'q52':
            if char in '0123456789abcdefABCDEF':
                self.current_state = 'q53' 
                return True
            
        return False

def is_valid_ip(self):
        return self.current_state in FINAL_STATES

def reset(self):
        self.current_state = 'q0'

def validate_ip(self, ip_string):
    self.reset()
    for char in ip_string:
        if not self.transition(char):
            return False, f"Error: La IP '{ip_string}' falló en el estado '{self.current_state}' con el caracter '{char}'"
    if self.is_valid_ip():
        return True, f"La IP '{ip_string}' es válida"
    else:
        return False, f"La IP '{ip_string}' no alcanzó un estado final válido"




        

         
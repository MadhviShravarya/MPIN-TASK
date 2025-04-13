'''Write code that tests the above written code using a set of inputs. Write at least 20 test case scenarios'''

weak_pins = set()
def is_common_mpinfour(mpin):
    #case 1: All digits are the same (eg, 1111, 2222, 5555 etc.)
    if mpin[0] == mpin[1] == mpin[2] == mpin[3]:
        return True
    
    #case 2: Sequential increasing or decreasing digits (eg, 1234, 6789, 5432 etc.)
    if (int(mpin[1]) == int(mpin[0]) + 1 and 
        int(mpin[2]) == int(mpin[1]) + 1 and 
        int(mpin[3]) == int(mpin[2]) + 1) or \
       (int(mpin[0]) == int(mpin[1]) + 1 and 
        int(mpin[1]) == int(mpin[2]) + 1 and 
        int(mpin[2]) == int(mpin[3]) + 1):
        return True
    
    #case 3 check 2121 or 1212 such patterned numbers
    if mpin[0] == mpin[2] and mpin[1] == mpin[3] and ( int(mpin[1]) == int(mpin[0])+1 or int(mpin[1]) == int(mpin[0])-1):
        return True
    
    return False  # If none of the conditions match, it's a strong MPIN

def is_common_mpinsix(mpin):
    #case 1: All digits are the same (eg, 1111, 2222, 5555 etc.)
    if mpin[0] == mpin[1] == mpin[2] == mpin[3]==mpin[4]==mpin[5]:
        return True
    
    #case 2: Sequential increasing or decreasing digits (eg, 123456, 654321, 543210 etc.)
    if all(int(mpin[i]) == int(mpin[i-1]) + 1 for i in range(1, len(mpin))) or \
        all(int(mpin[i]) == int(mpin[i - 1]) - 1 for i in range(1, len(mpin))):
        return True
    
    #case 3: check 121212 , 212121 - such patterned numbers
    if mpin[0] == mpin[2]==mpin[4] and mpin[1] == mpin[3]==mpin[5] and \
          (int(mpin[1]) == int(mpin[0])+1 or int(mpin[1]) == int(mpin[0])-1): 
        return True 
    #case 4: check 112233 , 001122 , 221100 - such patterned numbers
    if mpin[0]==mpin[1] and mpin[2]==mpin[3] and mpin[4]==mpin[5] and \
          ((int(mpin[2]) == int(mpin[1])+1 and int(mpin[4]) == int(mpin[3])+1) or (int(mpin[2]) == int(mpin[1])-1 and int(mpin[4]) == int(mpin[3])-1)): 
        return True    
    
    return False  # If none of the conditions match, it's a strong MPIN


months = {'jan': '01', 'feb': '02', 'mar': '03', 'apr': '04', 'may': '05', 'jun': '06', 
          'jul': '07', 'aug': '08', 'sep': '09', 'oct': '10', 'nov': '11', 'dec': '12'}


DOB = "20102001"
DOB=DOB.lower()
DD = DOB[:2] 
MM = months[DOB[2:5]] if DOB[2:5] in months else DOB[2:4]
YYYY = DOB[-4:]
YY=DOB[-2:]
DDMMYYYY = DD + MM + YYYY
DDMMYY=DD+MM+YY
DOB_poss={DD+MM+YY,DD+YY+MM,MM+DD+YY, MM+YY+DD, YY+MM+DD,YY+DD+MM,YYYY+MM,YYYY,
          MM+YYYY,YYYY+DD,DD+YYYY,DD+MM, MM+DD, MM+YY, YY+MM, DD+YY, YY+DD}

weak_pins.update(DOB_poss)

Spouse = "10Jan2000"
Spouse=Spouse.lower()
DD = Spouse[:2] 
MM = months[Spouse[2:5]] if Spouse[2:5] in months else Spouse[2:4]
YYYY = Spouse[-4:]
YY=Spouse[-2:]
Spouse_poss={DD+MM+YY,DD+YY+MM,MM+DD+YY, MM+YY+DD, YY+MM+DD,YY+DD+MM,YYYY,
             YYYY+MM,MM+YYYY,YYYY+DD,DD+YYYY,DD+MM, MM+DD, MM+YY, YY+MM, DD+YY, YY+DD}

weak_pins.update(Spouse_poss)

Anni = "22032025"
Anni=Anni.lower()
DD = Anni[:2] 
MM = months[Anni[2:5]] if Anni[2:5] in months else Anni[2:4]
YYYY = Anni[-4:]
YY=Anni[-2:]
Anni_poss={DD+MM+YY,DD+YY+MM,MM+DD+YY, MM+YY+DD, YY+MM+DD,YY+DD+MM,YYYY+MM,
           MM+YYYY,YYYY+DD,DD+YYYY,DD+MM, MM+DD, MM+YY, YY+MM, DD+YY, YY+DD,YYYY}

weak_pins.update(Anni_poss)

def test_case(mpin):
    if len(mpin)==4:
        if is_common_mpinfour(mpin):
            return "WEAK"
    if len(mpin)==6:    
        if is_common_mpinsix(mpin):
            return "WEAK"
    return "WEAK" if mpin in weak_pins else "STRONG"    
        
test_cases = [
    ("123456", "WEAK"), ("111111", "WEAK"), ("221100", "WEAK"), ("1111", "WEAK"),
    ("2001", "WEAK"), ("2025", "WEAK"), ("200120", "WEAK"), ("1010", "WEAK"),
    ("121212", "WEAK"), ("2203", "WEAK"), ("1001", "WEAK"), ("1709", "STRONG"),
    ("653290", "STRONG"), ("9089", "STRONG"), ("1357", "STRONG"),
    ("0000", "WEAK"), ("9999", "WEAK"), ("202503", "WEAK"), ("2000", "WEAK"),
    ("4758", "STRONG")
]
for mpin, expected in test_cases:
    result = test_case(mpin)
    print(f"MPIN: {mpin}, Expected: {expected}, Got: {result}, Result: {'PASS' if result == expected else 'FAIL'}")
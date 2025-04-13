'''Part D: Above with a 6-digit PIN '''

def is_common_mpin(mpin):
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
DOB = input("Enter the your DOB in DDMMYYY or DDMonYYYY format ").strip().lower()
DD = DOB[:2] 
MM = months[DOB[2:5]] if DOB[2:5] in months else DOB[2:4]
YYYY = DOB[-4:]
YY=DOB[-2:]
DDMMYYYY = DD + MM + YYYY
DDMMYY=DD+MM+YY
DOB_poss={DD+MM+YY,DD+YY+MM,MM+DD+YY, MM+YY+DD, YY+MM+DD,YY+DD+MM,YYYY+MM,MM+YYYY,YYYY+DD,DD+YYYY}

Spouse = input("Enter the your spouse bday in DDMMYYY or DDMonYYYY format ").strip().lower()
DD = Spouse[:2] 
MM = months[Spouse[2:5]] if Spouse[2:5] in months else Spouse[2:4]
YYYY = Spouse[-4:]
YY=Spouse[-2:]
Spouse_poss={DD+MM+YY,DD+YY+MM,MM+DD+YY, MM+YY+DD, YY+MM+DD,YY+DD+MM,YYYY+MM,MM+YYYY,YYYY+DD,DD+YYYY}

Anni = input("Enter the your Anniversary Date in DDMMYYY or DDMonYYYY format ").strip().lower()
DD = Anni[:2] 
MM = months[Anni[2:5]] if Anni[2:5] in months else Anni[2:4]
YYYY = Anni[-4:]
YY=Anni[-2:]
Anni_poss={DD+MM+YY,DD+YY+MM,MM+DD+YY, MM+YY+DD, YY+MM+DD,YY+DD+MM,YYYY+MM,MM+YYYY,YYYY+DD,DD+YYYY}

reason=[]

create_pin=input("Enter 6-digit pin to create pin: ")

if len(create_pin)!=6:
    print("Invalid Input! Enter exactly 6 digits.")

else:
    if is_common_mpin(create_pin):   
        reason.append("-COMMONLY_USED")
        print("Strength is WEAK " + " ".join(reason) )
    else:
        if create_pin in DOB_poss:
            reason.append("DEMOGRAPHIC_DOB_SELF")
            print("Strength is WEAK " + " ".join(reason) )
        elif create_pin in Spouse_poss:
            reason.append("DEMOGRAPHIC_DOB_SPOUSE") 
            print("Strength is WEAK " + " ".join(reason))
        elif create_pin in Anni_poss:
            reason.append("DEMOGRAPHIC_ANNIVERSARY")
            print("Strength is WEAK " + " ".join(reason))   
        else:
            print("strength is Strong " + " ".join(reason)) 

  
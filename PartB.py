'''Part B: Enhance the above to take user’s demographics as input and provides an output  
a. Strength: WEAK or STRONG '''

months = {'jan': '01', 'feb': '02', 'mar': '03', 'apr': '04', 'may': '05', 'jun': '06', 
          'jul': '07', 'aug': '08', 'sep': '09', 'oct': '10', 'nov': '11', 'dec': '12'}
DOB = input("Enter the your DOB in DDMMYYY or DDMonYYYY format ").strip().lower()
DD = DOB[:2] 
MM = months[DOB[2:5]] if DOB[2:5] in months else DOB[2:4]
YYYY = DOB[-4:]
YY=DOB[-2:]
DDMMYYYY = DD + MM + YYYY
DDMMYY=DD+MM+YY
DOB_poss={DD+MM, MM+DD, MM+YY, YY+MM, DD+YY, YY+DD,YYYY}

Spouse = input("Enter the your spouse bday in DDMMYYY or DDMonYYYY format ").strip().lower()
DD = Spouse[:2] 
MM = months[Spouse[2:5]] if Spouse[2:5] in months else Spouse[2:4]
YYYY = Spouse[-4:]
YY=Spouse[-2:]
Spouse_poss={DD+MM, MM+DD, MM+YY, YY+MM, DD+YY, YY+DD,YYYY}

Anni = input("Enter the your Anniversary Date in DDMMYYY or DDMonYYYY format ").strip().lower()
DD = Anni[:2] 
MM = months[Anni[2:5]] if Anni[2:5] in months else Anni[2:4]
YYYY = Anni[-4:]
YY=Anni[-2:]
Anni_poss={DD+MM, MM+DD, MM+YY, YY+MM, DD+YY, YY+DD,YYYY}

create_pin=input("Enter 4-digit pin to create pin: ")
if create_pin in DOB_poss or Anni_poss or Spouse_poss:
    print("Strength: WEAK")
else:
    print("Strength: STRONG")    


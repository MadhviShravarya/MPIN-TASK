'''Part A: Assume that the MPIN is 4-digits. Write a program that suggests if the MPIN is a commonly used one. 
Ignore the demographics for this part'''

# Function to check if the MPIN is weak
def is_common_mpin(mpin):
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
    if mpin[0] == mpin[2] and mpin[1] == mpin[3]: 
        return True
    
    return False  # If none of the conditions match, it's a strong MPIN

#taking input from a user
mpin = input("Enter a 4-digit MPIN: ")

#ensure that it is 4 digit number
if len(mpin) == 4 and mpin.isdigit():
    if is_common_mpin(mpin):
        print("COMMONLY_USED PIN")
    else:
        print("STRONG PIN")
else:
    print("Invalid Input! Enter exactly 4 digits.") 
